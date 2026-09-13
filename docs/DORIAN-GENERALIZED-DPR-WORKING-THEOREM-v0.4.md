# Generalized Dorian Phase Relation — Referee-Ready Working Theorem v0.4

**Status:** working post-v3 theorem package.  
**Purpose:** close the specific gaps identified by the independent adversarial audit.  
**Not a replacement for:** the published v3.0.0 sinusoidal-continuum theorem.

---

## 1. Model and notation

Let

\[
E(\theta)
=
1+\eta\sum_{h\in S}a_h\cos(h\theta+\alpha_h),
\]

\[
M(\theta,\delta)
=
1+\eta\sum_{h\in S}b_h\cos[h(\theta+\delta)+\gamma_h],
\]

where \(S\subset\mathbb N\) is finite unless stated otherwise,
\(a_h,b_h\ge0\), and

\[
\beta=\frac{u^2}{1-u^2},
\qquad
\Delta=1-u^2.
\]

For the positive co-phased class set

\[
\alpha_h=\gamma_h=0.
\]

Define the active support

\[
S_*=\{h:\ a_h>0\text{ or }b_h>0\},
\qquad
H_*=\max S_*.
\]

For absolutely summable spectra define

\[
A=\sum_h a_h,\qquad B=\sum_h b_h.
\]

---

## 2. Exact laboratory-frame matrix identity — waveform independent

For any admissible profiles \(E(\theta),M(\theta)\), define

\[
d(\theta)=1-u^2E(\theta)M(\theta),
\]

\[
J_0=\left\langle\frac1d\right\rangle,
\quad
J_E=\left\langle\frac E d\right\rangle,
\quad
J_M=\left\langle\frac M d\right\rangle.
\]

The exact local-continuum coupling is

\[
\tilde\xi
=
\frac1u
\left(
1-\frac{J_0}{J_0^2-u^2J_EJ_M}
\right).
\]

Set

\[
Q=1-u\tilde\xi.
\]

Introduce

\[
L(\theta)=
\begin{pmatrix}
1&\beta E(\theta)\\
M(\theta)&1+\beta
\end{pmatrix}.
\]

Since

\[
\det L
=
\frac{d}{\Delta},
\]

one obtains pointwise

\[
L^{-1}
=
\begin{pmatrix}
\dfrac1d&-\dfrac{u^2E}{d}\\
-\dfrac{\Delta M}{d}&\dfrac{\Delta}{d}
\end{pmatrix}.
\]

Therefore

\[
\left\langle L^{-1}\right\rangle
=
\begin{pmatrix}
J_0&-u^2J_E\\
-\Delta J_M&\Delta J_0
\end{pmatrix},
\]

and hence

\[
\boxed{
Q=
\left[
\left\langle L^{-1}\right\rangle^{-1}
\right]_{11}.
}
\]

No single-harmonic assumption enters this identity.

---

## 3. Fourier carrier identity and Schur complement

Let

\[
\mathscr H=\ell^2(\mathbb Z)\otimes\mathbb C^2,
\]

and let \(\mathcal L\) be Fourier multiplication by \(L(\theta)\).
Let \(P\) project onto harmonic \(0\), and let

\[
\mathsf Q=I-P.
\]

Because Fourier conjugation turns multiplication by \(L^{-1}\) into
\(\mathcal L^{-1}\),

\[
\boxed{
P\mathcal L^{-1}P
=
\left\langle L^{-1}\right\rangle.
}
\]

Whenever \(\mathcal L_{\mathsf Q\mathsf Q}\) is invertible, the carrier
Schur complement

\[
\mathcal S
=
\mathcal L_{00}
-
\mathcal L_{0\mathsf Q}
\mathcal L_{\mathsf Q\mathsf Q}^{-1}
\mathcal L_{\mathsf Q0}
\]

satisfies

\[
P\mathcal L^{-1}P=\mathcal S^{-1}.
\]

Consequently,

\[
\boxed{
\mathcal S=\left\langle L^{-1}\right\rangle^{-1},
\qquad
Q=\mathcal S_{11}.
}
\]

This identifies the continuum homogenization coefficient with the
carrier self-energy before any path expansion is introduced.

