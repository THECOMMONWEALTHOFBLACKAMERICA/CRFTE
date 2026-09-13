import sympy as sp

beta,a,b,q = sp.symbols("beta a b q", positive=True)
Delta = 1/(1+beta)
u2 = beta/(1+beta)

L0 = sp.Matrix([[1,beta],[1,1+beta]])
Vp = sp.Matrix([[0,beta*a/2],[b*q/2,0]])
Vm = sp.Matrix([[0,beta*a/2],[b/(2*q),0]])

Gamma = sp.diag(1,-1)
D = sp.simplify(Gamma*L0*Gamma)
Wp = sp.simplify(Gamma*Vp*Gamma)
Wm = sp.simplify(Gamma*Vm*Gamma)

Tp = sp.simplify(-D.inv()*Wp)
Tm = sp.simplify(-D.inv()*Wm)

ell = sp.Matrix([[1,-beta]])
e1 = sp.Matrix([1,0])

assert sp.simplify(ell*Tp - sp.Matrix([[0,beta*a/2]])) == sp.zeros(1,2)
assert sp.simplify(ell*Tm - sp.Matrix([[0,beta*a/2]])) == sp.zeros(1,2)

assert sp.simplify(Tp*e1 - sp.Matrix([beta*b*q/2,b*q/2])) == sp.zeros(2,1)
assert sp.simplify(Tm*e1 - sp.Matrix([beta*b/(2*q),b/(2*q)])) == sp.zeros(2,1)

O2 = sp.factor((ell*(Tm*Tp + Tp*Tm)*e1)[0])
O2_expected = sp.factor(beta*a*b*(q + 1/q)/4)
assert sp.simplify(O2-O2_expected)==0

O4 = sp.factor((ell*(Tm*Tm*Tp*Tp + Tp*Tp*Tm*Tm)*e1)[0])

cos1 = (q+1/q)/2
cos2 = (q**2+q**-2)/2
O4_expected = sp.factor(
    a*b*beta**3*(a**2+b**2)*cos1/8
    + a**2*b**2*beta**2*((1+beta)+beta*cos2)/8
)
assert sp.simplify(O4-O4_expected)==0

Tabs = sp.simplify(Tp.subs(q,1)+Tm.subs(q,1))
det_majorant = sp.factor((sp.eye(2)-Tabs).det())
trace_majorant = sp.factor(sp.trace(Tabs))

assert sp.simplify(det_majorant - (1-beta*(a+b+a*b)))==0
assert sp.simplify(trace_majorant-beta*(a+b))==0

print("DORIAN POSITIVE FIRST-RETURN LEMMA CERTIFICATE")
print("==============================================")
print("D =", D)
print("T+ =", Tp)
print("T- =", Tm)
print("ell*T+ =", sp.simplify(ell*Tp))
print("ell*T- =", sp.simplify(ell*Tm))
print("T+*e1 =", sp.simplify(Tp*e1))
print("T-*e1 =", sp.simplify(Tm*e1))
print("O(2) =", O2)
print("O(4) =", O4)
print("det(I-Tabs) =", det_majorant)
print("trace(Tabs) =", trace_majorant)
print("CERTIFICATE: PASS")
