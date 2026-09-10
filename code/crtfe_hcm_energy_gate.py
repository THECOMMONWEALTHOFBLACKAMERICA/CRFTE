import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass

@dataclass
class Case:
    N:int=48; M:int=4
    L0:float=625e-9; C0:float=250e-12
    mm:float=0.10; me:float=0.10
    fm:float=3e6; f0:float=150e3
    delta:float=0.0
    Rs:float=50.0; RL:float=50.0
    Vsrc:float=1.0


def rhs_factory(c:Case):
    N=c.N; Om=2*np.pi*c.fm; om=2*np.pi*c.f0
    kappa=2*np.pi*c.M/c.N
    idx=np.arange(N)
    pc=kappa*idx
    pl=kappa*(idx+0.5)+c.delta
    def rhs(t,y):
        q=y[:N]; ph=y[N:]
        C=c.C0*(1+c.me*np.cos(pc-Om*t))
        L=c.L0*(1+c.mm*np.cos(pl-Om*t))
        v=q/C; i=ph/L
        Vs=c.Vsrc*np.cos(om*t)
        isrc=(Vs-v[0])/c.Rs
        dq=np.empty(N)
        dq[0]=isrc-i[0]
        dq[1:]=i[:-1]-i[1:]
        # output node has no shunt C; vout = RL * i_last
        vout=c.RL*i[-1]
        dph=np.empty(N)
        dph[:-1]=v[:-1]-v[1:]
        dph[-1]=v[-1]-vout
        return np.r_[dq,dph]
    return rhs


def diagnostics(c:Case, t, y):
    N=c.N; Om=2*np.pi*c.fm; om=2*np.pi*c.f0
    kappa=2*np.pi*c.M/c.N; idx=np.arange(N)
    pc=kappa*idx; pl=kappa*(idx+0.5)+c.delta
    # arrays nt x N
    angc=pc[None,:]-Om*t[:,None]
    angl=pl[None,:]-Om*t[:,None]
    C=c.C0*(1+c.me*np.cos(angc)); L=c.L0*(1+c.mm*np.cos(angl))
    Cdot=c.C0*c.me*Om*np.sin(angc); Ldot=c.L0*c.mm*Om*np.sin(angl)
    q=y[:N,:].T; ph=y[N:,:].T
    v=q/C; i=ph/L
    Vs=c.Vsrc*np.cos(om*t)
    isrc=(Vs-v[:,0])/c.Rs
    vout=c.RL*i[:,-1]
    pin=v[:,0]*isrc
    pout=vout*i[:,-1]
    ppump=-0.5*np.sum(v*v*Cdot,axis=1)-0.5*np.sum(i*i*Ldot,axis=1)
    U=0.5*np.sum(q*q/C,axis=1)+0.5*np.sum(ph*ph/L,axis=1)
    return pin,pout,ppump,U,v[:,0],isrc,vout,i[:,-1]


def avg_trap(t,x): return np.trapezoid(x,t)/(t[-1]-t[0])

def run(c:Case, settle_periods=12, eval_periods=1, points_per_pump=120, rtol=3e-10, atol=1e-12):
    # f0/fm=1/20 in default => carrier period is common period.
    T0=1/c.f0
    tend=(settle_periods+eval_periods)*T0
    rhs=rhs_factory(c)
    sol=solve_ivp(rhs,(0,tend),np.zeros(2*c.N),method='DOP853',rtol=rtol,atol=atol,
                  max_step=1/c.fm/points_per_pump,dense_output=True)
    t0=settle_periods*T0
    ns=max(4001,int(eval_periods*T0*c.fm*points_per_pump)+1)
    t=np.linspace(t0,tend,ns)
    y=sol.sol(t)
    pin,pout,ppump,U,*ports=diagnostics(c,t,y)
    Pin=avg_trap(t,pin); Pout=avg_trap(t,pout); Ppump=avg_trap(t,ppump)
    dU=(U[-1]-U[0])/(t[-1]-t[0])
    closure=Pin+Ppump-Pout-dU
    scale=max(abs(Pin),abs(Pout),abs(Ppump),1e-30)
    return {
        'Pin':Pin,'Pout':Pout,'Ppump':Ppump,'dUdt':dU,'closure':closure,
        'relative_closure':closure/scale,'U_start':U[0],'U_end':U[-1],
        'steps':sol.t.size,'success':sol.success,'message':sol.message,
        't':t,'y':y,'ports':ports,'signals':(pin,pout,ppump,U)
    }

