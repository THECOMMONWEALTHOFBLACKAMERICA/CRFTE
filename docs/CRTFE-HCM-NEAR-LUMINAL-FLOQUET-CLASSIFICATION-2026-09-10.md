# CRTFE-HCM — Near-Luminal Floquet Classification and Anti-Phase Bifurcation

**Date:** 10 September 2026  
**Status:** Mathematical and numerical result for the ideal nondispersive continuum/Floquet model. No hardware-performance claim.

## Executive result

The near-luminal regime is not described by continuing the weak Dorian Phase Relation through its apparent `1/(1-u^2)` divergence.

For equal-depth modulation, the exact comoving singular region is phase dependent. The anti-phase case

\[
m_e=m_m=m,\qquad \delta=\pi
\]

has an analytically clean Floquet bifurcation because first-order refractive-index modulation cancels while first-order impedance modulation is maximal.

Outside the narrow exact singular layer around `u=1`:

- **subluminal `u<1`:** the adjacent forward/backward crossing produces a spatial stop-band pair `k = k_c ± i κ`;
- **superluminal `u>1`:** the corresponding crossing mixes opposite-sign-frequency Floquet branches and produces a temporal parametric-instability pair `ω = ω_c ± i γ`.

To leading order in `m`,

\[
\boxed{\frac{\kappa}{K}=\frac{m}{4}\sqrt{1-u^2},\qquad u<1}
\]

and

\[
\boxed{\frac{\gamma}{Kc_m}=\frac{m}{4}\sqrt{u^2-1},\qquad u>1.}
\]

Equivalently,

\[
\boxed{\frac{\gamma}{\Omega}=\frac{m}{4u}\sqrt{u^2-1}.}
\]

Direct Floquet calculations converge toward these square-root laws outside the singular layer.

## Exact singular layer

For

\[
\epsilon_r=1+m_e\cos\theta,\qquad \mu_r=1+m_m\cos(\theta+\delta),
\]

the comoving constitutive denominator is

\[
D(\theta)=1-u^2\epsilon_r(\theta)\mu_r(\theta).
\]

Ordinary homogenized constitutive parameters develop a phase pole when `D(θ)=0`.

For equal depths, define

\[
c_\delta=\left|\cos\frac{\delta}{2}\right|.
\]

Then

\[
u_- = \frac{1}{1+mc_\delta}
\]

and

\[
u_+=
\begin{cases}
1/(1-mc_\delta), & c_\delta\ge m,\\
1/\sqrt{(1-m^2)(1-c_\delta^2)}, & c_\delta<m.
\end{cases}
\]

At anti-phase,

\[
\epsilon_r\mu_r=1-m^2\cos^2\theta,
\]

so the broad `O(m)` luminal interval collapses to

\[
\boxed{1\le u\le \frac{1}{\sqrt{1-m^2}}.}
\]

For `m=0.10`,

\[
\boxed{1\le u\le1.005037815.}
\]

No ordinary effective-parameter continuation or low-order two-mode claim is made inside this interval.

## Why anti-phase is special

To first order,

\[
\frac{\delta n}{n_0}=\frac12[m_e\cos\theta+m_m\cos(\theta+\delta)]
\]

and

\[
\frac{\delta Z}{Z_0}=\frac12[m_m\cos(\theta+\delta)-m_e\cos\theta].
\]

Define

\[
N=m_e+m_me^{i\delta},\qquad Z=m_me^{i\delta}-m_e.
\]

For equal-depth anti-phase modulation,

\[
N=0,\qquad Z=-2m.
\]

Thus first-order co-propagating/index modulation is canceled while contra-propagating impedance coupling remains. This makes the adjacent forward/backward Floquet crossing an isolated leading-order problem away from the exact pole layer.

## Unmodulated crossing geometry

The unmodulated replicas are

\[
\omega_{n,+}=c_m(k+nK)-n\Omega,
\]

\[
\omega_{n,-}=-c_m(k+nK)-n\Omega,
\]

with

\[
u=\Omega/(Kc_m).
\]

For `u<1`, the low-positive-frequency crossing is between forward `n=+1` and backward `n=0`:

\[
\boxed{\omega_c=\frac{1-u}{2}Kc_m,\qquad k_c=\frac{u-1}{2}K.}
\]

For `u>1`, the low-positive-quasifrequency crossing is between forward `n=-1` and backward `n=0`:

\[
\boxed{\omega_c=\frac{u-1}{2}Kc_m,\qquad k_c=\frac{1-u}{2}K.}
\]

Above `u=1`, the two harmonics at the crossing have opposite laboratory-frequency sign, giving the temporal-instability branch.

## Two-mode reduction

For anti-phase equal-depth modulation, the first-order projected coupling magnitude is `m/2`.

At fixed real frequency below `u=1`,

\[
(\delta k)^2+\frac{m^2}{4c_m^2}\omega_{+1}\omega_0=0,
\]

which gives

\[
\boxed{\kappa=\frac{mK}{4}\sqrt{1-u^2}.}
\]

At fixed real `k` above `u=1`, the frequency perturbation obeys

