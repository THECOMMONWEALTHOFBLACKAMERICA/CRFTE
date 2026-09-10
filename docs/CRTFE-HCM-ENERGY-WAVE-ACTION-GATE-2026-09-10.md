# CRTFE-HCM — Finite-Ladder Energy and Wave-Action Consistency Checks

**Author:** Dorian Martin-Smith  
**Date:** 10 September 2026  
**Correction status:** Revised after adversarial review.  
**Status:** Public numerical consistency record; theoretical/numerical only. No experimental RF-performance claim.

## Correction notice

The original version of this document described the direct finite-ladder energy-balance calculation as a physics **falsification gate**. That characterization was too strong.

For the ideal time-varying L/C ladder written in charge/flux variables, the relation

\[
P_{\rm in}+P_{\rm pump}-P_{\rm out}-\frac{dU}{dt}=0
\]

follows algebraically from the model equations, KCL/KVL, and the chosen stored-energy definition. Therefore a small closure residual primarily tests the numerical implementation, integration, and quadrature. It is a useful simulator/unit-consistency check, but it is **not an independent falsification of the Dorian Phase Relation or of nonreciprocity**.

The Floquet wave-action / pseudounitary calculation is also retained as a numerical consistency check on the sideband representation. Pseudounitarity does not by itself establish passivity, bounded gain, stability, nonreciprocity, or the Dorian Phase Relation.

Actual direct falsification tests of the phase relation are now recorded separately in:

- [CRTFE-HCM — Direct Falsification Tests After Adversarial Review](CRTFE-HCM-DIRECT-FALSIFICATION-TESTS-2026-09-10.md)

## 1. Model and energy identity

The states are capacitor charge and inductor flux,

\[
q_n=C_n(t)V_n,
\qquad
\phi_n=L_n(t)I_n.
\]

For ideal time-varying reactive elements,

\[
U_C=\frac{q^2}{2C(t)},
\qquad
U_L=\frac{\phi^2}{2L(t)}.
\]

With the sign convention used here, modulation-pump power delivered to the electrical system is

\[
P_{\rm pump}(t)
=-\frac12\sum_n V_n^2\dot C_n
-\frac12\sum_n I_n^2\dot L_n.
\]

Differentiating the stored energy and substituting the ladder equations gives the exact model identity

\[
\boxed{
P_{\rm in}+P_{\rm pump}-P_{\rm out}-\frac{dU}{dt}=0.
}
\]

Accordingly, the numerical residual of this relation measures implementation and quadrature consistency rather than independently testing the underlying phase law.

## 2. Exact finite-ladder topology used in the published scripts

The canonical published model uses:

- `N = 48` shunt capacitors;
- `N = 48` series inductors;
- the final series inductor feeds the 50-ohm load;
- `M = 4` modulation periods over the 48-cell ladder;
- `L0 = 625 nH`;
- `C0 = 250 pF`;
- `m_e = m_m = 0.10`;
- `f_m = 3 MHz`;
- `f_0 = 150 kHz`;
- `Vsrc = 1.0 V`;
- 50-ohm source and load terminations;
- capacitor modulation phase indexed at cell positions `n`;
- inductor modulation phase referenced at physical midpoints `n + 1/2`;
- `delta = 0` for the principal numerical example.

The topology specification is stated explicitly because an independent adversarial reimplementation using 48 capacitors but only 47 inductors produced a different pump-power value. That difference reflects a different terminated ladder, not failure to reproduce the canonical published script.

## 3. Direct numerical consistency result

At the representative V1 point, the canonical model gives approximately:

| Quantity | Result |
|---|---:|
| Net input power into ladder | 2.499858208995 mW |
| Output/load power | 2.510502440065 mW |
| Pump work into electrical system | 10.644440885 uW |
| Mean stored-energy drift | 0.000209958 uW |
| Absolute closure residual | -1.443e-13 W |
| Relative closure residual | -5.75e-11 |

These numbers show that the code evaluates its own energy identity to high numerical precision. They should **not** be interpreted as independent evidence that the Dorian Phase Relation is physically correct.

