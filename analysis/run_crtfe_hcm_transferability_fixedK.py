import hashlib
import itertools
import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
import sys

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from crtfe_hcm_transferability_hb import solve_device

L0 = 625e-9
C0 = 250e-12
H = 15
tau = np.sqrt(L0 * C0)
kappa0 = np.pi / 6

PROTOCOL = ROOT / "protocol" / "CRTFE-HCM-TRANSFERABILITY-PROTOCOL-FIXED-K-2026-09-10.json"
OUT = ROOT / "data" / "transferability-generated"
OUT.mkdir(parents=True, exist_ok=True)


def fm_for_u(u):
    return abs(u) * kappa0 / (2 * np.pi * tau)


def case(N, ZL, ZR, delta_deg, r, u):
    return dict(N=int(N), ZL=float(ZL), ZR=float(ZR), delta_deg=float(delta_deg), r=float(r), u=float(u))


def one_job(args):
    label, idx, c, me, mm = args
    fm = fm_for_u(c["u"])
    kw = dict(
        N=c["N"], L0=L0, C0=C0, me=me, mm=mm, fm=fm, r=c["r"], u=c["u"],
        delta=np.deg2rad(c["delta_deg"]), H=H, ZL=c["ZL"], ZR=c["ZR"]
    )
    left = solve_device(side="L", **kw)
    right = solve_device(side="R", **kw)
    S21 = left["S_right"][H] * np.sqrt(c["ZL"] / c["ZR"])
    S12 = right["S_left"][H] * np.sqrt(c["ZR"] / c["ZL"])
    phi = float(np.angle(S21 / S12))
    w0 = 2 * np.pi * c["r"] * fm
    xi = float(-phi / (2 * c["N"] * w0 * tau))
    summary = dict(
        split=label, condition_id=idx, N=c["N"], ZL=c["ZL"], ZR=c["ZR"],
        delta_deg=c["delta_deg"], r=c["r"], u=c["u"], fm_Hz=fm, f0_Hz=c["r"] * fm,
        kappa_rad_per_cell=(kappa0 if c["u"] >= 0 else -kappa0), me=me, mm=mm,
        S21_real=S21.real, S21_imag=S21.imag, S21_mag=abs(S21),
        S12_real=S12.real, S12_imag=S12.imag, S12_mag=abs(S12),
        phi_nr_rad=phi, xi_hat=xi
    )
    raw = []
    for side, sol in [("L", left), ("R", right)]:
        Zin = c["ZL"] if side == "L" else c["ZR"]
        for j, h in enumerate(sol["hs"]):
            for port, key, Zout in [("L", "S_left", c["ZL"]), ("R", "S_right", c["ZR"])]:
                sval = sol[key][j] * np.sqrt(Zin / Zout)
                raw.append((
                    label, idx, c["N"], c["ZL"], c["ZR"], c["delta_deg"], c["r"], c["u"],
                    fm, c["r"] * fm, me, mm, side, port, int(h), float(sol["freqs"][j]),
                    float(sval.real), float(sval.imag), float(abs(sval)), float(np.angle(sval))
                ))
    return summary, raw


def run_jobs(jobs):
    summaries, raws = [], []
    with ProcessPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(one_job, job) for job in jobs]
        for i, future in enumerate(as_completed(futures), 1):
            s, r = future.result()
            summaries.append(s)
            raws.extend(r)
            if i % 20 == 0 or i == len(futures):
                print("progress", i, "/", len(futures), flush=True)
    return summaries, raws


def gf(name, u):
    if name == "u": return u
    if name == "u/(1-u)": return u / (1-u)
    if name == "u/(1-u^2)": return u / (1-u*u)
    if name == "u/(1-u^2)^(3/2)": return u / (1-u*u) ** 1.5
    raise ValueError(name)


