#!/usr/bin/env python3
"""
Dorian Generalized DPR Audit v0.1

Purpose
-------
Independent, deterministic computational audit for the post-v3 working
extensions of the Dorian Phase Relation.

This script checks four distinct claims:

A. Exact positive-spectrum path audit
   - Uses fractions.Fraction only.
   - Checks H=1,2,3 through total modulation order n=8.
   - Verifies:
       * no negative Laurent coefficients,
       * reflection symmetry c_r = c_-r,
       * ceiling |r| <= H floor(n/2),
       * odd orders absent for support {1,3},
       * odd orders present for support {1,2}.

B. Arbitrary-intrinsic-phase spectral-envelope stress
   - Deterministic NumPy seed.
   - Random H=2,3 finite spectra.
   - Direct exact continuum quadrature vs truncated first-return series.
   - Checks sup_delta |R_N(delta)| <= R_{N,+}(0) numerically.

C. Phase-origin covariance stress
   - Uses phases alpha_h=h*gamma_E and gamma_h=h*gamma_M.
   - Checks predicted worst phase delta = gamma_E - gamma_M mod 2pi.

D. Explicit phase-frustration counterexample
   - Demonstrates that delta=0 need not maximize truncation error once
     nonlinear intrinsic harmonic phase is introduced.

This is a computational audit of a WORKING extension framework.
It does not replace a proof and does not modify the published v3.0.0
sinusoidal-continuum theorem.
"""

from fractions import Fraction
from collections import defaultdict
import math
import cmath
import csv
import json
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent / "generated"
OUT.mkdir(exist_ok=True)

def padd(p, q):
    r = defaultdict(complex)
    for k, v in p.items():
        r[k] += v
    for k, v in q.items():
        r[k] += v
    return {k: v for k, v in r.items() if abs(v) > 1e-18}

def pscale(p, s, shift=0):
    return {k + shift: v * s for k, v in p.items()}

def poly_add_exact(p, q):
    r = defaultdict(Fraction)
    for k, v in p.items():
        r[k] += v
    for k, v in q.items():
        r[k] += v
    return {k: v for k, v in r.items() if v}

def poly_scale_exact(p, s, shift=0):
    return {k + shift: v * s for k, v in p.items() if v * s}

def matvec_T_exact(step, beta, avec, bvec, vec):
    h = abs(step)
    ah = avec.get(h, Fraction(0))
    bh = bvec.get(h, Fraction(0))
    half = Fraction(1, 2)

    out0 = poly_add_exact(
        poly_scale_exact(vec[0], beta * bh * half, step),
        poly_scale_exact(vec[1], beta * (1 + beta) * ah * half, 0),
    )
    out1 = poly_add_exact(
        poly_scale_exact(vec[0], bh * half, step),
        poly_scale_exact(vec[1], beta * ah * half, 0),
    )
    return [out0, out1]

def first_return_exact(order, H, beta, avec, bvec):
    states = {0: [{0: Fraction(1)}, {}]}
    steps = [
        s for h in range(1, H + 1) for s in (-h, h)
        if avec.get(h, 0) != 0 or bvec.get(h, 0) != 0
    ]
    final = [{}, {}]

    for k in range(1, order + 1):
        new = {}
        for pos, vec in states.items():
            for s in steps:
                pos2 = pos + s
                transformed = matvec_T_exact(s, beta, avec, bvec, vec)

                if k < order and pos2 == 0:
                    continue

                if k == order:
                    if pos2 != 0:
                        continue
                    final[0] = poly_add_exact(final[0], transformed[0])
                    final[1] = poly_add_exact(final[1], transformed[1])
                else:
                    if pos2 not in new:
                        new[pos2] = [{}, {}]
                    new[pos2][0] = poly_add_exact(new[pos2][0], transformed[0])
                    new[pos2][1] = poly_add_exact(new[pos2][1], transformed[1])
        states = new

    return poly_add_exact(final[0], poly_scale_exact(final[1], -beta))

def T_apply(step, beta, a, b, alpha, gamma, vec):
    h = abs(step)
    ah = a[h - 1]
    bh = b[h - 1]

    if step > 0:
        ep = cmath.exp(1j * alpha[h - 1])
        mp = cmath.exp(1j * gamma[h - 1])
    else:
        ep = cmath.exp(-1j * alpha[h - 1])
        mp = cmath.exp(-1j * gamma[h - 1])

    out0 = padd(
        pscale(vec[0], beta * bh * mp / 2, step),
        pscale(vec[1], beta * (1 + beta) * ah * ep / 2, 0),
    )
    out1 = padd(
        pscale(vec[0], bh * mp / 2, step),
        pscale(vec[1], beta * ah * ep / 2, 0),
    )
    return [out0, out1]