The separate convergence addendum shows that the residual behaves as expected for numerical quadrature/integration error:

- [Separated Energy-Gate Convergence Addendum](CRTFE-HCM-ENERGY-CONVERGENCE-ADDENDUM-2026-09-10.md)

## 4. Pump-off and single-channel controls

Pump-off, C-only, L-only, and combined-channel cases were also evaluated.

The important conceptual distinction remains:

\[
\boxed{
\text{pump energy exchange} \neq \text{synthetic magnetoelectric coupling}.
}

Single-channel modulation can exchange real energy with the external modulation source while the homogenized same-channel magnetoelectric coupling tends to zero in the low-frequency limit.

These controls are useful for debugging and bookkeeping, but because the energy identity holds for arbitrary prescribed `C_n(t)` and `L_n(t)`, they are not direct tests of the Dorian Phase Relation.

## 5. Floquet sideband / wave-action consistency

A complex single-quasifrequency drive was used to extract positive- and negative-frequency Floquet sidebands separately.

For sideband frequencies

\[
\omega_n=\omega_0+n\Omega,
\]

an action-normalized finite scattering representation was tested against a pseudounitary metric of the form

\[
S_F^\dagger V S_F=V,
\]

where the sign of each sideband frequency is retained in the indefinite metric `V`.

For a single carrier input, the outgoing/incoming signed action ratio was approximately

\[
0.999999965.
\]

For a central multi-input set, the maximum Gram residual decreased as numerical resolution and output-sideband coverage were increased:

| Output range / setting | Maximum matrix-element residual | Frobenius residual |
|---|---:|---:|
| `n_out = +/-5`, settle 4, 40 points/pump | 2.45e-6 | 6.55e-6 |
| `n_out = +/-6`, settle 5, 50 points/pump | 1.26e-6 | 4.01e-6 |
| `n_out = +/-7`, settle 8, 60 points/pump | 8.97e-7 | 2.08e-6 |

This supports consistency of the implemented Floquet normalization and truncation trend. It does **not** certify passivity or stability: an indefinite-metric pseudounitary system can support parametric amplification.

## 6. Near-luminal regime remains unresolved

The existing transfer-matrix branch tracker does not produce a stable harmonic-order-converged gap width or attenuation interval near the luminal region.

Therefore no near-luminal directional bandgap, unidirectional branch, or physical divergence is claimed.

A better-conditioned scattering-matrix recursion or generalized-eigenvalue formulation is required before classifying that region.

## 7. Corrected evidence hierarchy

1. **Analytic weak-order derivation:** supports the CRTFE-HCM phase relation within its stated asymptotic regime.
2. **Direct terminated-device nonreciprocity phase sweep:** now tested separately and reported in the direct falsification record.
3. **Velocity functional form:** now tested against competing candidate functions over `u = 0.05` to `0.70`.
4. **Spatial and harmonic convergence:** finite-frequency residual survives the tested `N` and `H` controls in the intended V1 regime.
5. **Direct energy closure:** simulator/unit-consistency test only; not an independent physics falsifier.
6. **Floquet wave-action Gram relation:** sideband/scattering consistency check only; not a passivity, stability, or nonreciprocity certificate.
7. **Near-luminal regime:** unresolved.
8. **Hardware:** untested.

## References

- D. Globosits, J. Hupfl, and S. Rotter, *Pseudounitary Floquet scattering matrix for wave-front shaping in time-periodic photonic media*, Physical Review A **110**, 053515 (2024). DOI: 10.1103/PhysRevA.110.053515.
- M. G. Silveirinha and P. A. Huidobro, *Homogenization Theory of Space-Time Metamaterials*, Physical Review Applied **16**, 014044 (2021).
- P. A. Huidobro et al., *Fresnel drag in space-time-modulated metamaterials*, Proceedings of the National Academy of Sciences **116**, 24943 (2019).

## Reproducibility note

The canonical numerical scripts remain public. This correction preserves the numerical results while changing the evidentiary interpretation of the energy and wave-action checks. No hardware isolation, insertion loss, gain, efficiency, or experimental nonreciprocity claim is made.