def main():
    prot = json.loads(PROTOCOL.read_text())
    tr = prot["training_cartesian"]
    train = [case(N, ZL, ZR, d, r, u) for N, (ZL, ZR), d, r, u in itertools.product(
        tr["N"], tr["Z_pairs_ohm"], tr["delta_deg"], tr["r_f0_over_fm"], tr["u"]
    )]
    hp = prot["heldout_population"]
    pop = [case(N, ZL, ZR, d, r, u) for N, (ZL, ZR), d, r, u in itertools.product(
        hp["N"], hp["Z_pairs_ohm"], hp["delta_deg"], hp["r_f0_over_fm"], hp["u"]
    )]
    rng = np.random.default_rng(prot["heldout_sampling"]["seed"])
    sel = rng.choice(len(pop), size=prot["heldout_sampling"]["number_of_device_conditions"], replace=False)
    held = [pop[int(i)] for i in sel]
    split = {"seed": prot["heldout_sampling"]["seed"], "training": train, "heldout": held}
    split_path = OUT / "exact_split.json"
    split_path.write_text(json.dumps(split, indent=2))
    print("SPLIT_SHA256", hashlib.sha256(split_path.read_bytes()).hexdigest(), flush=True)

    jobs = [(label, idx, cc, .1, .1)
            for label, key in [("train", "training"), ("heldout", "heldout")]
            for idx, cc in enumerate(split[key])]
    sums, raws = run_jobs(jobs)
    sdf = pd.DataFrame(sums).sort_values(["split", "condition_id"])
    raw_cols = ["split","condition_id","N","ZL","ZR","delta_deg","r","u","fm_Hz","f0_Hz","me","mm",
                "incidence","output_port","h","freq_Hz","S_real","S_imag","S_mag","S_phase_rad"]
    rdf = pd.DataFrame(raws, columns=raw_cols).sort_values(["split","condition_id","incidence","output_port","h"])
    sdf.to_csv(OUT / "condition_summary.csv", index=False)
    rdf.to_csv(OUT / "full_sidebands.csv", index=False)

    T = sdf[sdf.split == "train"].copy()
    V = sdf[sdf.split == "heldout"].copy()
    models = ["u", "u/(1-u)", "u/(1-u^2)", "u/(1-u^2)^(3/2)"]
    rows = []
    for name in models:
        XT = np.c_[gf(name, T.u.values) * np.cos(np.deg2rad(T.delta_deg.values)), T.r.values**2]
        C, D = np.linalg.lstsq(XT, T.xi_hat.values, rcond=None)[0]
        XV = np.c_[gf(name, V.u.values) * np.cos(np.deg2rad(V.delta_deg.values)), V.r.values**2]
        pV = XV @ np.array([C, D])
        rows.append(dict(model=name, C=C, D=D,
                         train_SSE=np.sum((T.xi_hat.values - XT @ np.array([C, D]))**2),
                         heldout_SSE=np.sum((V.xi_hat.values - pV)**2),
                         heldout_RMSE=np.sqrt(np.mean((V.xi_hat.values - pV)**2))))
    pd.DataFrame(rows).sort_values("heldout_SSE").to_csv(OUT / "model_selection.csv", index=False)

    guT = gf("u/(1-u^2)", T.u.values) * np.cos(np.deg2rad(T.delta_deg.values))
    r2T = T.r.values**2
    Cfit, Dfit = np.linalg.lstsq(np.c_[guT, r2T], T.xi_hat.values, rcond=None)[0]
    Dfix = float(np.dot(r2T, T.xi_hat.values - .005 * guT) / np.dot(r2T, r2T))
    for tag, C, D in [("one_time_fit", float(Cfit), float(Dfit)), ("analytic_C_fixed", .005, Dfix)]:
        gu = gf("u/(1-u^2)", V.u.values) * np.cos(np.deg2rad(V.delta_deg.values))
        pred = C * gu + D * V.r.values**2
        err = pred - V.xi_hat.values
        non = np.abs(.005 * gu) >= 2e-4
        rel = np.full(len(V), np.nan)
        rel[non] = np.abs(err[non]) / np.maximum(np.abs(V.xi_hat.values[non]), 1e-30)
        w0 = 2*np.pi*V.f0_Hz.values
        phase_pred = -2*V.N.values*w0*tau*pred
        phase_err = np.abs(phase_pred - V.phi_nr_rad.values)
        score = dict(model=tag, C=C, D=D, n=len(V), n_nonnull=int(non.sum()),
                     median_rel_nonnull=np.nanmedian(rel), p95_rel_nonnull=np.nanpercentile(rel,95),
                     worst_rel_nonnull=np.nanmax(rel), median_abs_phase_err_rad=np.median(phase_err),
                     p95_abs_phase_err_rad=np.percentile(phase_err,95), worst_abs_phase_err_rad=np.max(phase_err),
                     heldout_SSE=np.sum(err**2))
        pd.DataFrame([score]).to_csv(OUT / f"score_{tag}.csv", index=False)
        if tag == "analytic_C_fixed":
            out = V.copy()
            out["xi_pred"] = pred
            out["xi_error"] = err
            out["relative_error_nonnull"] = rel
            out["phase_pred_rad"] = phase_pred
            out["abs_phase_error_rad"] = phase_err
            out.to_csv(OUT / "heldout_predictions.csv", index=False)


if __name__ == "__main__":
    main()
