#!/usr/bin/env python3
from pathlib import Path
import argparse, sys
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
EXPECTED=ROOT/'data'/'expected'

def check_score(path):
    s=pd.read_csv(path).iloc[0]
    ok=[]
    ok.append(('median relative <= 5%', float(s.median_rel_nonnull)<=0.05))
    ok.append(('p95 relative <= 10%', float(s.p95_rel_nonnull)<=0.10))
    ok.append(('worst relative <= 20%', float(s.worst_rel_nonnull)<=0.20))
    ok.append(('median phase <= 2e-4 rad', float(s.median_abs_phase_err_rad)<=2e-4))
    ok.append(('p95 phase <= 5e-4 rad', float(s.p95_abs_phase_err_rad)<=5e-4))
    return ok

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--actual',default=str(ROOT/'reproduced'))
    ap.add_argument('--reference-only',action='store_true')
    a=ap.parse_args()
    actual=EXPECTED if a.reference_only else Path(a.actual)
    score=actual/'score_analytic_C_fixed.csv'
    models=actual/'model_selection_heldout.csv'
    if not score.exists() or not models.exists():
        print('missing reproduced score/model files',file=sys.stderr); return 2
    checks=check_score(score)
    m=pd.read_csv(models).sort_values('heldout_SSE')
    checks.append(('Dorian u/(1-u^2) has lowest heldout SSE', str(m.iloc[0].model)=='u/(1-u^2)'))
    for name,ok in checks: print(('PASS' if ok else 'FAIL'),name)
    if not a.reference_only:
        ref=pd.read_csv(EXPECTED/'score_analytic_C_fixed.csv').iloc[0]
        act=pd.read_csv(score).iloc[0]
        for col in ['median_rel_nonnull','p95_rel_nonnull','worst_rel_nonnull','median_abs_phase_err_rad','p95_abs_phase_err_rad','heldout_SSE']:
            av=float(act[col]); rv=float(ref[col]); tol=max(1e-11,abs(rv)*5e-5)
            ok=abs(av-rv)<=tol
            print(('PASS' if ok else 'WARN'),f'{col}: actual={av:.12g} reference={rv:.12g} tol={tol:.3g}')
    return 0 if all(ok for _,ok in checks) else 1

if __name__=='__main__': raise SystemExit(main())