On the envelope convergence disk introduced below, the carrier matrix element
computed from the weighted-\(\ell^1\) Neumann series agrees with the
\(\ell^2\) Schur-complement carrier matrix element, because the corresponding
first-return path series is absolutely convergent. Thus the two operator
realizations compute the same scalar carrier resolvent element.

---

## 4. Explicit derivation of the multi-harmonic transition kernel

The zero Fourier block is

\[
L_0=
\begin{pmatrix}
1&\beta\\
1&1+\beta
\end{pmatrix}.
\]

For harmonic \(+h\),

\[
V_{+h}
=
\frac12
\begin{pmatrix}
0&\beta a_he^{i\alpha_h}\\
b_he^{i\gamma_h}q^h&0
\end{pmatrix},
\qquad q=e^{i\delta},
\]

and \(V_{-h}\) is obtained by complex conjugating intrinsic phases and
sending \(q^h\to q^{-h}\).

Apply

\[
\Gamma=\operatorname{diag}(1,-1).
\]

Define

\[
D=\Gamma L_0\Gamma
=
\begin{pmatrix}
1&-\beta\\
-1&1+\beta
\end{pmatrix}.
\]

Its determinant is one, so

\[
D^{-1}
=
\begin{pmatrix}
1+\beta&\beta\\
1&1
\end{pmatrix}.
\]

Also

\[
W_{+h}
=
\Gamma V_{+h}\Gamma
=
-\frac12
\begin{pmatrix}
0&\beta a_he^{i\alpha_h}\\
b_he^{i\gamma_h}q^h&0
\end{pmatrix}.
\]

The transition block is **not** \(\Gamma V\Gamma\). It is

\[
\boxed{
T_{+h}=-D^{-1}W_{+h}.
}
\]

Multiplying explicitly gives

\[
\boxed{
T_{+h}
=
\frac12
\begin{pmatrix}
\beta b_he^{i\gamma_h}q^h&
\beta(1+\beta)a_he^{i\alpha_h}\\
b_he^{i\gamma_h}q^h&
\beta a_he^{i\alpha_h}
\end{pmatrix}.
}
\]

Likewise,

\[
\boxed{
T_{-h}
=
\frac12
\begin{pmatrix}
\beta b_he^{-i\gamma_h}q^{-h}&
\beta(1+\beta)a_he^{-i\alpha_h}\\
b_he^{-i\gamma_h}q^{-h}&
\beta a_he^{-i\alpha_h}
\end{pmatrix}.
}
\]

For the positive co-phased class, stripping the formal phase label
\(q^{\pm h}\) leaves only nonnegative coefficients.

With

\[
e_1=\binom10,
\qquad
\ell^T=e_1^TD=(1,-\beta),
\]

the external factors are

\[
T_{\pm h}e_1
=
\frac{b_he^{\pm i\gamma_h}q^{\pm h}}2
\binom{\beta}{1},
\]

and

\[
\boxed{
\ell^TT_{\pm h}
=
\left(
0,\frac{\beta a_he^{\pm i\alpha_h}}2
\right).
}
\]

Thus the negative component of \(\ell\) does not create a negative
scalar path coefficient in the positive co-phased class.

---

## 5. Exact carrier first-return identity

Let \(T\) be the harmonic-lattice transition operator whose allowed jumps
are \(\pm h\) for \(h\in S_*\). Partition it by carrier/complement:

\[
T=
\begin{pmatrix}
0&T_{0\mathsf Q}\\
T_{\mathsf Q0}&T_{\mathsf Q}
\end{pmatrix},
\qquad
T_{\mathsf Q}=\mathsf Q T\mathsf Q.
\]

The gauged Fourier operator factors as

\[
\widetilde{\mathcal L}_{00}=D,
\]

\[
\widetilde{\mathcal L}_{0\mathsf Q}
=
-\eta D T_{0\mathsf Q},
\]

\[
\widetilde{\mathcal L}_{\mathsf Q0}
=
-\eta \mathcal D_{\mathsf Q}T_{\mathsf Q0},
\]

\[
\widetilde{\mathcal L}_{\mathsf Q\mathsf Q}
=
\mathcal D_{\mathsf Q}(I-\eta T_{\mathsf Q}),
\]

where \(\mathcal D_{\mathsf Q}\) is block diagonal with block \(D\).