\[
(\delta\omega)^2=\frac{m^2}{4}\omega_{-1}\omega_0,
\]

and since the frequency product is negative,

\[
\boxed{\gamma=\frac{mKc_m}{4}\sqrt{u^2-1}.}
\]

This is the spatial-to-temporal near-luminal bifurcation.

## Numerical verification at m=0.10, delta=pi

### Subluminal spatial gap

| u | two-mode κ/K | direct Floquet κ/K | relative error |
|---:|---:|---:|---:|
| 0.800 | 0.015000000 | 0.014990716 | -0.062% |
| 0.850 | 0.013169567 | 0.013157157 | -0.094% |
| 0.900 | 0.010897247 | 0.010879909 | -0.159% |
| 0.920 | 0.009797959 | 0.009777602 | -0.208% |
| 0.940 | 0.008529361 | 0.008504736 | -0.289% |
| 0.950 | 0.007806247 | 0.007778670 | -0.353% |
| 0.960 | 0.007000000 | 0.006968521 | -0.450% |
| 0.980 | 0.004974937 | 0.004929041 | -0.923% |
| 0.990 | 0.003526684 | 0.003462789 | -1.812% |
| 0.995 | 0.002496873 | 0.002412966 | -3.360% |

The reported complex-`k` pair is converged across high harmonic orders at these points. Agreement deteriorates as `u→1−`, as expected when the isolated-crossing approximation approaches the singular/multiharmonic layer.

### Superluminal temporal instability

| u | two-mode γ/Ω | direct Floquet γ/Ω | relative error |
|---:|---:|---:|---:|
| 1.010 | 0.003509269 | 0.003044921 | -13.232% |
| 1.020 | 0.004926410 | 0.004689905 | -4.801% |
| 1.050 | 0.007622767 | 0.007509282 | -1.489% |
| 1.100 | 0.010414945 | 0.010356543 | -0.561% |
| 1.150 | 0.012345453 | 0.012312376 | -0.268% |
| 1.200 | 0.013819270 | 0.013802033 | -0.125% |

At `u=1.05, 1.10, 1.15, 1.20`, the complex-frequency pair is essentially invariant across `H=5/7` through `H=17` at displayed precision. More harmonics are required near `u=1.01–1.02`, consistent with proximity to the singular layer.

## Phase dependence

For general equal-depth phase,

\[
|Z|=2m\left|\sin\frac{\delta}{2}\right|.
\]

An isolated crossing would suggest

\[
\frac{\kappa}{K}\approx\frac{|Z|}{8}\sqrt{1-u^2},
\]

\[
\frac{\gamma}{Kc_m}\approx\frac{|Z|}{8}\sqrt{u^2-1}.
\]

This is **not** a universal near-luminal law. When `N=m(1+e^{iδ})` is nonzero, co-propagating Floquet replicas also couple and strongly modify the simple two-mode result near the broader phase-dependent pole interval.

Selected converged slices show:

- `δ=0°`: `Z=0`; no converged carrier-connected complex-`k` or complex-`ω` pair in the sampled slices. The matched case instead exhibits luminal characteristic locking/compression and spectral degeneracy.
- `δ=90°`: the two-mode approximation is strongly modified close to its broad pole window; a converged temporal complex pair appears farther into the superluminal region.
- `δ=135°`: the two-mode approximation is closer and converged temporal instability appears above the narrower pole window.
- `δ=180°`: the square-root law is exceptionally clean because the first-order index channel vanishes.

## Correction to the earlier characteristic interpretation

The in-phase matched characteristic equations possess local compression/locking rates inside their horizon interval. Those local rates should **not** automatically be identified with a complex Bloch quasifrequency.

After rejecting harmonic-edge truncation modes, the direct Floquet eigenproblem did not produce a converged carrier-connected complex-`ω` branch for the equal-depth in-phase slices tested here.

Therefore:

\[
\boxed{\text{characteristic compression/locking is not by itself a demonstrated temporal modal instability.}}
\]

## Revised near-luminal classification

1. **Outer weak-order region:** Dorian Phase Relation remains the appropriate constitutive descriptor.
2. **Pre-luminal multiband crossover:** forward Floquet spacing collapses and single-band homogenization loses uniform validity.
3. **Phase-dependent pole layer:** `1-u² ε_r μ_r=0` for some modulation phase; ordinary constitutive homogenization fails.
4. **Anti-phase subluminal branch:** outside the pole layer, an analytically predictable spatial stop band occurs at the adjacent forward/backward crossing.
5. **Anti-phase superluminal branch:** outside the pole layer, the same crossing becomes a converged temporal parametric instability with square-root growth.
6. **General phase:** index-like and impedance-like couplings coexist; a full multiband spectral map is required rather than a universal two-mode law.

## Evidence boundary

This result is theoretical and numerical. It does **not** demonstrate experimental RF gain, hardware stability/instability, insertion loss, isolation, a near-luminal device operating point, or a universal instability law in lossy/dispersive media.

The anti-phase square-root formulas are leading-order isolated-crossing results verified against the direct ideal Floquet model outside the singular layer. The exact pole layer remains unresolved as a fully converged multiharmonic spectral problem.