if __name__=='__main__':
    for me,mm,label in [(0,0,'pump_off'),(0.1,0,'C_only'),(0,0.1,'L_only'),(0.1,0.1,'both')]:
        c=Case(me=me,mm=mm)
        r=run(c)
        print(label, {k:r[k] for k in ['Pin','Pout','Ppump','dUdt','closure','relative_closure','steps','success']})

# --- Complex single-quasifrequency drive for Floquet wave-action test ---
def rhs_factory_complex(c:Case):
    N=c.N; Om=2*np.pi*c.fm; om=2*np.pi*c.f0
    kappa=2*np.pi*c.M/c.N; idx=np.arange(N)
    pc=kappa*idx; pl=kappa*(idx+0.5)+c.delta
    def rhs(t,y):
        q=y[:N]; ph=y[N:]
        C=c.C0*(1+c.me*np.cos(pc-Om*t)); L=c.L0*(1+c.mm*np.cos(pl-Om*t))
        v=q/C; i=ph/L
        Vs=c.Vsrc*np.exp(1j*om*t)
        isrc=(Vs-v[0])/c.Rs
        dq=np.empty(N,dtype=complex); dq[0]=isrc-i[0]; dq[1:]=i[:-1]-i[1:]
        vout=c.RL*i[-1]
        dph=np.empty(N,dtype=complex); dph[:-1]=v[:-1]-v[1:]; dph[-1]=v[-1]-vout
        return np.r_[dq,dph]
    return rhs

def complex_scattering(c:Case, settle_periods=8, points_per_pump=160, nmax=8, rtol=1e-9, atol=1e-12):
    T0=1/c.f0; tend=(settle_periods+1)*T0; rhs=rhs_factory_complex(c)
    sol=solve_ivp(rhs,(0,tend),np.zeros(2*c.N,dtype=complex),method='DOP853',rtol=rtol,atol=atol,
                  max_step=1/c.fm/points_per_pump,dense_output=True)
    # endpoint=False avoids double-counting periodic endpoint
    ns=int(round(T0*c.fm*points_per_pump))
    t=tend-T0 + np.arange(ns)*(T0/ns)
    y=sol.sol(t); N=c.N; Om=2*np.pi*c.fm; om=2*np.pi*c.f0
    kappa=2*np.pi*c.M/c.N; idx=np.arange(N)
    C=c.C0*(1+c.me*np.cos(idx[None,:]*kappa-Om*t[:,None]))
    L=c.L0*(1+c.mm*np.cos((idx[None,:]+0.5)*kappa+c.delta-Om*t[:,None]))
    q=y[:N,:].T; ph=y[N:,:].T; v=q/C; i=ph/L
    Vs=c.Vsrc*np.exp(1j*om*t); isrc=(Vs-v[:,0])/c.Rs
    aL=(v[:,0]+c.Rs*isrc)/2
    bL=(v[:,0]-c.Rs*isrc)/2
    bR=c.RL*i[:,-1]  # matched right load, outgoing voltage wave
    rows=[]
    Pin0=None
    for n in range(-nmax,nmax+1):
        wn=om+n*Om
        basis=np.exp(-1j*wn*t)
        a=np.mean(aL*basis); br=np.mean(bL*basis); bt=np.mean(bR*basis)
        Pa=abs(a)**2/(2*c.Rs); Pr=abs(br)**2/(2*c.Rs); Pt=abs(bt)**2/(2*c.RL)
        if n==0: Pin0=Pa
        rows.append((n,wn,a,br,bt,Pa,Pr,Pt))
    action_in=Pin0/om
    action_out=sum((r[6]+r[7])/r[1] for r in rows if abs(r[1])>0)
    energy_out=sum(r[6]+r[7] for r in rows)
    return {'rows':rows,'action_in':action_in,'action_out':action_out,
            'action_ratio':action_out/action_in,'energy_out':energy_out,'Pin_incident':Pin0,
            'steps':sol.t.size,'success':sol.success}