Hence, whenever the complement Neumann series converges,

\[
\widetilde{\mathcal S}
=
D
-
\eta^2
DT_{0\mathsf Q}
(I-\eta T_{\mathsf Q})^{-1}
T_{\mathsf Q0}.
\]

Because the fixed gauge leaves the carrier \((1,1)\) entry unchanged,

\[
Q
=
1-
\eta^2
\ell^TT_{0\mathsf Q}
(I-\eta T_{\mathsf Q})^{-1}
T_{\mathsf Q0}e_1.
\]

Since \(Q=1-u\tilde\xi\),

\[
\boxed{
u\tilde\xi
=
\eta^2
\ell^TT_{0\mathsf Q}
(I-\eta T_{\mathsf Q})^{-1}
T_{\mathsf Q0}e_1.
}
\]

This is the continuum-identification lemma missing from the earlier
audit package. The factors \(u,\eta^2,\ell,e_1\) follow directly from
the exact carrier Schur complement above, not from numerical fitting.

Because every intermediate factor is \(T_{\mathsf Q}=\mathsf QT\mathsf Q\),
an interior visit to harmonic zero is removed. The expansion is therefore
a **first-return** expansion, not an unrestricted carrier Green function.

---

## 6. Named Banach-space majorant and convergence

For arbitrary intrinsic phases, define the positive \(2\times2\)
absolute majorant

\[
T_{\rm abs}
=
\begin{pmatrix}
\beta B&\beta(1+\beta)A\\
B&\beta A
\end{pmatrix}.
\]

Let

\[
\rho=\rho(T_{\rm abs}).
\]

When

\[
\boxed{
u^2(1+A)(1+B)<1,
}
\]

one has

\[
\rho<1.
\]

For \(A>0\) and \(B>0\), choose a strictly positive left Perron vector
\(w^T\) satisfying

\[
w^TT_{\rm abs}=\rho w^T.
\]

If \(A=0\) or \(B=0\), one constitutive channel is unmodulated and the
cross-coupling vanishes identically, so the envelope claim is vacuous and
does not require a strictly positive Perron vector.

On

\[
X=\ell^1(\mathbb Z\setminus\{0\};\mathbb C^2)
\]

define the Perron-weighted norm

\[
\boxed{
\|x\|_w
=
\sum_{n\ne0}w^T|x_n|,
}
\]

where absolute value is componentwise.

The sum of the entrywise absolute transition blocks over all jumps is
bounded by \(T_{\rm abs}\). Therefore

\[
\boxed{
\|T_{\mathsf Q}x\|_w
\le
\rho\|x\|_w.
}
\]

Hence

\[
\|T_{\mathsf Q}\|_w\le\rho<1,
\]

and

\[
\boxed{
(I-\eta T_{\mathsf Q})^{-1}
=
\sum_{k=0}^{\infty}\eta^kT_{\mathsf Q}^k
}
\]

converges absolutely at \(\eta=1\).

Because

\[
\widetilde{\mathcal L}_{\mathsf Q\mathsf Q}
=
\mathcal D_{\mathsf Q}(I-\eta T_{\mathsf Q}),
\]

the same condition is sufficient for complement-block invertibility.
Moreover,

\[
d(\theta)
\ge
1-u^2(1+A)(1+B)>0
\]

on this disk, so the pointwise constitutive inverse and the averaged
carrier block are regular there.

This supplies the previously unnamed functional-analytic setting.

---

## 7. Positive-spectrum generalized DPR theorem

Assume finite support and

\[
\alpha_h=\gamma_h=0,
\qquad
a_h,b_h\ge0.
\]

At total modulation order \(n\),

\[
\boxed{
\tilde\xi^{(n)}(\delta)
=
\sum_{r=0}^{H_*\lfloor n/2\rfloor}
A_{n,r}\cos(r\delta),
\qquad
A_{n,r}\ge0.
}
\]

### Harmonic ceiling

For a closed length-\(n\) path, let its signed step lengths be
\(s_jh_j\), with

\[
\sum_{j=1}^{n}s_jh_j=0.
\]

If \(\mathcal M\) is the subset of steps/factors where the magnetic column is
selected, the phase exponent is

\[
r=\sum_{j\in\mathcal M}s_jh_j.
\]

Closure also gives

