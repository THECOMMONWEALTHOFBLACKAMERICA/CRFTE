#!/usr/bin/env python3
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse, json, hashlib, sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'code'))
from crtfe_hcm_transferability_hb import solve_device

L0=625e-9; C0=250e-12; ME=0.1; MM=0.1; H=15
TAU=np.sqrt(L0*C0); KAPPA0=np.pi/6

def fm_for_u(u): return abs(u)*KAPPA0/(2*np.pi*TAU)

def one_job(args):
    label,idx,c=args
    fm=fm_for_u(c['u'])
    kw=dict(N=c['N'],L0=L0,C0=C0,me=ME,mm=MM,fm=fm,r=c['r'],u=c['u'],delta=np.deg2rad(c['delta_deg']),H=H,ZL=c['ZL'],ZR=c['ZR'])
    L=solve_device(side='L',**kw); R=solve_device(side='R',**kw)
    S21=L['S_right'][H]*np.sqrt(c['ZL']/c['ZR'])
    S12=R['S_left'][H]*np.sqrt(c['ZR']/c['ZL'])
    phi=float(np.angle(S21/S12)); w0=2*np.pi*c['r']*fm
    xi=float(-phi/(2*c['N']*w0*TAU))
    sm=dict(split=label,condition_id=idx,N=c['N'],ZL=c['ZL'],ZR=c['ZR'],delta_deg=c['delta_deg'],r=c['r'],u=c['u'],fm_Hz=fm,f0_Hz=c['r']*fm,kappa_rad_per_cell=(KAPPA0 if c['u']>=0 else -KAPPA0),me=ME,mm=MM,S21_real=S21.real,S21_imag=S21.imag,S21_mag=abs(S21),S12_real=S12.real,S12_imag=S12.imag,S12_mag=abs(S12),phi_nr_rad=phi,xi_hat=xi)
    raw=[]
    for side,sol in [('L',L),('R',R)]:
        Zin=c['ZL'] if side=='L' else c['ZR']
        for j,h in enumerate(sol['hs']):
            for port,key,Zout in [('L','S_left',c['ZL']),('R','S_right',c['ZR'])]:
                sval=sol[key][j]*np.sqrt(Zin/Zout)
                raw.append((label,idx,c['N'],c['ZL'],c['ZR'],c['delta_deg'],c['r'],c['u'],fm,c['r']*fm,ME,MM,side,port,int(h),float(sol['freqs'][j]),float(sval.real),float(sval.imag),float(abs(sval)),float(np.angle(sval))))
    return sm,raw

def run_jobs(jobs, workers):
    sums=[]; raws=[]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        fut=[ex.submit(one_job,j) for j in jobs]
        for i,f in enumerate(as_completed(fut),1):
            s,r=f.result(); sums.append(s); raws.extend(r)
            if i%20==0 or i==len(fut): print(f'progress {i}/{len(fut)}', flush=True)
    return sums,raws

def gf(name,u):
    if name=='u': return u
    if name=='u/(1-u)': return u/(1-u)
    if name=='u/(1-u^2)': return u/(1-u*u)
    if name=='u/(1-u^2)^(3/2)': return u/(1-u*u)**1.5
    raise KeyError(name)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default=str(ROOT/'reproduced')); ap.add_argument('--workers',type=int,default=4); a=ap.parse_args()
    out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
    split_path=ROOT/'protocol'/'heldout_split_fixedK.json'
    split=json.loads(split_path.read_text())
    print('split_sha256',hashlib.sha256(split_path.read_bytes()).hexdigest())
    jobs=[(label,idx,c) for label,key in [('train','training'),('heldout','heldout')] for idx,c in enumerate(split[key])]
    sums,raws=run_jobs(jobs,a.workers)
    sdf=pd.DataFrame(sums).sort_values(['split','condition_id'])
    cols=['split','condition_id','N','ZL','ZR','delta_deg','r','u','fm_Hz','f0_Hz','me','mm','incidence','output_port','h','freq_Hz','S_real','S_imag','S_mag','S_phase_rad']
    rdf=pd.DataFrame(raws,columns=cols).sort_values(['split','condition_id','incidence','output_port','h'])
    sdf.to_csv(out/'condition_summary_fixedK.csv',index=False); rdf.to_csv(out/'full_sidebands_fixedK.csv',index=False)
    T=sdf[sdf.split=='train'].copy(); V=sdf[sdf.split=='heldout'].copy()
    models=['u','u/(1-u)','u/(1-u^2)','u/(1-u^2)^(3/2)']; mr=[]
    for name in models:
        XT=np.c_[gf(name,T.u.values)*np.cos(np.deg2rad(T.delta_deg.values)),T.r.values**2]; C,D=np.linalg.lstsq(XT,T.xi_hat.values,rcond=None)[0]
        XV=np.c_[gf(name,V.u.values)*np.cos(np.deg2rad(V.delta_deg.values)),V.r.values**2]; pV=XV@np.array([C,D]); pT=XT@np.array([C,D])
        mr.append(dict(model=name,C=C,D=D,train_SSE=np.sum((T.xi_hat.values-pT)**2),heldout_SSE=np.sum((V.xi_hat.values-pV)**2),heldout_RMSE=np.sqrt(np.mean((V.xi_hat.values-pV)**2))))
    mdf=pd.DataFrame(mr).sort_values('heldout_SSE'); mdf.to_csv(out/'model_selection_heldout.csv',index=False)
    guT=gf('u/(1-u^2)',T.u.values)*np.cos(np.deg2rad(T.delta_deg.values)); r2T=T.r.values**2
    Cfit,Dfit=np.linalg.lstsq(np.c_[guT,r2T],T.xi_hat.values,rcond=None)[0]; Dfix=float(np.dot(r2T,T.xi_hat.values-.005*guT)/np.dot(r2T,r2T))
    for tag,C,D in [('one_time_fit',float(Cfit),float(Dfit)),('analytic_C_fixed',.005,Dfix)]:
        gu=gf('u/(1-u^2)',V.u.values)*np.cos(np.deg2rad(V.delta_deg.values)); pred=C*gu+D*V.r.values**2; err=pred-V.xi_hat.values
        non=np.abs(.005*gu)>=2e-4; rel=np.full(len(V),np.nan); rel[non]=np.abs(err[non])/np.maximum(np.abs(V.xi_hat.values[non]),1e-30)
        w0=2*np.pi*V.f0_Hz.values; pp=-2*V.N.values*w0*TAU*pred; pe=np.abs(pp-V.phi_nr_rad.values)
        sc=dict(model=tag,C=C,D=D,n=len(V),n_nonnull=int(non.sum()),median_rel_nonnull=np.nanmedian(rel),p95_rel_nonnull=np.nanpercentile(rel,95),worst_rel_nonnull=np.nanmax(rel),median_abs_phase_err_rad=np.median(pe),p95_abs_phase_err_rad=np.percentile(pe,95),worst_abs_phase_err_rad=np.max(pe),heldout_SSE=np.sum(err**2))
        pd.DataFrame([sc]).to_csv(out/f'score_{tag}.csv',index=False)
        if tag=='analytic_C_fixed':
            predout=V.copy(); predout['xi_pred']=pred; predout['xi_error']=err; predout['relative_error_nonnull']=rel; predout['phase_pred_rad']=pp; predout['abs_phase_error_rad']=pe; predout.to_csv(out/'heldout_predictions.csv',index=False)
    print(pd.DataFrame([sc]).to_string(index=False)); print(mdf.to_string(index=False))

if __name__=='__main__': main()
