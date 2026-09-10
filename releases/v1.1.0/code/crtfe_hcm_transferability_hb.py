import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import spsolve


def conv_matrix(base, depth, phase, H):
    """Fourier convolution for x(t)=base*(1+depth*cos(phase-Omega t)).
    State convention y(t)=sum_h y_h exp(+i (w0+h Omega)t).
    Returns Q=Cconv @ V or Phi=Lconv @ I.
    """
    S=2*H+1
    M=np.eye(S,dtype=complex)*base
    for r in range(S):
        if r+1<S:
            M[r,r+1]+=base*(depth/2)*np.exp(1j*phase)
        if r-1>=0:
            M[r,r-1]+=base*(depth/2)*np.exp(-1j*phase)
    return M


def solve_device(N=48,L0=625e-9,C0=250e-12,me=.1,mm=.1,fm=3e6,r=.05,u=.45,
                 delta=0.0,H=4,ZL=50.0,ZR=50.0,side='L',Vs=1.0):
    f0=r*fm; Om=2*np.pi*fm; w0=2*np.pi*f0
    hs=np.arange(-H,H+1); S=len(hs); wh=w0+hs*Om
    kappa=Om*np.sqrt(L0*C0)/u
    pc=kappa*np.arange(N)
    pl=kappa*(np.arange(N)+0.5)+delta
    ns=2*N*S
    A=lil_matrix((ns,ns),dtype=complex)
    b=np.zeros(ns,dtype=complex)
    def vi(n,hidx): return n*S+hidx
    def ii(n,hidx): return N*S+n*S+hidx
    for n in range(N):
        C=conv_matrix(C0,me,pc[n],H)
        WC=(1j*wh[:,None])*C
        for hr in range(S):
            row=n*S+hr
            for hc in range(S):
                val=WC[hr,hc]
                if val!=0: A[row,vi(n,hc)] += val
            if n==0:
                A[row,vi(0,hr)] += 1/ZL
                A[row,ii(0,hr)] += 1
                if side=='L' and hs[hr]==0: b[row]+=Vs/ZL
            else:
                A[row,ii(n-1,hr)] += -1
                A[row,ii(n,hr)] += 1
    for n in range(N):
        L=conv_matrix(L0,mm,pl[n],H)
        WL=(1j*wh[:,None])*L
        for hr in range(S):
            row=N*S+n*S+hr
            for hc in range(S):
                val=WL[hr,hc]
                if val!=0: A[row,ii(n,hc)] += val
            A[row,vi(n,hr)] += -1
            if n<N-1:
                A[row,vi(n+1,hr)] += 1
            else:
                A[row,ii(n,hr)] += ZR
                if side=='R' and hs[hr]==0: b[row] += -Vs
    x=spsolve(csr_matrix(A),b)
    V=x[:N*S].reshape(N,S); I=x[N*S:].reshape(N,S)
    VsL=np.zeros(S,dtype=complex); VsR=np.zeros(S,dtype=complex)
    VsL[H]=Vs if side=='L' else 0
    VsR[H]=Vs if side=='R' else 0
    vL=V[0]
    iL=(VsL-vL)/ZL
    vR=VsR+ZR*I[-1]
    iR=(VsR-vR)/ZR
    aL=(vL+ZL*iL)/2; bL=(vL-ZL*iL)/2
    aR=(vR+ZR*iR)/2; bR=(vR-ZR*iR)/2
    ain=(aL if side=='L' else aR)[H]
    return {
        'hs':hs,'freqs':f0+hs*fm,'S_left':bL/ain,'S_right':bR/ain,
        'ain':ain,'V':V,'I':I,'kappa':kappa,'f0':f0
    }

if __name__=='__main__':
    for deg in [0,90,180,270]:
        L=solve_device(delta=np.deg2rad(deg),side='L',H=5)
        R=solve_device(delta=np.deg2rad(deg),side='R',H=5)
        h0=5
        S21=L['S_right'][h0]; S12=R['S_left'][h0]
        print(deg, S21, S12, np.angle(S21/S12))