\[
r=-\sum_{j\notin\mathcal M}s_jh_j.
\]

Therefore

\[
|r|
\le
H_*
\min(|\mathcal M|,n-|\mathcal M|)
\le
\boxed{
H_*\left\lfloor\frac n2\right\rfloor.
}
\]

### Phase-uniform truncation theorem

For

\[
\tilde\xi_{\le N}
=
\sum_{n=2}^{N}\tilde\xi^{(n)},
\]

the absolutely convergent remainder is

\[
R_N(\delta)
=
\sum_{n>N}\sum_r A_{n,r}\cos(r\delta).
\]

Thus

\[
|R_N(\delta)|
\le
\sum_{n>N}\sum_r A_{n,r}
=
R_N(0),
\]

and therefore

\[
\boxed{
\max_\delta
\left|
\tilde\xi_{\rm exact}(\delta)-\tilde\xi_{\le N}(\delta)
\right|
=
\tilde\xi_{\rm exact}(0)-\tilde\xi_{\le N}(0).
}
\]

---

## 8. Exact odd-order onset criterion

Let \(S_*\) be the active support.

Order \(n\) can contribute only if there exists a signed zero-sum
relation

\[
\boxed{
\sum_{j=1}^{n}s_jh_j=0,
\qquad
s_j\in\{\pm1\},
\quad
h_j\in S_*.
}
\]

The first possible odd order is

\[
\boxed{
n_{\rm odd}^{\min}
=
\min\left\{
n\in2\mathbb N+1:
\exists\,s_j,h_j,\;
\sum_{j=1}^{n}s_jh_j=0
\right\}.
}
\]

Let

\[
g=\gcd S_*.
\]

Then all odd orders vanish **if and only if** every normalized index
\(h/g\) is odd.

For the converse, suppose the normalized support contains an even element
\(e\) and an odd element \(o\). Then the signed relation

\[
\underbrace{o+\cdots+o}_{e\ {\rm copies}}
-
\underbrace{e+\cdots+e}_{o\ {\rm copies}}
=0
\]

has odd total length \(e+o\). Ordering the \(e\) positive \(o\)-steps first
and the \(o\) negative \(e\)-steps afterward gives a first-return walk with
no interior visit to zero. When the corresponding active electric/magnetic
coefficients are positive, its path weight is positive. Hence mixed
normalized parity guarantees that at least one odd modulation order is
nonzero, although the first such order need not be \(O(3)\).

Example:

\[
S_*=\{1,4,6\}
\]

has

\[
O(3)=0,
\]

but the five-step relation

\[
4+4=6+1+1
\]

allows

\[
O(5)\ne0.
\]

---

## 9. Arbitrary-phase spectral-envelope theorem

Now allow arbitrary intrinsic phases \(\alpha_h,\gamma_h\).

Every phase factor in a path has modulus one. If \(w_{\rm path}\) is an
arbitrary-phase first-return path weight and \(w_{{\rm path},+}\) is the
corresponding phase-stripped positive-envelope weight, then

\[
\boxed{
|w_{\rm path}(\delta)|
=
w_{{\rm path},+}.
}
\]

Absolute convergence in the Perron-weighted \(\ell^1\) space permits
termwise triangle inequality:

\[
\begin{aligned}
|R_N(\delta)|
&=
\left|
\sum_{\rm tail}w_{\rm path}(\delta)
\right|\\
&\le
\sum_{\rm tail}|w_{\rm path}(\delta)|\\
&=
\sum_{\rm tail}w_{{\rm path},+}\\
&=
R_{N,+}(0).
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_\delta|R_N(\delta)|
\le
R_{N,+}(0).
}
\]

Likewise,

\[
\boxed{
\sup_\delta|\tilde\xi(\delta)|
\le
\tilde\xi_+(0).
}
\]

This is an inequality for arbitrary intrinsic Fourier phases, not an
equality theorem.

For finite support, the geometric ceiling survives independently of
positivity:

\[
|r|\le H_*\lfloor n/2\rfloor.
\]

The order-\(n\) response may therefore contain both sine and cosine
terms up to that ceiling.

---

## 10. Phase-origin covariance — corrected non-unique maximizers

Suppose

\[
\alpha_h=h\gamma_E,
\qquad
\gamma_h=h\gamma_M
\]