def first_return_poly(order, H, beta, a, b, alpha, gamma):
    states = {0: [{0: 1 + 0j}, {}]}
    steps = [
        s for h in range(1, H + 1) for s in (-h, h)
        if a[h - 1] > 0 or b[h - 1] > 0
    ]
    final = [{}, {}]

    for k in range(1, order + 1):
        new = {}
        for pos, vec in states.items():
            for s in steps:
                pos2 = pos + s
                tv = T_apply(s, beta, a, b, alpha, gamma, vec)

                if k < order and pos2 == 0:
                    continue

                if k == order:
                    if pos2 != 0:
                        continue
                    final[0] = padd(final[0], tv[0])
                    final[1] = padd(final[1], tv[1])
                else:
                    if pos2 not in new:
                        new[pos2] = [{}, {}]
                    new[pos2][0] = padd(new[pos2][0], tv[0])
                    new[pos2][1] = padd(new[pos2][1], tv[1])
        states = new

    return padd(final[0], pscale(final[1], -beta))

def peval_real(p, delta):
    return float(np.real(sum(v * np.exp(1j * k * delta) for k, v in p.items())))

def exact_xi(u, a, b, alpha, gamma, delta, nth=2048):
    th = np.linspace(0, 2 * np.pi, nth, endpoint=False)
    E = np.ones_like(th)
    M = np.ones_like(th)

    for h in range(1, len(a) + 1):
        E += a[h - 1] * np.cos(h * th + alpha[h - 1])
        M += b[h - 1] * np.cos(h * (th + delta) + gamma[h - 1])

    d = 1 - u * u * E * M
    J0 = np.mean(1 / d)
    JE = np.mean(E / d)
    JM = np.mean(M / d)

    return float((1 / u) * (1 - J0 / (J0 * J0 - u * u * JE * JM)))

def trunc_xi(u, polys, N, delta):
    return sum(peval_real(polys[n], delta) for n in range(2, N + 1)) / u

def audit_A():
    beta = Fraction(2, 7)
    configs = {
        "H1_single_sinusoid": (
            1,
            {1: Fraction(1, 10)},
            {1: Fraction(3, 25)},
        ),
        "H2_positive": (
            2,
            {1: Fraction(1, 10), 2: Fraction(1, 25)},
            {1: Fraction(3, 25), 2: Fraction(1, 30)},
        ),
        "H3_positive": (
            3,
            {1: Fraction(1, 10), 2: Fraction(1, 25), 3: Fraction(1, 40)},
            {1: Fraction(3, 25), 2: Fraction(1, 30), 3: Fraction(1, 35)},
        ),
        "support_1_3_normalized_odd": (
            3,
            {1: Fraction(1, 10), 3: Fraction(1, 40)},
            {1: Fraction(3, 25), 3: Fraction(1, 35)},
        ),
    }

    rows = []
    pass_all = True

    for name, (H, avec, bvec) in configs.items():
        for n in range(2, 9):
            p = first_return_exact(n, H, beta, avec, bvec)
            coeffs = list(p.values())
            neg = sum(v < 0 for v in coeffs)
            sym = all(p.get(k, Fraction(0)) == p.get(-k, Fraction(0)) for k in p)
            max_exp = max((abs(k) for k in p), default=0)
            ceiling = H * (n // 2)
            ceiling_pass = max_exp <= ceiling

            if neg != 0 or not sym or not ceiling_pass:
                pass_all = False

            rows.append([
                name, H, n, bool(p), len(p), neg, sym,
                max_exp, ceiling, ceiling_pass
            ])

    h13 = [r for r in rows if r[0] == "support_1_3_normalized_odd" and r[2] % 2 == 1]
    h12 = [r for r in rows if r[0] == "H2_positive" and r[2] % 2 == 1]

    odd_absent_h13 = all(not r[3] for r in h13)
    odd_present_h12 = any(r[3] for r in h12)
    pass_all = pass_all and odd_absent_h13 and odd_present_h12

    with (OUT / "audit_A_exact_path.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "configuration","H","order_n","nonzero_order","laurent_monomials",
            "negative_coefficients","reflection_symmetric",
            "max_abs_phase_exponent","ceiling_H_floor_n_over_2","ceiling_pass"
        ])
        w.writerows(rows)

    return {
        "pass": bool(pass_all),
        "odd_absent_support_1_3": bool(odd_absent_h13),
        "odd_present_support_1_2": bool(odd_present_h12),
        "rows": int(len(rows)),
    }

