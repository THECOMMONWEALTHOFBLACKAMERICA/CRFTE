#!/usr/bin/env python3
"""
Dorian Generalized DPR Audit v0.3 — repair-specific checks.

Adds the independent checks requested by the adversarial review:
F. Construct T_h from D^{-1} W_h using exact Laurent/Fraction algebra.
G. Even-support phase-origin covariance: non-unique maximizers.
H. Sparse {1,4} full-relation holonomy: triangle test is insufficient.
I. First-return series vs direct continuum quadrature through order 10.
J. Arbitrary-phase spectral-envelope stress at 0.97 * envelope pole.
K. 2x2 majorant determinant/radius identity checks.

Requires: NumPy.
"""

from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import csv
import json
import math
import cmath
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "generated_v03"
OUT.mkdir(exist_ok=True)

sys.path.insert(0, str(HERE))
from audit_generalized_dpr import first_return_poly, exact_xi, trunc_xi

def pclean(p):
    return {int(k): v for k,v in p.items() if v != 0}

def padd(a,b):
    r=defaultdict(F)
    for k,v in a.items(): r[k]+=v
    for k,v in b.items(): r[k]+=v
    return pclean(r)

def pscale(a,s):
    return pclean({k:v*s for k,v in a.items()})

def pmul(a,b):
    r=defaultdict(F)
    for ka,va in a.items():
        for kb,vb in b.items():
            r[ka+kb]+=va*vb
    return pclean(r)

def zero(): return {}
def const(x): return {} if x == 0 else {0:F(x)}

def matmul(A,B):
    C=[[{},{}],[{},{}]]
    for i in range(2):
        for j in range(2):
            s={}
            for k in range(2):
                s=padd(s,pmul(A[i][k],B[k][j]))
            C[i][j]=s
    return C

def matscale(A,s):
    return [[pscale(A[i][j],s) for j in range(2)] for i in range(2)]

def eqmat(A,B):
    return all(pclean(A[i][j])==pclean(B[i][j]) for i in range(2) for j in range(2))

def audit_F_kernel():
    rows=[]
    passed=True
    beta=F(2,7)
    Dinv=[
        [const(1+beta), const(beta)],
        [const(1), const(1)],
    ]
    for h in range(1,7):
        a=F(h+1, 50+h)
        b=F(h+2, 47+h)

        for sign in (+1,-1):
            exp=sign*h
            W=[
                [zero(), const(-beta*a/F(2))],
                [{exp:-b/F(2)}, zero()],
            ]
            constructed=matscale(matmul(Dinv,W),F(-1))
            expected=[
                [{exp:beta*b/F(2)}, const(beta*(1+beta)*a/F(2))],
                [{exp:b/F(2)}, const(beta*a/F(2))],
            ]
            ok=eqmat(constructed,expected)
            passed &= ok
            rows.append([h,sign,ok,str(constructed),str(expected)])

    with (OUT/"audit_F_kernel_from_L_exact.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["harmonic_h","sign","exact_match","constructed_T","expected_T"])
        w.writerows(rows)

    return {"pass":bool(passed),"cases":len(rows)}

def audit_G_even_support():
    H=4
    a=[0.0,0.11,0.0,0.055]
    b=[0.0,0.095,0.0,0.045]
    A=sum(a); B=sum(b)
    pole=1/math.sqrt((1+A)*(1+B))
    u=.64*pole
    gammaE=.37
    gammaM=-.51
    alpha=[h*gammaE for h in range(1,H+1)]
    gamma=[h*gammaM for h in range(1,H+1)]
    beta=u*u/(1-u*u)
    polys={n:first_return_poly(n,H,beta,a,b,alpha,gamma) for n in range(2,7)}

    d0=(gammaE-gammaM)%(2*math.pi)
    d1=(d0+math.pi)%(2*math.pi)
    ds=np.linspace(0,2*np.pi,1441,endpoint=False)
    exact=np.array([exact_xi(u,a,b,alpha,gamma,d,4096) for d in ds])

    rows=[]
    passed=True
    for N in [2,3,4,5,6]:
        tr=np.array([trunc_xi(u,polys,N,d) for d in ds])
        rem=np.abs(exact-tr)
        scanmax=float(rem.max())

        def remainder_at(d):
            return abs(exact_xi(u,a,b,alpha,gamma,d,8192)-trunc_xi(u,polys,N,d))
        r0=remainder_at(d0)
        r1=remainder_at(d1)

        periodic_equal=abs(r0-r1) <= max(1e-12, 2e-8*max(r0,r1,1e-30))
        both_max=(r0 >= scanmax*(1-5e-5) and r1 >= scanmax*(1-5e-5))
        ok=periodic_equal and both_max
        passed &= ok
        rows.append([N,d0*180/math.pi,d1*180/math.pi,r0,r1,scanmax,periodic_equal,both_max,ok])

    with (OUT/"audit_G_even_support_nonunique_maximizers.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["N","predicted_deg","repeated_deg","remainder_predicted",
                    "remainder_repeated","grid_scan_max","periodic_equal",
                    "both_match_global_max","pass"])
        w.writerows(rows)

    return {"pass":bool(passed),"gcd_support":2,"expected_period_deg":180.0}

