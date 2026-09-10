import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass

@dataclass
class Case:
    N:int=48; M:int=4
    L0:float=625e-9; C0:float=250e-12
    mm:float=.10; me:float=.10
    fm:float=3e6; f0:float=150e3
    delta:float=0.0; Rs:float=50.0; RL:float=50.0; Vsrc:float=1.0

def rhs_factory(c):
    N=c.N; Om=2*np.pi*c.fm; om=2*np.pi*c.f0
    kappa=2*np.pi*c.M/c.N; idx=np.arange(N)
    pc=kappa*idx; pl=kappa*(idx+.5)+c.delta
    def rhs(t,y):
        q=y[:N]; ph=y[N:]
        C=c.C0*(1+c.me*np.cos(pc-Om*t)); L=c.L0*(1+c.mm*np.cos(pl-Om*t))
        v=q/C; i=ph/L
        Vs=c.Vsrc*np.cos(om*t); isrc=(Vs-v[0])/c.Rs
        dq=np.empty(N); dq[0]=isrc-i[0]; dq[1:]=i[:-1]-i[1:]
        vout=c.RL*i[-1]
        dph=np.empty(N); dph[:-1]=v[:-1]-v[1:]; dph[-1]=v[-1]-vout
        return np.r_[dq,dph]
    return rhs

def diagnostics(c,t,y):
    N=c.N; Om=2*np.pi*c.fm; om=2*np.pi*c.f0
    kappa=2*np.pi*c.M/c.N; idx=np.arange(N)
    pc=kappa*idx; pl=kappa*(idx+.5)+c.delta
    ac=pc[None,:]-Om*t[:,None]; al=pl[None,:]-Om*t[:,None]
    C=c.C0*(1+c.me*np.cos(ac)); L=c.L0*(1+c.mm*np.cos(al))
    Cdot=c.C0*c.me*Om*np.sin(ac); Ldot=c.L0*c.mm*Om*np.sin(al)
    q=y[:N,:].T; ph=y[N:,:].T; v=q/C; i=ph/L
    Vs=c.Vsrc*np.cos(om*t); isrc=(Vs-v[:,0])/c.Rs; vout=c.RL*i[:,-1]
    pin=v[:,0]*isrc; pout=vout*i[:,-1]
    ppump=-.5*np.sum(v*v*Cdot,axis=1)-.5*np.sum(i*i*Ldot,axis=1)
    U=.5*np.sum(q*q/C,axis=1)+.5*np.sum(ph*ph/L,axis=1)
    return pin,pout,ppump,U

def solve(c, points_per_pump=80, max_settle=20):
    T0=1/c.f0; tend=(max_settle+1)*T0
    return solve_ivp(rhs_factory(c),(0,tend),np.zeros(2*c.N),method='DOP853',
        rtol=3e-10,atol=1e-12,max_step=1/c.fm/points_per_pump,dense_output=True)

def closure(c,sol,settle,eval_samples):
    T0=1/c.f0; t=np.linspace(settle*T0,(settle+1)*T0,eval_samples)
    y=sol.sol(t); pin,pout,ppump,U=diagnostics(c,t,y)
    avg=lambda x: np.trapezoid(x,t)/(t[-1]-t[0])
    Pin,Pout,Ppump=avg(pin),avg(pout),avg(ppump)
    dU=(U[-1]-U[0])/(t[-1]-t[0])
    r=Pin+Ppump-Pout-dU
    return r, r/max(abs(Pin),abs(Pout),abs(Ppump),1e-30)

def periodicity(c,sol,settle):
    T0=1/c.f0; a=sol.sol(settle*T0); b=sol.sol((settle+1)*T0)
    return np.linalg.norm(b-a)/max(np.linalg.norm(a),np.linalg.norm(b),1e-30)

if __name__=='__main__':
    c=Case()
    sol=solve(c,80,20)
    print('evaluation quadrature sweep')
    for ns in [501,1001,2001,4001,8001,16001,32001]:
        print(ns, closure(c,sol,10,ns))

    print('settling / periodicity sweep')
    for s in [1,2,4,6,8,10,12,14,16,18,20]:
        print(s, periodicity(c,sol,s), closure(c,sol,s,4001))

    print('ODE step-resolution sweep')
    for ppp in [10,15,20,30,40,60,80,120]:
        s=solve(c,ppp,10)
        print(ppp, closure(c,s,10,16001), s.t.size)