def audit_B():
    rng = np.random.default_rng(12092026)
    rows = []
    failures = 0
    max_ratio = 0.0

    for H in [2, 3]:
        for case in range(10):
            A = float(rng.uniform(.08, .32))
            B = float(rng.uniform(.08, .32))
            a = (A * rng.dirichlet(np.ones(H))).tolist()
            b = (B * rng.dirichlet(np.ones(H))).tolist()
            alpha = rng.uniform(-np.pi, np.pi, H).tolist()
            gamma = rng.uniform(-np.pi, np.pi, H).tolist()

            pole = 1 / math.sqrt((1 + A) * (1 + B))
            u = float(rng.uniform(.40, .76) * pole)
            beta = u * u / (1 - u * u)

            polys = {
                n: first_return_poly(n, H, beta, a, b, alpha, gamma)
                for n in range(2, 7)
            }
            env_polys = {
                n: first_return_poly(n, H, beta, a, b, [0] * H, [0] * H)
                for n in range(2, 7)
            }

            deltas = np.linspace(0, 2 * np.pi, 361, endpoint=False)
            exact = np.array([
                exact_xi(u, a, b, alpha, gamma, d, 2048)
                for d in deltas
            ])
            env_exact0 = exact_xi(u, a, b, [0] * H, [0] * H, 0, 4096)

            for N in [2, 3, 4, 5, 6]:
                trunc = np.array([
                    trunc_xi(u, polys, N, d) for d in deltas
                ])
                rem = np.abs(exact - trunc)
                imax = int(np.argmax(rem))

                env_trunc0 = trunc_xi(u, env_polys, N, 0)
                env_tail = env_exact0 - env_trunc0
                maxrem = float(rem[imax])
                ratio = maxrem / env_tail if env_tail > 0 else float("nan")

                passed = maxrem <= env_tail * (1 + 2e-8) + 1e-12
                if not passed:
                    failures += 1
                if np.isfinite(ratio):
                    max_ratio = max(max_ratio, ratio)

                rows.append([
                    H, case, A, B, u, pole, u / pole, N,
                    float(deltas[imax] * 180 / np.pi),
                    maxrem, env_tail, ratio, passed
                ])

    with (OUT / "audit_B_spectral_envelope.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "H","case","A_abs_sum","B_abs_sum","u","envelope_pole_u",
            "u_fraction_of_envelope_pole","truncation_order_N",
            "argmax_remainder_phase_deg","max_abs_remainder_arbitrary_phase",
            "positive_envelope_tail_at_delta0",
            "frustration_factor_maxrem_over_envelope","envelope_bound_pass"
        ])
        w.writerows(rows)

    return {
        "pass": bool(failures == 0),
        "failures": int(failures),
        "cases": int(len(rows)),
        "max_frustration_factor": float(max_ratio),
    }

def audit_C():
    rng = np.random.default_rng(992026)
    rows = []
    max_err_deg = 0.0

    for case in range(12):
        H = int(rng.choice([2, 3, 4]))
        A = float(rng.uniform(.06, .28))
        B = float(rng.uniform(.06, .28))
        a = (A * rng.dirichlet(np.ones(H))).tolist()
        b = (B * rng.dirichlet(np.ones(H))).tolist()

        gammaE = float(rng.uniform(-np.pi, np.pi))
        gammaM = float(rng.uniform(-np.pi, np.pi))
        alpha = [h * gammaE for h in range(1, H + 1)]
        gamma = [h * gammaM for h in range(1, H + 1)]

        pole = 1 / math.sqrt((1 + A) * (1 + B))
        u = .62 * pole
        beta = u * u / (1 - u * u)

        polys = {
            n: first_return_poly(n, H, beta, a, b, alpha, gamma)
            for n in range(2, 6)
        }

        ds = np.linspace(0, 2 * np.pi, 1441, endpoint=False)
        exact = np.array([
            exact_xi(u, a, b, alpha, gamma, d, 2048)
            for d in ds
        ])
        trunc = np.array([
            trunc_xi(u, polys, 3, d) for d in ds
        ])
        rem = np.abs(exact - trunc)
        imax = int(np.argmax(rem))

        predicted = (gammaE - gammaM) % (2 * np.pi)
        actual = ds[imax]
        err = ((actual - predicted + np.pi) % (2 * np.pi) - np.pi)
        err_deg = abs(err * 180 / np.pi)
        max_err_deg = max(max_err_deg, err_deg)

        rows.append([
            case, H, gammaE * 180 / np.pi, gammaM * 180 / np.pi,
            predicted * 180 / np.pi, actual * 180 / np.pi,
            err * 180 / np.pi
        ])

    with (OUT / "audit_C_phase_origin_covariance.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "case","H","gamma_E_deg","gamma_M_deg",
            "predicted_worst_phase_deg","observed_worst_phase_deg",
            "circular_error_deg"
        ])
        w.writerows(rows)

    return {
        "pass": bool(max_err_deg < 0.35),
        "cases": int(len(rows)),
        "max_abs_circular_error_deg": float(max_err_deg),
        "acceptance_deg": 0.35,
    }