def audit_H_sparse_holonomy():
    H=4
    a=[.14,0,0,.09]
    b=[.13,0,0,.08]
    alpha=[0.0,0.0,0.0,2.0]
    gamma=[0.0,0.0,0.0,2.0]
    u=.55
    beta=u*u/(1-u*u)
    polys={n:first_return_poly(n,H,beta,a,b,alpha,gamma) for n in range(2,9)}
    ds=np.linspace(0,2*np.pi,1441,endpoint=False)
    exact=np.array([exact_xi(u,a,b,alpha,gamma,d,4096) for d in ds])

    rows=[]
    moved=False
    for N in range(2,9):
        tr=np.array([trunc_xi(u,polys,N,d) for d in ds])
        rem=np.abs(exact-tr)
        imax=int(np.argmax(rem))
        ratio=float(rem[imax]/rem[0]) if rem[0] else float("inf")
        phase=float(ds[imax]*180/math.pi)
        if N>=4 and ratio>1.2 and min(phase,360-phase)>5:
            moved=True
        rows.append([N,float(rem[0]),float(rem[imax]),ratio,phase])

    no_triangle=True
    support={1,4}
    for h in support:
        for k in support:
            if h+k in support:
                no_triangle=False

    holonomy=(4*alpha[0]-alpha[3])%(2*math.pi)
    nonflat=min(holonomy,2*math.pi-holonomy)>1e-8

    with (OUT/"audit_H_sparse_1_4_holonomy.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["N","remainder_delta0","max_abs_remainder","max_over_delta0","argmax_deg"])
        w.writerows(rows)

    return {
        "pass":bool(no_triangle and nonflat and moved),
        "no_in_support_triangle":no_triangle,
        "relation":"4*1 - 1*4 = 0",
        "electric_relation_holonomy_rad":float(holonomy),
        "frustration_seen_in_remainder":moved,
    }

def audit_I_series_vs_quadrature():
    H=2
    a=[.12,.05]
    b=[.11,.04]
    A=sum(a); B=sum(b)
    pole=1/math.sqrt((1+A)*(1+B))
    u=.75*pole
    alpha=[0.0,0.0]
    gamma=[0.0,0.0]
    beta=u*u/(1-u*u)

    polys={n:first_return_poly(n,H,beta,a,b,alpha,gamma) for n in range(2,11)}
    exact=exact_xi(u,a,b,alpha,gamma,0.0,32768)

    rows=[]
    residuals=[]
    for N in range(2,11):
        trunc=trunc_xi(u,polys,N,0.0)
        resid=exact-trunc
        rel=abs(resid)/abs(exact)
        residuals.append(abs(resid))
        rows.append([N,exact,trunc,resid,rel])

    monotone=all(residuals[i+1] < residuals[i] for i in range(len(residuals)-1))
    final_rel=rows[-1][-1]
    passed=monotone and final_rel < 1e-6

    with (OUT/"audit_I_series_vs_quadrature.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["truncation_order_N","exact_quadrature_xi","first_return_truncation",
                    "exact_minus_truncation","relative_residual"])
        w.writerows(rows)

    return {
        "pass":bool(passed),
        "u_fraction_of_pole":.75,
        "monotone_residual":bool(monotone),
        "relative_residual_at_N10":float(final_rel),
    }

