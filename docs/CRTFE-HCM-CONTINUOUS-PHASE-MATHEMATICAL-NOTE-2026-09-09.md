# CRTFE-HCM Continuous-Phase Mathematical Note

**Author:** Dorian Martin-Smith  
**Public disclosure date:** 9 September 2026  
**Naming revision:** 10 September 2026  
**Zenodo DOI:** [10.5281/zenodo.22681634](https://doi.org/10.5281/zenodo.22681634)  
**Project:** CRTFE-HCM / CRFTE  
**Status:** Public technical note; theoretical/numerical formulation to be experimentally tested. Not a patentability opinion and not a claim that the underlying space-time homogenization theory or relative electric/magnetic phase control is new.

## Purpose

This note records the explicit weak-modulation continuous-relative-phase engineering relation used in CRTFE-HCM for synthetic magnetoelectric coupling in a space-time-modulated medium.

The underlying in-phase result, space-time modulation of electric and magnetic constitutive channels, synthetic magnetoelectric coupling, and relative electric/magnetic modulation phase as a nonreciprocity tuning parameter are prior art, including Huidobro et al. (PNAS, 2019) and Silveirinha & Huidobro (Physical Review Applied, 2021).

Within the CRTFE-HCM research record, the explicit weak-order parametrization

\[
\tilde\xi_D(\delta)=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta
\]

and its associated fixed-depth phase-sweep/falsification formulation are referred to as the **Dorian Phase Relation**.

The name is an internal/public naming convention for this specific CRTFE-HCM formulation and does not assert invention of the underlying prior-art theory of relative E/M phase control.

## 1. Modulation definitions

Let

\[
\epsilon(x,t)=\epsilon_m\left[1+m_e\cos(Kx-\Omega t)\right]
\]

and

\[
\mu(x,t)=\mu_m\left[1+m_m\cos(Kx-\Omega t+\delta)\right].
\]

Here:

- \(m_e\) is the physical electric-channel modulation depth;
- \(m_m\) is the physical magnetic-channel modulation depth;
- \(K\) is the modulation spatial wavenumber;
- \(\Omega\) is the modulation angular frequency;
- \(\delta\) is a continuous relative temporal phase between the two channels.

Define

\[
u=\frac{\Omega}{Kc_m},
\]

where \(c_m\) is the wave velocity of the unmodulated effective medium.

## 2. Prior-art in-phase weak-modulation relation

Using the common convention

\[
\epsilon=\epsilon_m[1+2\alpha_e\cos\theta],\qquad
\mu=\mu_m[1+2\alpha_m\cos\theta],
\]

with physical modulation depths

\[
m_e=2\alpha_e,\qquad m_m=2\alpha_m,
\]

the in-phase weak-modulation homogenized magnetoelectric term can be written in normalized engineering form as

\[
\tilde\xi_{\delta=0}
=\frac{m_em_m}{2}\frac{u}{1-u^2},
\]

where

\[
\tilde\xi\equiv c_m\xi_{\rm eff}.
\]

This in-phase mechanism is prior art.

## 3. Dorian Phase Relation

For two single-harmonic electric and magnetic modulation channels separated by a physical relative temporal phase \(\delta\), the second-order electric-magnetic cross term carries the relative-phase dependence

\[
\operatorname{Re}\left[(m_e/2)(m_m/2)e^{i\delta}\right]
\propto m_em_m\cos\delta.
\]

The CRTFE-HCM weak-order engineering parametrization is therefore written as the **Dorian Phase Relation**:

\[
\boxed{
\tilde\xi_D(\delta)
=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta
}
\]

or, equivalently,

\[
\boxed{
\xi_{D,\rm eff}(\delta)
=\frac{1}{c_m}\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta.
}
\]

The subscript \(D\) is a naming label for the CRTFE-HCM formulation; it does not denote a distinct fundamental constitutive quantity from the effective magnetoelectric coupling \(\xi_{\rm eff}\).

The relation predicts continuous control of the sign and magnitude of the phase-dependent effective magnetoelectric coupling while \(m_e\), \(m_m\), and \(u\) remain fixed, within the bounded weak-modulation/homogenized regime where the approximation applies.

## 4. Distinguishing operating points

The Dorian Phase Relation predicts

\[
\delta=0 \Rightarrow +\tilde\xi_{\max},
\]

\[
\delta=\frac{\pi}{2} \Rightarrow 0,
\]

\[
\delta=\pi \Rightarrow -\tilde\xi_{\max},
\]

\[
\delta=\frac{3\pi}{2} \Rightarrow 0,
\]

and then return to the positive maximum at \(2\pi\).

The important experimental distinction is that the phase-dependent zero crossing at \(\delta=\pi/2\) occurs with both modulation channels still active at their original nonzero depths. This differs from obtaining \(\xi_{\rm eff}=0\) by reducing either electric or magnetic modulation depth to zero.

## 5. Experimental signature

A practical measurement should allow for realized phase offset, finite-frequency corrections, and static system asymmetry. The test model is therefore

\[
\boxed{
\tilde\xi_{\rm measured}(\delta)
=A\cos(\delta-\delta_0)+B
}
\]

where:

- \(A\) is the phase-dependent mechanism amplitude;
- \(\delta_0\) captures realized-versus-commanded phase offset;
- \(B\) captures phase-independent higher-order, finite-frequency, or hardware contributions.

Signed forward and reverse propagation constants must be retained. For the reduced effective dispersion

\[
(k-\xi\omega)^2=\epsilon_{\rm eff}\mu_{\rm eff}\omega^2,
\]

one has

\[
k_+=\xi\omega+n\omega,
\]

\[
k_-=\xi\omega-n\omega,
\]

and therefore

\[
\boxed{
\xi=\frac{k_++k_-}{2\omega}
}
\]

and

\[
\boxed{
n=\frac{k_+-k_-}{2\omega}.
}
\]

The sign of \(k_-\) must not be discarded.

## 6. Falsifiable predictions

Within the weak-modulation, long-wavelength, bounded subluminal regime, the Dorian Phase Relation predicts:

1. \(\tilde\xi(\delta)\) follows a cosine dependence at fixed \(m_e\), \(m_m\), and \(u\).
2. The second-order continuum cross-channel contribution vanishes as either \(m_e\to0\) or \(m_m\to0\).
3. Reversing the traveling modulation direction, \(K\to-K\), reverses the sign of the phase-dependent contribution.
4. A continuous sweep of \(\delta\) carries the phase-dependent contribution through zero without requiring either constitutive modulation channel to be shut off.
5. In the tested low/moderate-\(u\) regime, the amplitude follows the expected \(u/(1-u^2)\) scaling until the weak homogenized approximation begins to fail as the multiband/luminal region is approached.

## 7. Validity limits

The Dorian Phase Relation is not claimed to be exact outside the perturbative homogenized regime. The intended regime is the same class of long-wavelength, weak-modulation conditions used in the underlying space-time homogenization literature, including \(\omega\ll\Omega\) and \(k\ll K\).

Current CRTFE-HCM numerical validation supports the weak-order form over a bounded subluminal range, approximately through \(u\lesssim0.7\) for the modulation depths examined. This is a numerical operating bound for the tested model, not a universal theorem.

The apparent singularity at \(u=1\) is not presented as a demonstrated physical divergence. Near the luminal/multiband regime, weak homogenization loses validity and a converged full Floquet-band treatment is required. The present CRTFE-HCM record makes no near-luminal directional-bandgap or unidirectional-branch claim.

## 8. Naming, attribution, and prior-art boundary

**Dorian Phase Relation:** within CRTFE-HCM, the name refers specifically to the explicit weak-order engineering parametrization

\[
\tilde\xi_D(\delta)=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta,
\]

its fixed-depth continuous phase sweep, the zero-crossing/sign-reversal formulation, and the associated falsification protocol recorded by Dorian Martin-Smith.

**Not claimed as new here:** space-time modulation generally; effective Fresnel drag; synthetic magnetoelectric coupling generally; relative E/M modulation phase as a nonreciprocity tuning parameter; the in-phase weak-modulation coupling mechanism; lumped transmission-line space-time-modulation implementations; or constitutive-parameter retrieval generally.

The use of the name **Dorian Phase Relation** is a naming convention in the CRTFE-HCM publication record. Whether that terminology is adopted by other researchers is a matter of subsequent scientific usage and citation.

## 9. Current numerical evidence boundary

Subsequent CRTFE-HCM numerical work has stress-tested the relation and finite-device implementation beyond the original mathematical note. The public record now includes:

- phase-law validation;
- bounded subluminal \(u/(1-u^2)\) scaling checks;
- spatial and Floquet-harmonic convergence checks;
- identification of a finite-frequency same-channel residual scaling approximately as \((f_0/f_m)^2\) in the intended V1 regime;
- direct finite-device pump-to-field energy closure;
- sideband-resolved Floquet wave-action checks; and
- separated numerical convergence tests for ODE resolution, averaging quadrature, and settling.

These remain theoretical and numerical results. No experimental hardware isolation, insertion loss, efficiency, gain, or other RF performance claim is made.

## References

1. P. A. Huidobro, E. Galiffi, S. Guenneau, R. V. Craster, and J. B. Pendry, “Fresnel drag in space-time-modulated metamaterials,” *PNAS* 116, 24943–24948 (2019).
2. M. G. Silveirinha and P. A. Huidobro, “Homogenization Theory of Space-Time Metamaterials,” *Physical Review Applied* 16, 014044 (2021).

## Citation

Martin-Smith, D. (2026). *Continuous Relative-Phase Control of Synthetic Magnetoelectric Coupling in Space-Time Modulated Transmission Media*. Zenodo. https://doi.org/10.5281/zenodo.22681634

---

This GitHub revision establishes a public timestamp for the **Dorian Phase Relation** naming convention within the CRTFE-HCM technical record. The Zenodo DOI provides the persistent archival record associated with the underlying mathematical note. Neither record, by itself, is a legal determination of inventorship, patentability, validity, ownership, priority, or freedom to operate.
