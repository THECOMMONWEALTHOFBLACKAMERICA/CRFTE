# CRTFE-HCM — Open Technical Disclosure: Physics, Floquet Validation, and Constitutive-State Control

**Author:** Dorian Martin-Smith  
**Public disclosure date:** 10 September 2026  
**Project:** CRTFE-HCM / CRFTE  
**Original mathematical record:** Zenodo DOI [10.5281/zenodo.22681634](https://doi.org/10.5281/zenodo.22681634)  
**Status:** Open technical disclosure. Theoretical and numerical work; no claim of experimentally demonstrated nonreciprocal hardware.

## Abstract

CRTFE-HCM is a programmable electromagnetic-medium research program built around space-time modulation, effective constitutive-state estimation, and closed-loop control.

For traveling electric and magnetic constitutive modulations with relative phase \(\delta\), the weak-order effective magnetoelectric coupling is

\[
\boxed{
\tilde\xi_{\rm eff}(\delta)
=
\frac{m_e m_m}{2}
\frac{u}{1-u^2}
\cos\delta
}
\]

with

\[
u=\frac{\Omega}{Kc_m}.
\]

The relationship has been checked against the general homogenization framework and against a discrete harmonic-balance/Floquet transmission-line model. In the intended weak-modulation, moderate-\(u\), long-wavelength regime, the cosine law survives. A practical discrete implementation also exhibits finite-frequency Floquet corrections that decrease approximately as \((f_0/f_m)^2\) as the probe is moved deeper into the homogenized regime.

This document also discloses the intended CRTFE-HCM constitutive-state control architecture: directional propagation and impedance observables are used to estimate the effective electromagnetic state, commands are constrained to the physically reachable constitutive manifold, and actuation is withheld when the requested state is unidentifiable, unreachable, or ill-conditioned.

---

## 1. Prior-art boundary

The underlying ideas of space-time modulation, synthetic Fresnel drag, bianisotropy, and using relative electric/magnetic modulation phase to tune nonreciprocity are prior art.

Relevant foundations include Huidobro et al. (PNAS, 2019) and Silveirinha & Huidobro (Physical Review Applied, 2021). The latter explicitly treats the relative phase between electric and magnetic space-time modulations as a tuning parameter for nonreciprocity and giant bianisotropy.

Accordingly, this disclosure does **not** claim invention of relative E/M phase control as a general concept.

The Martin-Smith contribution recorded here is narrower and engineering-focused:

- explicit weak-order \(\cos\delta\) parametrization in the CRTFE-HCM formulation;
- fixed-depth zero-crossing and sign-reversal experiment;
- signed directional propagation retrieval;
- finite-frequency Floquet falsification and scaling tests;
- multi-observable effective constitutive-state identification;
- reachable-manifold inverse control;
- identifiability and conditioning gates; and
- explicit refusal/withholding of actuation when the requested electromagnetic state cannot be reliably identified or physically realized.

---

## 2. Traveling constitutive modulation

Let

\[
\epsilon(x,t)
=
\epsilon_m\left[1+m_e\cos(Kx-\Omega t)\right]
\]

and

\[
\mu(x,t)
=
\mu_m\left[1+m_m\cos(Kx-\Omega t+\delta)\right].
\]

Here:

- \(m_e\) is electric-channel modulation depth;
- \(m_m\) is magnetic-channel modulation depth;
- \(K\) is modulation spatial wavenumber;
- \(\Omega\) is modulation angular frequency;
- \(\delta\) is physical relative E/M modulation phase;
- \(c_m\) is the unmodulated wave velocity.

Define

\[
u=\frac{\Omega}{Kc_m}.
\]

Expanding the general homogenized laboratory-frame expression to second order in modulation depth gives

\[
\boxed{
\tilde\xi_{\rm eff}
=
\frac{m_em_m}{2}
\frac{u}{1-u^2}
\cos\delta
+O(m^3)
}
\]

with

\[
\tilde\xi=c_m\xi_{\rm eff}.
\]

At this order there is no continuum magnetoelectric term proportional only to \(m_e^2\) or only to \(m_m^2\).

The phase-dependent contribution therefore predicts

\[
\delta=0\Rightarrow +\tilde\xi_{\max},
\]

\[
\delta=\frac{\pi}{2}\Rightarrow0,
\]

\[
\delta=\pi\Rightarrow-\tilde\xi_{\max}.
\]

The key experimental feature is that the zero crossing occurs while both modulation channels remain active at fixed nonzero depth.

---

## 3. Exact homogenization beyond weak order

The full homogenized equations were evaluated numerically without truncating the response at second order.

For \(m_e=m_m=0.10\), representative results are:

| \(u\) | Exact / weak amplitude | Departure from cosine |
|---:|---:|---:|
| 0.10 | 1.0000 | 0.00002% |
| 0.30 | 1.0000 | 0.0017% |
| 0.45 | 1.0003 | 0.0114% |
| 0.60 | 1.0016 | 0.0565% |
| 0.70 | 1.0048 | 0.167% |
| 0.80 | 1.0172 | 0.599% |
| 0.85 | 1.0405 | 1.39% |
| 0.90 | 1.1640 | 5.50% |

The weak-order cosine law is therefore extremely accurate around the intended first-test region \(u\approx0.3-0.5\). Higher-order harmonics become increasingly important as \(u\to1\).

The exact continuum model also gives, to numerical precision,

\[
\boxed{\tilde\xi_{\rm C-only}=0}
\]

and

\[
\boxed{\tilde\xi_{\rm L-only}=0}.
\]

---

## 4. Discrete Floquet transmission-line test

A time-periodic lumped \(L/C\) ladder was modeled using harmonic-balance sidebands and a Floquet transfer matrix.

For a representative 48-cell case,

- \(N=48\),
- \(M=4\),
- \(f_0=500\) kHz,
- \(f_m=3\) MHz,
- \(L_0=625\) nH,
- \(C_0=250\) pF,
- \(m_e=m_m=0.10\),

one obtains approximately

\[
\boxed{
\tilde\xi_{\rm ladder}(\delta)
=
0.0030078\cos(\delta-15^\circ)-0.0001305.
}
\]

The departure from a cosine fit is about 0.012% of the fundamental amplitude at this operating point.

The listed component values imply \(u\approx0.45\), not 0.50.

---

## 5. Geometric phase calibration

A discrete ladder has the shunt capacitor and series inductor at different physical positions.

For a capacitor at \(x=nd\) and a series inductor centered at \(x=(n+1/2)d\), the half-cell displacement contributes

\[
\delta_{\rm geom}=\frac{Kd}{2}.
\]

With \(M\) modulation periods over \(N\) cells,

\[
\boxed{
\delta_{\rm geom}=\frac{\pi M}{N}.
}
\]

For \(M=4,N=48\),

\[
\boxed{\delta_{\rm geom}=15^\circ.}
\]

The numerical model independently retrieves essentially this same offset.

The continuum equation is therefore written in terms of the **physical** relative phase. A practical controller must calibrate commanded electrical phase to the actual relative phase at the element locations.

---

## 6. Finite-frequency Floquet correction

An initial nonzero same-channel residual was tested by refining the ladder from \(N=12\) to \(N=384\) while keeping the physical medium fixed.

The residual did not disappear merely by increasing spatial resolution, so it is not primarily a finite-cell spatial-discretization artifact.

The controlling variable is instead

\[
r=\frac{f_0}{f_m}.
\]

At fine spatial discretization, the C-only residual behaves approximately as:

| \(f_0/f_m\) | C-only residual \(\tilde\xi\) |
|---:|---:|
| 0.1667 | \(-6.50\times10^{-5}\) |
| 0.10 | \(-2.22\times10^{-5}\) |
| 0.05 | \(-5.44\times10^{-6}\) |
| 0.0333 | \(-2.41\times10^{-6}\) |
| 0.020 | \(-8.66\times10^{-7}\) |
| 0.010 | \(-2.16\times10^{-7}\) |
| 0.005 | \(-5.41\times10^{-8}\) |

The low-frequency scaling is approximately

\[
\boxed{
|\tilde\xi_{\rm residual}|
\propto
\left(\frac{f_0}{f_m}\right)^2.
}
\]

The L-only case follows essentially the same scaling.

Thus the single-channel directional bias in the practical ladder is interpreted as a **finite-frequency Floquet correction**. It vanishes as the probe is moved deeper into the homogenized limit \(\omega/\Omega\to0\).

---

## 7. Practical experimental fit

A real experiment should use

\[
\boxed{
\tilde\xi_{\rm measured}(\delta)
=
A\cos(\delta-\delta_0)+B.
}
\]

Here:

- \(A\) is the desired phase-dependent cross-channel coupling;
- \(\delta_0\) captures geometric, cable, driver, and calibration phase;
- \(B\) captures higher-order continuum effects, finite-frequency Floquet bias, and static hardware asymmetry.

The phase-dependent null is therefore defined by

\[
\delta-\delta_0=\frac{\pi}{2}
\]

rather than by blindly assuming a commanded 90-degree setting.

---

## 8. Signed directional retrieval

For the reduced effective dispersion

\[
(k-\xi\omega)^2
=
\epsilon_{\rm eff}\mu_{\rm eff}\omega^2,
\]

signed forward and reverse propagation constants satisfy

\[
k_+=\xi\omega+n\omega,
\]

\[
k_-=\xi\omega-n\omega.
\]

Therefore

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

The sign of \(k_-\) must be preserved. Using \(|k_-|\) destroys the separation between the nonreciprocal shift and the effective refractive contribution.

Signed \(k_\pm\) alone do not uniquely determine the complete constitutive state. CRTFE-HCM therefore uses additional directional observables, including Bloch impedance where available.

A representative effective-state estimate is

\[
\boxed{
\hat x=
(\hat\epsilon,\hat\mu,\hat\xi,\hat\sigma).
}
\]

The full inversion may use

\[
(k_+,k_-,Z_B^+,Z_B^-)
\]

and multi-frequency attenuation information, subject to the identifiability of the chosen constitutive model.

---

## 9. CRTFE-HCM constitutive-state servo

The actuator space is not assumed to span an arbitrary box in \((\epsilon,\mu,\xi,\sigma)\).

Instead, the reachable electromagnetic state is treated as a manifold generated by the physical actuator variables:

\[
\boxed{
x=h(q)}
\]

where, for example,

\[
q=(m_e,m_m,\delta,\psi,\Delta G,u,\ldots).
\]

A requested constitutive state \(x_{\rm target}\) is converted to an actuator command through constrained inverse control:

\[
\boxed{
q^*
=
\arg\min_{q\in\mathcal U}
\left\|W[h(q)-x_{\rm target}]\right\|^2.
}
\]

Locally, a damped least-squares update may be written

\[
\boxed{
\Delta q
=
(J^T WJ+\lambda I)^{-1}J^TWe
}
\]

with

\[
J=\frac{\partial h}{\partial q},
\qquad
e=x_{\rm target}-\hat x.
\]

The controller therefore operates on the physically reachable constitutive manifold rather than silently forcing impossible parameter combinations.

---

## 10. Identifiability, reachability, and refusal

The controller should not issue a constitutive-state command merely because an optimizer returns a number.

Before actuation, the measurement inversion must be sufficiently identifiable and the actuator map sufficiently well conditioned.

Representative gates are

\[
\sigma_{\min}(G)>\tau_G
\]

for the measurement/identification problem and

\[
\sigma_{\min}(J)>\tau_J
\]

for the local actuator-to-state map.

If the requested state is not identifiable, not reachable, or lies in a region where the inverse becomes unacceptably ill-conditioned, CRTFE-HCM can explicitly

\[
\boxed{\text{REFUSE OR WITHHOLD ACTUATION}.}
\]

This is a deliberate design feature rather than an optimizer failure mode.

Where permitted, the system may instead compute a projection onto the reachable set:

\[
\boxed{
x_{\rm attainable}=\operatorname{Proj}_{\mathcal M}(x_{\rm target}).}
\]

The distinction between requested state, identifiable state, and physically realizable state is preserved in the control record.

---

## 11. Optional loss / dissipative channel

A later CRTFE-HCM embodiment can include an independently controlled dissipative or gain/loss channel with its own relative phase variable \(\psi\).

The purpose is not merely to add another tunable element, but to enlarge and shape the reachable constitutive manifold and permit control of attenuation/non-Hermitian response alongside electric, magnetic, and magnetoelectric behavior.

This channel remains subject to the same identifiability and reachability requirements as the E and M channels.

---

## 12. V1 experimental operating point

The earlier 500-kHz probe with a 3-MHz pump gives

\[
\frac{f_0}{f_m}\approx0.167.
\]

The numerical falsification pass indicates a cleaner first experiment is obtained by reducing the probe frequency to approximately

\[
\boxed{
f_0\approx100\text{–}150\ \mathrm{kHz}
}
\]

while retaining the 3-MHz pump.

This places

\[
\frac{f_0}{f_m}\approx0.033\text{–}0.05,
\]

reducing same-channel Floquet background by roughly one to two orders of magnitude relative to the earlier 500-kHz choice.

The goal of V1 is therefore maximum interpretability rather than maximum signal amplitude.

---

## 13. Falsification protocol

The first experimental campaign should include at least the following nulls and reversals:

1. **Pump off** — the phase-dependent signal must disappear.
2. **C-only modulation** — apparent coupling must approach zero as \(f_0/f_m\to0\).
3. **L-only modulation** — same requirement.
4. **Traveling-wave reversal** — \(K\to-K\) must reverse the phase-dependent contribution.
5. **Full phase sweep** — the response should fit \(A\cos(\delta-\delta_0)+B\) in the intended regime.
6. **Probe-frequency sweep** — same-channel residual should decrease approximately as \((f_0/f_m)^2\).
7. **Phase calibration** — commanded and physical E/M phase must be distinguished.
8. **Signed propagation retrieval** — the sign of \(k_-\) must be preserved.
9. **Identifiability gate** — constitutive estimates must be rejected when the inverse problem is rank-deficient or ill-conditioned.
10. **Reachability gate** — target constitutive states outside the reachable manifold must not be silently commanded.

Failure of these tests is evidence against the proposed interpretation or against the suitability of the tested operating point.

---

## 14. RF application path

A practical commercialization/research branch of CRTFE-HCM is an adaptive magnet-free nonreciprocal RF front end.

The intended progression is:

\[
\text{phase-controlled programmable medium}
\rightarrow
\text{measured nonreciprocal state}
\rightarrow
\text{adaptive isolation}
\rightarrow
\text{STAR / radar / EW front end}.
\]

A compelling demonstration would deliberately detune or load the medium, observe degradation of isolation, estimate the changed constitutive state, and automatically recover the desired nonreciprocal operating point through the constitutive-state servo.

This remains a proposed application. No such hardware demonstration is claimed here.

---

## 15. Research philosophy

The present CRTFE-HCM workflow is deliberately falsification-oriented:

1. make a quantitative prediction;
2. implement it in a model that contains more physical detail;
3. search for deviations and null-test failures;
4. identify whether discrepancies arise from physics, approximation limits, geometry, finite-frequency behavior, or implementation;
5. change the experiment accordingly.

The finite-frequency residual is an example of this process. An apparent same-channel violation was not discarded as noise; it was isolated and shown numerically to decrease approximately quadratically with probe-to-pump frequency ratio.

---

## 16. Current conclusion

Within its stated weak-modulation, moderate-\(u\), long-wavelength regime, the central relation

\[
\boxed{
\tilde\xi_{\rm eff}(\delta)
=
\frac{m_em_m}{2}
\frac{u}{1-u^2}
\cos\delta
}
\]

survives the current analytical and numerical falsification pass.

The next step is physical experimental validation.

The broader CRTFE-HCM architecture disclosed here treats the electromagnetic medium as a controlled constitutive system rather than as a fixed component: measure the directional state, estimate the effective constitutive state, determine what states are identifiable and reachable, solve the constrained inverse-control problem, and refuse commands that the physical medium cannot reliably realize.

That architecture is now intentionally placed in the public research record.

---

## References

1. P. A. Huidobro, E. Galiffi, S. Guenneau, R. V. Craster, and J. B. Pendry, “Fresnel drag in space-time-modulated metamaterials,” *Proceedings of the National Academy of Sciences* 116, 24943–24948 (2019).
2. M. G. Silveirinha and P. A. Huidobro, “Homogenization Theory of Space-Time Metamaterials,” *Physical Review Applied* 16, 014044 (2021).
3. D. Martin-Smith, “Continuous Relative-Phase Control of Synthetic Magnetoelectric Coupling in Space-Time Modulated Transmission Media,” Zenodo (2026), DOI: 10.5281/zenodo.22681634.

---

**Evidence boundary:** This document reports theoretical derivation, numerical homogenization, and harmonic-balance/Floquet modeling. It does not claim experimental validation, a working RF circulator, propulsion, lift, or flight hardware.