def audit_J_near_pole_envelope():
    rng=np.random.default_rng(4242)
    rows=[]
    failures=0
    maxratio=0.0

    for case in range(3):
        H=3
        A=.18
        B=.16
        a=(A*rng.dirichlet(np.ones(H))).tolist()
        b=(B*rng.dirichlet(np.ones(H))).tolist()
        alpha=rng.uniform(-np.pi,np.pi,H).tolist()
        gamma=rng.uniform(-np.pi,np.pi,H).tolist()

        pole=1/math.sqrt((1+A)*(1+B))
        u=.97*pole
        beta=u*u/(1-u*u)

        polys={n:first_return_poly(n,H,beta,a,b,alpha,gamma) for n in range(2,7)}
        env={n:first_return_poly(n,H,beta,a,b,[0]*H,[0]*H) for n in range(2,7)}

        ds=np.linspace(0,2*np.pi,181,endpoint=False)
        exact=np.array([exact_xi(u,a,b,alpha,gamma,d,8192) for d in ds])
        env_exact0=exact_xi(u,a,b,[0]*H,[0]*H,0.0,32768)

        for N in range(2,7):
            tr=np.array([trunc_xi(u,polys,N,d) for d in ds])
            maxrem=float(np.max(np.abs(exact-tr)))
            envtail=float(env_exact0-trunc_xi(u,env,N,0.0))
            ratio=maxrem/envtail
            ok=maxrem <= envtail*(1+2e-7)+1e-11
            failures += 0 if ok else 1
            maxratio=max(maxratio,ratio)
            rows.append([case,N,u,pole,u/pole,maxrem,envtail,ratio,ok])

    with (OUT/"audit_J_near_pole_envelope_097.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["case","N","u","envelope_pole","u_fraction_of_pole",
                    "max_abs_remainder","positive_envelope_tail","ratio","pass"])
        w.writerows(rows)

    return {
        "pass":bool(failures==0),
        "cases":len(rows),
        "failures":int(failures),
        "max_ratio":float(maxratio),
        "u_fraction_of_pole":.97,
    }

def audit_K_majorant():
    rng=np.random.default_rng(73013)
    failures=0
    rows=[]
    for case in range(100):
        A=float(rng.uniform(.01,.6))
        B=float(rng.uniform(.01,.6))
        pole=1/math.sqrt((1+A)*(1+B))
        frac=float(rng.uniform(.1,.99))
        u=frac*pole
        beta=u*u/(1-u*u)
        M=np.array([
            [beta*B, beta*(1+beta)*A],
            [B, beta*A],
        ],dtype=float)
        det=float(np.linalg.det(np.eye(2)-M))
        rhs=1-beta*(A+B+A*B)
        rho=max(abs(np.linalg.eigvals(M)))
        cond=(u*u*(1+A)*(1+B)<1)
        ok=abs(det-rhs)<1e-11 and ((rho<1)==cond)
        failures += 0 if ok else 1
        rows.append([case,A,B,u,pole,det,rhs,float(rho),cond,ok])

    with (OUT/"audit_K_majorant_identity.csv").open("w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["case","A","B","u","pole","det_I_minus_Tabs",
                    "one_minus_beta_A_B_AB","rho_Tabs","branch_condition","pass"])
        w.writerows(rows)

    return {"pass":bool(failures==0),"cases":len(rows),"failures":int(failures)}

def main():
    result={
        "audit_version":"0.3",
        "F_kernel_from_L":audit_F_kernel(),
        "G_even_support_nonunique_maximizers":audit_G_even_support(),
        "H_sparse_relation_holonomy":audit_H_sparse_holonomy(),
        "I_series_vs_quadrature":audit_I_series_vs_quadrature(),
        "J_near_pole_envelope":audit_J_near_pole_envelope(),
        "K_majorant_identity":audit_K_majorant(),
    }
    result["overall_pass"]=all(v["pass"] for k,v in result.items() if isinstance(v,dict) and "pass" in v)
    (OUT/"audit_summary_v0.3.json").write_text(json.dumps(result,indent=2))

    print("DORIAN GENERALIZED DPR REPAIR AUDIT v0.3")
    print("="*52)
    for k,v in result.items():
        if isinstance(v,dict) and "pass" in v:
            print(f"{k}: {'PASS' if v['pass'] else 'FAIL'}")
    print("-"*52)
    print("OVERALL:", "PASS" if result["overall_pass"] else "FAIL")
    if not result["overall_pass"]:
        raise SystemExit(1)

if __name__=="__main__":
    main()
