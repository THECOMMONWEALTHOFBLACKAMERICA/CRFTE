# CRTFE-HCM Continuous-Phase Mathematical Note

**Author:** Dorian Martin-Smith  
**Public disclosure date:** 9 September 2026  
**Zenodo DOI:** [10.5281/zenodo.22681634](https://doi.org/10.5281/zenodo.22681634)  
**Project:** CRTFE-HCM / CRFTE  
**Status:** Public technical note; proposed analytical extension to be experimentally tested. Not a patentability opinion and not a claim that the underlying space-time homogenization theory is new.

## Purpose

This note records a specific continuous-relative-temporal-phase extension of the weak-modulation homogenized magnetoelectric-coupling relation used in space-time-modulated media.

The underlying in-phase result, the requirement that both electric and magnetic constitutive channels be modulated, and the transmission-line space-time-modulation framework are prior art, including Huidobro et al. (PNAS, 2019) and Silveirinha & Huidobro (Physical Review Applied, 2021).

The specific point recorded here is the proposed continuous temporal offset \(\delta\) between electric and magnetic modulation channels that share the same spatial phase progression, with modulation depths and modulation velocity held fixed.

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

## 3. Martin-Smith continuous-temporal-phase extension

For two single-harmonic modulation channels separated by a relative temporal phase \(\delta\), the second-order electric-magnetic cross term is proportional to the real part of the product of the corresponding complex harmonic amplitudes:

\[
\operatorname{Re}\left[(m_e/2)(m_m/2)e^{i\delta}\right]
\propto m_em_m\cos\delta.
\]

Therefore the proposed weak-modulation continuous-phase extension is

\[
\boxed{
\tilde\xi(\delta)
=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta
}
\]

or, equivalently,

\[
\boxed{
\xi_{\rm eff}(\delta)
=\frac{1}{c_m}\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta.
}
\]

This expression predicts continuous control of the sign and magnitude of the effective magnetoelectric coupling while \(m_e\), \(m_m\), and \(u\) remain fixed.

## 4. Distinguishing operating points

The proposed relation predicts

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

The important distinction is that the zero crossing at \(\delta=\pi/2\) occurs with both modulation channels still active at their original nonzero depths. This differs from obtaining \(\xi_{\rm eff}=0\) by reducing either electric or magnetic modulation depth to zero.

## 5. Experimental signature

A practical measurement should allow for realized phase offset and static system asymmetry. The test model is therefore

\[
\boxed{
\tilde\xi_{\rm measured}(\delta)
=A\cos(\delta-\delta_0)+B
}
\]

where:

- \(A\) is the phase-dependent mechanism amplitude;
- \(\delta_0\) captures realized-versus-commanded phase offset;
- \(B\) captures phase-independent systematic or hardware asymmetry.

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

Within the weak-modulation, long-wavelength regime, the proposed extension predicts:

1. \(\tilde\xi(\delta)\) follows a cosine dependence at fixed \(m_e\), \(m_m\), and \(u\).
2. \(\tilde\xi\to0\) as either \(m_e\to0\) or \(m_m\to0\).
3. Reversing the traveling modulation direction, \(K\to-K\), reverses the sign of \(\tilde\xi\).
4. A continuous sweep of \(\delta\) carries \(\tilde\xi\) through zero without requiring either constitutive modulation channel to be shut off.

## 7. Validity limits

This note does not claim the expression is exact outside the perturbative homogenized regime. The intended regime is the same class of long-wavelength, weak-modulation conditions used in the underlying space-time homogenization literature, including \(\omega\ll\Omega\) and \(k\ll K\). The expression also should not be extrapolated through the \(u\to1\) singular region without full Floquet treatment.

## 8. Attribution and prior-art boundary

**Attributed here to Dorian Martin-Smith:** the public statement and derivation of the continuous temporal-phase engineering extension

\[
\tilde\xi(\delta)=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta
\]

for two nonzero electric and magnetic modulation channels sharing a common traveling spatial phase progression but separated by a continuously variable relative temporal phase \(\delta\), together with the proposed fixed-depth zero-crossing/sign-reversal experiment and the fitted experimental form \(A\cos(\delta-\delta_0)+B\).

**Not claimed as new here:** space-time modulation generally; effective Fresnel drag; the requirement to modulate both electric and magnetic channels; the in-phase weak-modulation coupling relation; lumped transmission-line implementations; or constitutive-parameter retrieval generally.

## References

1. P. A. Huidobro, E. Galiffi, S. Guenneau, R. V. Craster, and J. B. Pendry, “Fresnel drag in space-time-modulated metamaterials,” *PNAS* 116, 24943–24948 (2019).
2. M. G. Silveirinha and P. A. Huidobro, “Homogenization Theory of Space-Time Metamaterials,” *Physical Review Applied* 16, 014044 (2021).

## Citation

Martin-Smith, D. (2026). *Continuous Relative-Phase Control of Synthetic Magnetoelectric Coupling in Space-Time Modulated Transmission Media*. Zenodo. https://doi.org/10.5281/zenodo.22681634

---

This GitHub commit establishes a public timestamp for this technical note. The Zenodo DOI provides a persistent citable archival record. Neither record, by itself, is a legal determination of inventorship, patentability, validity, ownership, or freedom to operate.
