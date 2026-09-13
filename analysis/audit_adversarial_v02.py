#!/usr/bin/env python3
"""Additional adversarial exact-rational audit for Generalized DPR v0.2."""

from fractions import Fraction as F
import csv
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from audit_generalized_dpr import first_return_exact

OUT = HERE / "generated"
OUT.mkdir(exist_ok=True)
beta = F(2, 7)

def active_H(avec, bvec):
    support = sorted(set(
        [h for h,v in avec.items() if v != 0] +
        [h for h,v in bvec.items() if v != 0]
    ))
    return max(support), support

def check(name, nominal_H, avec, bvec, orders):
    Hstar, support = active_H(avec, bvec)
    rows=[]
    ok=True
    for n in orders:
        p=first_return_exact(n, nominal_H, beta, avec, bvec)
        coeffs=list(p.values())
        neg=sum(v<0 for v in coeffs)
        sym=all(p.get(k,F(0))==p.get(-k,F(0)) for k in p)
        max_exp=max((abs(k) for k in p),default=0)
        ceiling=Hstar*(n//2)
        ceiling_pass=max_exp<=ceiling
        row=[name,nominal_H,Hstar,"{" + ",".join(map(str,support)) + "}",
             n,bool(p),len(p),neg,sym,max_exp,ceiling,ceiling_pass]
        rows.append(row)
        if neg or not sym or not ceiling_pass:
            ok=False
    return ok, rows

tests=[
("H4_concentrated_top",4,
 {1:F(1,1000),2:F(1,1000),3:F(1,1000),4:F(1,4)},
 {1:F(1,1000),2:F(1,1000),3:F(1,1000),4:F(1,5)}, range(2,13)),
("H5_uniform",5,
 {h:F(1,20) for h in range(1,6)},
 {h:F(1,25) for h in range(1,6)}, range(2,13)),
("H4_asymmetric_channels",4,
 {1:F(1,5),2:F(1,50),3:F(1,5),4:F(1,50)},
 {1:F(1,50),2:F(1,5),3:F(1,50),4:F(1,5)}, range(2,13)),
("nominal_H3_support_2",3,
 {2:F(1,8)}, {2:F(1,7)}, range(2,13)),
("H6_gap_support_1_4_6",6,
 {1:F(1,20),4:F(1,15),6:F(1,10)},
 {1:F(1,18),4:F(1,12),6:F(1,9)}, range(2,13)),
]

allrows=[]
overall=True
for t in tests:
    ok,rows=check(*t)
    overall &= ok
    allrows.extend(rows)

gap=[r for r in allrows if r[0]=="H6_gap_support_1_4_6"]
gap_o3=next(r for r in gap if r[4]==3)
gap_o5=next(r for r in gap if r[4]==5)
onset_pass=(gap_o3[5] is False and gap_o5[5] is True)
overall &= onset_pass

with (OUT/"audit_E_adversarial_exact_v02.csv").open("w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["configuration","nominal_H","active_H_star","support","order_n",
                "nonzero_order","laurent_monomials","negative_coefficients",
                "reflection_symmetric","max_abs_phase_exponent",
                "sharp_ceiling_Hstar_floor_n_over_2","ceiling_pass"])
    w.writerows(allrows)

print("GENERALIZED DPR ADVERSARIAL EXACT AUDIT v0.2")
print("="*50)
for name,*_ in tests:
    rs=[r for r in allrows if r[0]==name]
    fail=[r for r in rs if r[7] or not r[8] or not r[11]]
    print(f"{name}: {'PASS' if not fail else 'FAIL'}")
print("support {1,4,6}: O(3)=0 and O(5)!=0:", "PASS" if onset_pass else "FAIL")
print("-"*50)
print("OVERALL:", "PASS" if overall else "FAIL")

if not overall:
    raise SystemExit(1)
