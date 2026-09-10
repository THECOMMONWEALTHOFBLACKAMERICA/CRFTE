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
tau = np.sqrt(L0 * C0)
kappa = np.pi / 6
rows = []

for name, case in [
    ("lowu", dict(N=192, r=.03, u=.05, delta=np.deg2rad(22.5), ZL=50, ZR=75)),
    ("highu", dict(N=192, r=.03, u=.70, delta=np.deg2rad(22.5), ZL=50, ZR=75)),
]:
    prev = None
    fm = abs(case["u"]) * kappa / (2 * np.pi * tau)
    for H in range(10, 17):
        left = solve_device(side="L", H=H, L0=L0, C0=C0, me=.1, mm=.1, fm=fm, **case)
        right = solve_device(side="R", H=H, L0=L0, C0=C0, me=.1, mm=.1, fm=fm, **case)
        s21 = left["S_right"][H]
        s12 = right["S_left"][H]
        nr = np.angle(s21 / s12)
        max_all = max_sig = max_weak = np.nan
        if prev:
            pH, pL, pR = prev
            vals, sig, weak = [], [], []
            for h in range(-pH, pH + 1):
                for cur, old, key in [
                    (left, pL, "S_left"), (left, pL, "S_right"),
                    (right, pR, "S_left"), (right, pR, "S_right")
                ]:
                    a = cur[key][H + h]
                    b = old[key][pH + h]
                    change = abs(a - b)
                    vals.append(change)
                    scale = max(abs(a), abs(b))
                    if scale > 1e-3:
                        sig.append(change / scale)
                    else:
                        weak.append(change)
            max_all = max(vals)
            max_sig = max(sig) if sig else np.nan
            max_weak = max(weak) if weak else np.nan
        edge = max(abs(x[key][j]) for x in [left, right] for key in ["S_left", "S_right"] for j in [0, -1])
        rows.append(dict(case=name, u=case["u"], H=H, nr_phase=nr,
                         max_overlap_abs_change=max_all,
                         max_sig_relative_change=max_sig,
                         max_weak_abs_change=max_weak,
                         edge_sideband_max=edge))
        prev = (H, left, right)

out = ROOT / "data" / "CRTFE-HCM-fixedK-H-convergence-generated.csv"
pd.DataFrame(rows).to_csv(out, index=False)
print(pd.DataFrame(rows).to_string(index=False))
print(out)
