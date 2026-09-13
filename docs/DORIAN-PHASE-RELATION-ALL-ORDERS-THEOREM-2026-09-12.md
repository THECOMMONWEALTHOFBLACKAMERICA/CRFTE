# The Dorian Phase Relation — All-Orders Phase-Uniform Truncation Theorem

**Author:** Dorian Martin-Smith  
**Version:** 3.0.0  
**Date:** 12 September 2026  
**Program:** CRFTE / CRTFE-HCM  
**Reserved Zenodo DOI:** [10.5281/zenodo.22731518](https://doi.org/10.5281/zenodo.22731518)

## Abstract

This note advances the Dorian Phase Relation beyond its weak second-order form for the local sinusoidal space-time continuum

\[
E(\theta)=1+\eta a\cos\theta,\qquad
M(\theta)=1+\eta b\cos(\theta+\delta).
\]

On the phase-uniform regular subluminal branch

\[
0<u<\frac{1}{\sqrt{(1+a)(1+b)}},
\]

the exact homogenized magnetoelectric coefficient admits a positive first-return expansion with explicit modulation grading. The construction proves that odd total modulation orders vanish, the order-\(2N\) term contains phase harmonics only through \(\cos(N\delta)\), the phase-harmonic coefficients are nonnegative, and the maximum absolute remainder of every finite even-order truncation occurs at the in-phase condition \(\delta=0\).

## Exact matrix representation

Define

\[
\beta=\frac{u^2}{1-u^2},
\qquad
L(\theta)=
\begin{pmatrix}
1&\beta E(\theta)\\
M(\theta)&1+\beta
\end{pmatrix}.
\]

For the exact continuum averages \(J_0,J_E,J_M\),

\[
Q\equiv 1-u\tilde\xi
=
\frac{J_0}{J_0^2-u^2J_EJ_M}
=
\left[\left\langle L^{-1}\right\rangle^{-1}\right]_{11}.
\]

Fourier multiplication by \(L(\theta)\) gives a bi-infinite block-Toeplitz operator \(\mathcal L\). If \(P\) projects onto carrier harmonic \(n=0\) and \(\mathsf Q=I-P\), then

\[
P\mathcal L^{-1}P=\langle L^{-1}\rangle.
\]

On the phase-uniform branch, the majorant condition derived below gives \(\rho(T_{\rm abs})<1\). Since \(T_{\mathsf Q}\) is the carrier-excluded restriction of the same transition operator, its Neumann series converges at \(\eta=1\); hence \(I-T_{\mathsf Q}\) and \(\mathcal L_{\mathsf Q\mathsf Q}=\mathcal D_{\mathsf Q}(I-T_{\mathsf Q})\) are invertible throughout the stated branch. The convergence proof uses only the explicit transition blocks and their positive majorant, so this invocation is not circular.

The carrier Schur complement

\[
\mathcal S=
\mathcal L_{00}
-\mathcal L_{0\mathsf Q}
\mathcal L_{\mathsf Q\mathsf Q}^{-1}
\mathcal L_{\mathsf Q0}
\]

therefore satisfies

\[
\mathcal S=\langle L^{-1}\rangle^{-1},
\qquad
Q=\mathcal S_{11}.
\]

## Exact unequal-depth in-phase coefficient

At the physical grading point \(\eta=1\) and \(\delta=0\), let \(c=\cos\theta\) and keep \(a\) and \(b\) unequal. Then

\[
d(c)=\Delta-u^2(a+b)c-u^2ab c^2
=\Delta(1-\lambda_+c)(1-\lambda_-c),
\]

with

\[
\lambda_\pm=
\frac{u^2(a+b)\pm\sqrt{u^4(a+b)^2+4\Delta u^2ab}}{2\Delta}.
\]

Let

\[
G_\pm=(1-\lambda_\pm^2)^{-1/2},
\qquad
L_\lambda=\lambda_+-\lambda_-,
\]

and define

\[
J_0=
\frac{\lambda_+G_+-\lambda_-G_-}{\Delta L_\lambda},
\]

\[
I_1=
\frac{G_+-G_-}{\Delta L_\lambda},
\]

\[
I_2=
\frac{(G_+-1)/\lambda_+-(G_--1)/\lambda_-}{\Delta L_\lambda},
\]

with any apparent \(\lambda_\pm=0\) singularity interpreted by continuity. Set

\[
\mu_c=I_1/J_0,
\qquad
\sigma_c^2=I_2/J_0-\mu_c^2.
\]

Because \(E=1+ac\) and \(M=1+bc\) are affine in the same scalar \(c\),

\[
C_w=ab\sigma_c^2,
\]

and therefore

\[
\boxed{
\tilde\xi_0(a,b,u)=
\frac{uJ_0ab\sigma_c^2}{1+u^2J_0ab\sigma_c^2}
}.
\]

This removes the earlier abstract/content mismatch; the all-orders theorem itself does not require equal depths.

## Positive first-return lemma with explicit \(\eta\)-grading

After the fixed internal gauge \(\Gamma=\operatorname{diag}(1,-1)\), let

\[
D=
\begin{pmatrix}
1&-\beta\\
-1&1+\beta
\end{pmatrix}
\]

and

\[
T_+
=
\frac12
\begin{pmatrix}
\beta bq&\beta(1+\beta)a\\
bq&\beta a
\end{pmatrix},
\quad
T_-
=
\frac12
\begin{pmatrix}
\beta bq^{-1}&\beta(1+\beta)a\\
bq^{-1}&\beta a
\end{pmatrix},
\quad q=e^{i\delta}.
\]

Every physical modulation vertex carries one explicit factor of \(\eta\). Let \(T\) be the full nearest-neighbor transition operator and define

\[
T_{\mathsf Q}=\mathsf Q T\mathsf Q.
\]

Thus every interior factor \(T_{\mathsf Q}^n\) acts wholly inside the non-carrier subspace. Any intermediate visit to harmonic zero is projected out, so the Schur-complement series contains first-return paths by construction: the carrier appears only at the initial departure and final return.

With carrier/complement transition maps \(T_{0\mathsf Q},T_{\mathsf Q0},T_{\mathsf Q}\),

\[
\widetilde{\mathcal L}_{0\mathsf Q}=-\eta D T_{0\mathsf Q},
\]

\[
\widetilde{\mathcal L}_{\mathsf Q0}=-\eta\mathcal D_{\mathsf Q}T_{\mathsf Q0},
\]

and

\[
\widetilde{\mathcal L}_{\mathsf Q\mathsf Q}
=
\mathcal D_{\mathsf Q}(I-\eta T_{\mathsf Q}).
\]

Hence

\[
u\tilde\xi
=
\eta^2\ell^T
T_{0\mathsf Q}
(I-\eta T_{\mathsf Q})^{-1}
T_{\mathsf Q0}e_1,
\]

where

\[
e_1=(1,0)^T,\qquad \ell^T=(1,-\beta).
\]

The two external vertices give the explicit \(\eta^2\) factor. Expanding the complement resolvent,

\[
u\tilde\xi
=
\sum_{n=0}^{\infty}
\eta^{n+2}
\ell^T T_{0\mathsf Q}T_{\mathsf Q}^{n}T_{\mathsf Q0}e_1.
\]

A return path to harmonic zero must have even total length, so only \(n=2N-2\) contributes:

\[
\tilde\xi
=
\sum_{N=1}^{\infty}\eta^{2N}\tilde\xi^{(2N)}.
\]

The boundary factors are

\[
T_+e_1=\frac{bq}{2}(\beta,1)^T,\qquad
T_-e_1=\frac{bq^{-1}}{2}(\beta,1)^T,
\]

and

\[
\ell^TT_+=\ell^TT_-=(0,\beta a/2).
\]

After separating the Laurent phase winding, all coefficients in the departure, interior, and return factors are nonnegative for \(a,b,\beta>0\).

## Convergence

The absolute transition majorant is

\[
T_{\rm abs}=
\begin{pmatrix}
\beta b&\beta(1+\beta)a\\
b&\beta a
\end{pmatrix}.
\]

Its Perron radius is below one exactly when

\[
\beta(a+b+ab)<1,
\]

equivalent to

\[
u^2(1+a)(1+b)<1.
\]

The inequality is independent of \(\delta\); this is the precise sense in which the branch is **phase-uniform**. Thus the first-return expansion converges absolutely at the physical point \(\eta=1\) for every relative phase on the complete regular subluminal branch, and this convergence establishes the complement-block invertibility used above.

## All-orders harmonic structure

At total order \(2N\),

\[
\tilde\xi^{(2N)}(\delta)
=
\sum_{r=0}^{N}A_{N,r}\cos(r\delta),
\qquad A_{N,r}\ge0.
\]

Therefore, for

\[
\tilde\xi_{\le2N}=\sum_{n=1}^{N}\tilde\xi^{(2n)},
\]

the exact remainder obeys

\[
\boxed{
\max_\delta
\left|
\tilde\xi_{\rm exact}(\delta)-\tilde\xi_{\le2N}(\delta)
\right|
=
\tilde\xi_{\rm exact}(0)-\tilde\xi_{\le2N}(0)
}.
\]

This is the **all-orders phase-uniform truncation theorem for the stated local sinusoidal continuum model**.

## Scope

This theorem does **not** extend by itself to arbitrary or nonsinusoidal waveforms, finite staggered L/C ladders, lossy/dispersive/nonlinear/spatially nonlocal devices, near-luminal multiband regimes, finite-frequency discrete Floquet systems outside the continuum limit, or hardware.

The discrete ladder tomography/refinement studies in this repository are numerical supplements, not part of the theorem.

## Prior record

Earlier weak-order Dorian/CRTFE-HCM mathematical note: Zenodo DOI **10.5281/zenodo.22681634**.


## Supplementary phase-uniform validity maps

The theorem identifies \\(\\delta=0\\) as the exact worst-case phase for the absolute truncation remainder. Therefore the in-phase threshold tables below are conservative validity boundaries for **all** relative phases on the regular branch.

- [Equal-depth validity thresholds](../data/Dorian_validity_thresholds_v3.csv)
- [Unequal-depth validity thresholds](../data/Dorian_unequal_depth_validity_thresholds_v3.csv)
- [Validity-map interpretation and captions](DORIAN-PHASE-RELATION-VALIDITY-MAPS-v3.md)

These numerical maps quantify the usable domains of the \\(O(2)\\), \\(O(4)\\), and \\(O(6)\\) truncations; they do not enlarge the theorem's scope.


## Verification summary

The all-orders theorem has been cross-checked at four independent or structurally distinct points:

- the shortest two-step first-return paths reproduce the earlier weak-order Dorian relation exactly;
- the length-four first-return paths reproduce the independently derived general unequal-depth O(4) perturbation term, including the constant and cos(2 delta) content;
- the exact sparse rational recurrence audit through O(20) reports zero wrong-sign monomial coefficients at every audited order; this audit is supplementary and is not the theorem's logical basis;
- the unequal-depth numerical validity map is symmetric under exchange a <-> b to numerical precision, as required by the exact continuum equations.

The `worst_case_phase_deg = 0.0` values in the unequal-depth validity table are theorem-predicted worst-case phases, not outputs of an empirical phase scan.

See [publication QA markup](DORIAN-PHASE-RELATION-PUBLICATION-QA-v3.md) for the final OCR/extraction-artifact review.