for all active harmonics.

The change of variable

\[
\theta'=\theta+\gamma_E
\]

reduces the problem exactly to the positive co-phased class with

\[
\delta_{\rm eff}
=
\delta+\gamma_M-\gamma_E.
\]

Hence

\[
\boxed{
\delta_0=\gamma_E-\gamma_M
}
\]

is **a maximizer** of the truncation remainder.

Let

\[
g=\gcd S_*.
\]

Because all active harmonics are multiples of \(g\), the response is
periodic in \(\delta\) with period

\[
\frac{2\pi}{g}.
\]

Thus the phases

\[
\boxed{
\delta_k
=
\gamma_E-\gamma_M+\frac{2\pi k}{g}
\pmod{2\pi}
}
\]

are all maximizers. The period \(2\pi/g\) is guaranteed but need not be the
primitive phase period when the electric and magnetic supports differ or
additional degeneracies are present.

The maximum value is

\[
\boxed{
\max_\delta|R_N(\delta)|
=
R_{N,+}(0).
}
\]

---

## 11. Full relation-lattice holonomy criterion

For finite active support \(S_*\), define the integer relation lattice

\[
\boxed{
\mathcal K
=
\left\{
m=(m_h)_{h\in S_*}\in\mathbb Z^{S_*}:
\sum_{h\in S_*}m_hh=0
\right\}.
}
\]

For electric phases define

\[
\Phi_E(m)
=
\sum_{h\in S_*}m_h\alpha_h
\pmod{2\pi},
\]

and analogously

\[
\Phi_M(m)
=
\sum_{h\in S_*}m_h\gamma_h
\pmod{2\pi}.
\]

Under a phase-origin shift

\[
\alpha_h\mapsto\alpha_h-h\chi,
\]

one has

\[
\Phi_E(m)\mapsto
\Phi_E(m)-\chi\sum_hm_hh
=
\Phi_E(m),
\]

so every relation-lattice holonomy is gauge invariant.

The phase assignment is **flat** precisely when

\[
\boxed{
\Phi_E(m)=0
\quad
\text{for every }m\in\mathcal K.
}
\]

This is equivalent to the existence of a phase origin \(\gamma_E\) such
that

\[
\boxed{
\alpha_h=h\gamma_E\pmod{2\pi}
\qquad(h\in S_*).
}
\]

Likewise for the magnetic phases.

Therefore

\[
\boxed{
\text{translation-positive spectrum}
\iff
\text{all integer-relation holonomies vanish}.
}
\]

Triangular quantities such as

\[
\alpha_h+\alpha_k-\alpha_{h+k}
\]

are useful when the required harmonics are present, but they are **not**
a complete criterion on sparse support.

For example, support

\[
S_*=\{1,4\}
\]

contains no in-support triangle, yet the relation

\[
4(1)-1(4)=0
\]

produces the gauge-invariant holonomy

\[
\boxed{
4\alpha_1-\alpha_4.
}
\]

Nonzero holonomy obstructs a global coefficientwise-positive gauge. It
does **not** imply that every finite-order remainder must attain its
maximum away from zero.

---

## 12. Publication-safe hierarchy

The corrected hierarchy is:

1. **Pure sinusoid:** published v3.0.0 theorem.
2. **Positive co-phased finite spectrum:** exact generalized positive
   first-return theorem with ceiling
   \(H_*\lfloor n/2\rfloor\), exact signed-relation parity criterion, and
   exact phase-uniform remainder equality.
3. **Phase-flat translated spectrum:** same equality after a phase-origin
   shift; maximizing phase need not be unique.
4. **Arbitrary intrinsic Fourier phases:** positive spectral-envelope
   inequality and full relation-lattice holonomy obstruction.

The arbitrary-phase layer is an **inequality-and-obstruction framework**,
not an equality theorem.

---

## 13. Remaining external-review boundary

The repaired package makes G1/G2/G5 self-contained, corrects G6/G7, and
incorporates the final copyedits requested by an independent adversarial
re-audit that returned an overall verdict of **A — theorem-ready**. It remains
a working extension until separately versioned and externally published.

No claim here extends to loss, constitutive dispersion, nonlocality,
finite staggered ladders, near-luminal multiband physics, or hardware.