def audit_D():
    u = .55
    a = [.18, .12]
    b = [.17, .11]
    phi = 2 * np.pi / 3
    alpha = [0.0, phi]
    gamma = [0.0, phi]
    beta = u * u / (1 - u * u)

    polys = {
        n: first_return_poly(n, 2, beta, a, b, alpha, gamma)
        for n in range(2, 7)
    }

    ds = np.linspace(0, 2 * np.pi, 1441, endpoint=False)
    exact = np.array([
        exact_xi(u, a, b, alpha, gamma, d, 4096)
        for d in ds
    ])

    rows = []
    found = False
    for N in [2, 3, 4, 5, 6]:
        trunc = np.array([trunc_xi(u, polys, N, d) for d in ds])
        rem = np.abs(exact - trunc)
        imax = int(np.argmax(rem))
        max_over_zero = float(rem[imax] / rem[0]) if rem[0] else float("nan")

        if N == 2 and max_over_zero > 1.2 and abs(ds[imax]) > 0.1:
            found = True

        rows.append([
            u, a[0], a[1], b[0], b[1], 120.0, 120.0, N,
            float(rem[0]), float(rem[imax]),
            float(ds[imax] * 180 / np.pi), max_over_zero
        ])

    with (OUT / "audit_D_phase_frustration_counterexample.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "u","a1","a2","b1","b2","alpha2_deg","gamma2_deg",
            "truncation_order_N","remainder_at_delta0","max_abs_remainder",
            "argmax_phase_deg","max_over_delta0"
        ])
        w.writerows(rows)

    return {
        "pass": bool(found),
        "criterion": "At N=2, max remainder must exceed delta=0 remainder by >20% and occur away from 0.",
    }

def main():
    A = audit_A()
    B = audit_B()
    C = audit_C()
    D = audit_D()

    result = {
        "audit_version": "0.1",
        "numpy_version": np.__version__,
        "A_exact_positive_spectrum": A,
        "B_arbitrary_phase_envelope": B,
        "C_phase_origin_covariance": C,
        "D_phase_frustration_counterexample": D,
    }
    result["overall_pass"] = all([
        A["pass"], B["pass"], C["pass"], D["pass"]
    ])

    (OUT / "audit_summary.json").write_text(json.dumps(result, indent=2))

    print("DORIAN GENERALIZED DPR AUDIT v0.1")
    print("=" * 40)
    print("A exact positive-spectrum path audit:", "PASS" if A["pass"] else "FAIL")
    print("  odd absent support {1,3}:", A["odd_absent_support_1_3"])
    print("  odd present support {1,2}:", A["odd_present_support_1_2"])
    print("B arbitrary-phase spectral envelope:", "PASS" if B["pass"] else "FAIL")
    print("  failures:", B["failures"], "/", B["cases"])
    print("  max frustration factor:", B["max_frustration_factor"])
    print("C phase-origin covariance:", "PASS" if C["pass"] else "FAIL")
    print("  max |phase error| deg:", C["max_abs_circular_error_deg"])
    print("D explicit frustration counterexample:", "PASS" if D["pass"] else "FAIL")
    print("-" * 40)
    print("OVERALL:", "PASS" if result["overall_pass"] else "FAIL")

    if not result["overall_pass"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
