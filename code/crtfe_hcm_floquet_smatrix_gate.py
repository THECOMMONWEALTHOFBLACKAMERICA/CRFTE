import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass

@dataclass
class Case:
    N:int=48; M:int=4
    L0:float=625e-9; C0:float=250e-12
    mm:float=.10; me:float=.10
    fm:float=3e6; f0:float=150e3
    delta:float=0.0; R:float=50.0; Vsrc:float=1.0

def solve_column(c, nin, side='L', settle_periods=5, points_per_pump=50, nout=6, rtol=1e-8, atol=1e-11):
    N=c.N; Om=2*np.pi*c.fm; om0=2*np.pi*c.f0; win=om0+nin*Om
    kap=2*np.pi*c.M/c.N; idx=np.arange(N)
    pc=kap*idx; pl=kap*(idx+.5)+c.delta
    def rhs(t,y):
        q=y[:N]; ph=y[N:]
        C=c.C0*(1+c.me*np.cos(pc-Om*t)); L=c.L0*(1+c.mm*np.cos(pl-Om*t))
        v=q/C; i=ph/L
        src=c.Vsrc*np.exp(1j*win*t)
        VsL=src if side=='L' else 0j
        VsR=src if side=='R' else 0j
        iL=(VsL-v[0])/c.R
        # port node after final inductor: i_last=(vN-VsR)/R => vN=VsR+R*i_last
        vN=VsR+c.R*i[-1]
        dq=np.empty(N,dtype=complex); dq[0]=iL-i[0]; dq[1:]=i[:-1]-i[1:]
        dph=np.empty(N,dtype=complex); dph[:-1]=v[:-1]-v[1:]; dph[-1]=v[-1]-vN
        return np.r_[dq,dph]
    T0=1/c.f0; tend=(settle_periods+1)*T0
    sol=solve_ivp(rhs,(0,tend),np.zeros(2*N,dtype=complex),method='DOP853',rtol=rtol,atol=atol,
                  max_step=1/c.fm/points_per_pump,dense_output=True)
    ns=int(round(T0*c.fm*points_per_pump)); t=tend-T0+np.arange(ns)*(T0/ns)
    y=sol.sol(t); q=y[:N,:].T; ph=y[N:,:].T
    C=c.C0*(1+c.me*np.cos(pc[None,:]-Om*t[:,None])); L=c.L0*(1+c.mm*np.cos(pl[None,:]-Om*t[:,None]))
    v=q/C; i=ph/L
    src=c.Vsrc*np.exp(1j*win*t); VsL=src if side=='L' else 0j; VsR=src if side=='R' else 0j
    iL=(VsL-v[:,0])/c.R; vN=VsR+c.R*i[:,-1]; iR=(VsR-vN)/c.R
    aL=(v[:,0]+c.R*iL)/2; bL=(v[:,0]-c.R*iL)/2
    aR=(vN+c.R*iR)/2; bR=(vN-c.R*iR)/2
    # input amplitude should be Vsrc/2 on selected side
    outs=[]
    for n in range(-nout,nout+1):
        wn=om0+n*Om; basis=np.exp(-1j*wn*t)
        outs.append((n,wn,np.mean(bL*basis),np.mean(bR*basis)))
    ain=np.mean((aL if side=='L' else aR)*np.exp(-1j*win*t))
    return ain, outs

def gram_gate(c, nin_vals=(-2,-1,0,1,2), nout=6, settle_periods=5, points_per_pump=50):
    Om=2*np.pi*c.fm; om0=2*np.pi*c.f0
    cols=[]; labels=[]
    for side in ['L','R']:
        for nin in nin_vals:
            ain, outs=solve_column(c,nin,side,settle_periods,points_per_pump,nout)
            vec=[]
            win=om0+nin*Om
            for out_side_idx in [0,1]:
                for n,wn,bL,bR in outs:
                    b=(bL,bR)[out_side_idx]
                    sraw=b/ain
                    # action/photon-flux normalized amplitude
                    vec.append(sraw*np.sqrt(abs(win)/abs(wn)))
            cols.append(vec); labels.append((side,nin,win))
    S=np.array(cols,dtype=complex).T
    out_freqs=[]
    for out_side_idx in [0,1]:
        for n in range(-nout,nout+1): out_freqs.append(om0+n*Om)
    Vout=np.diag(np.sign(out_freqs))
    Vin=np.diag([np.sign(x[2]) for x in labels])
    G=S.conj().T@Vout@S
    E=G-Vin
    return labels,S,G,Vin,E, np.max(np.abs(E)), np.linalg.norm(E,'fro')

if __name__=='__main__':
    c=Case()
    labels,S,G,Vin,E,mx,fr=gram_gate(c,nin_vals=(-1,0,1),nout=5,settle_periods=4,points_per_pump=40)
    print('labels',labels)
    print('max_abs',mx,'fro',fr)
    print(np.abs(E))
