# CRTFE-HCM — Finite-Ladder Energy and Wave-Action Falsification Gate

**Author:** Dorian Martin-Smith  
**Date:** 10 September 2026  
**Status:** Public numerical validation record; theoretical/numerical only. No experimental RF-performance claim.

## 1. Question being tested

The earlier CRTFE-HCM work established a bounded low/moderate-`u` effective-medium result for the phase-dependent synthetic magnetoelectric coupling,

\[
\tilde\xi(\delta)\approx \frac{m_e m_m}{2}\frac{u}{1-u^2}\cos\delta,
\]

and numerically separated a same-channel finite-frequency residual from spatial and Floquet-harmonic truncation effects in the intended V1 regime.

The next falsification gate is more fundamental:

> Does a terminated, finite, explicitly time-modulated L/C ladder obey the correct energy exchange with its modulation pump, and does its Floquet scattering behavior satisfy the expected wave-action conservation structure?

Until this gate is passed, quantitative gain, isolation, insertion-loss, or efficiency claims are not earned.

## 2. Independent time-domain model

The conservation test was implemented independently of the earlier bulk Floquet eigenvalue retrieval.

The states are capacitor charge and inductor flux,

\[
q_n=C_n(t)V_n,
\qquad
\phi_n=L_n(t)I_n.
\]

Using `q` and `phi` avoids hiding the time variation of the reactive elements inside an approximate impedance representation.

For an ideal time-varying capacitor,

\[
U_C=\frac{q^2}{2C(t)},
\]

and for an ideal time-varying inductor,

\[
U_L=\frac{\phi^2}{2L(t)}.
\]

Differentiating gives the modulation-work terms. With the convention used here, pump power delivered to the electrical system is

\[
\boxed{
P_{\rm pump}(t)
=-\frac12\sum_n V_n^2\dot C_n
-\frac12\sum_n I_n^2\dot L_n.
}
\]

The finite-device conservation identity is therefore

\[
\boxed{
P_{\rm in}+P_{\rm pump}-P_{\rm out}-\frac{dU}{dt}=0
}
\]

for the ideal lossless ladder. A dissipative implementation would add `P_loss` on the output side.

## 3. V1 test point

The principal test used:

- `N = 48` cells
- `M = 4` modulation periods
- `L0 = 625 nH`
- `C0 = 250 pF`
- `m_e = m_m = 0.10`
- `f_m = 3 MHz`
- `f_0 = 150 kHz`
- `f_0/f_m = 0.05`
- physical midpoint phase reference for the L channel
- `delta = 0`
- 50-ohm source and load terminations

This is intentionally in the bounded subluminal V1 region, away from the unresolved near-luminal multiband boundary.

## 4. Direct power closure

After ten carrier periods of settling and with 50 integration points per modulation period, the averaged result was:

| Quantity | Result |
|---|---:|
| Net input power into ladder | 2.499858208995 mW |
| Output/load power | 2.510502440065 mW |
| Pump work into electrical system | 10.644440885 uW |
| Mean stored-energy drift | 0.000209958 uW |
| Absolute closure residual | -1.443e-13 W |
| Relative closure residual | -5.75e-11 |

Thus the small excess of output power over net RF input is quantitatively supplied by the modulation pump. It is not energy created by the effective magnetoelectric term.

The closure error also decreases under tighter temporal resolution. Representative relative residuals were approximately:

- 20 points/pump period: `4.39e-8`
- 40 points/pump period: `1.98e-9`
- 80 points/pump period: `1.62e-9`
- longer-settled 50 points/pump run: `5.75e-11`

## 5. Null and phase controls

The same finite-ladder energy identity was checked with the pump disabled, C-only modulation, L-only modulation, and both channels active.

All cases closed at approximately `1e-9` to `1e-8` relative error or better in the shorter convergence runs.

Importantly, C-only and L-only modulation each exchange real energy with the pump even though the homogenized same-channel magnetoelectric coupling tends to zero in the low-frequency limit.

That distinction is important:

\[
\boxed{
\text{pump energy exchange} \neq \text{synthetic magnetoelectric coupling}.
}
\]

At the representative test point, approximate pump powers were:

| Modulation | Pump work |
|---|---:|
| pump off | 0 |
| C only | 3.366 uW |
| L only | 3.348 uW |
| C + L, delta=0 | 10.644 uW |

The power balance also closed for `delta = 0, 90, 180, 270 degrees`. Pump exchange itself varies with relative phase, as expected for a driven parametric system.

## 6. Sideband-resolved action-flux test

A second calculation used a complex single-quasifrequency incident wave so that positive- and negative-frequency Floquet channels could be tracked separately rather than being automatically paired by a real cosine drive.

For sideband frequencies

\[
\omega_n=\omega_0+n\Omega,
\]

wave-action conservation requires the sign of `omega_n` to be retained. In an action/photon-flux normalized basis the relevant finite Floquet scattering relation is of pseudounitary form,

\[
\boxed{
S_F^\dagger V S_F=V,
}
\]

where `V` assigns `+1` to positive-frequency channels and `-1` to negative-frequency channels.

For a single carrier input at the V1 point, the outgoing signed action sum divided by the incoming action converged to

\[
\boxed{0.999999965}
\]

after ten settling periods. Including output sidebands beyond approximately `|n|=3` changed the result negligibly at this modulation depth.

The dominant converted power appeared in the first upper and lower sidebands. The total outgoing energy exceeded the incident RF energy by approximately `10.644 uW`, matching the independently calculated modulation-pump work to about `1.8e-5` relative in that cross-method comparison.

## 7. Multi-input Floquet Gram test

A broader finite-scattering test was then constructed using both left and right incidence for input Floquet channels `n = -1, 0, +1`.

Outputs were retained on both ports over successively broader sideband sets and converted to an action-flux normalized basis using the sideband-frequency magnitude, while the metric retained the sign of each sideband frequency.

The maximum element of

\[
S^\dagger V_{\rm out} S-V_{\rm in}
\]

decreased as settling, temporal resolution, and output-sideband coverage were increased:

| Output range / numerical setting | Maximum matrix-element residual | Frobenius residual |
|---|---:|---:|
| `n_out = +/-5`, settle 4, 40 points/pump | 2.45e-6 | 6.55e-6 |
| `n_out = +/-6`, settle 5, 50 points/pump | 1.26e-6 | 4.01e-6 |
| `n_out = +/-7`, settle 8, 60 points/pump | 8.97e-7 | 2.08e-6 |

This is strong numerical evidence for the expected wave-action structure in the tested finite ladder.

It is **not** a proof of the infinite-dimensional Floquet scattering matrix. The reported Gram test covers a central set of incident channels and an explicitly truncated, converging set of outgoing channels.

## 8. Energy-gate conclusion

For the intended V1 operating regime, the energy gate does not expose a conservation inconsistency.

The direct time-domain calculation closes

\[
P_{\rm in}+P_{\rm pump}=P_{\rm out}+dU/dt
\]

to numerical precision, and the independent sideband-resolved calculation is consistent with Floquet wave-action/pseudounitary conservation.

Therefore:

\[
\boxed{
\text{The finite V1 numerical ladder passes the present energy-accounting falsification gate.}
}
\]

This result does **not** yet establish experimental efficiency, insertion loss, isolation, gain, or hardware performance.

## 9. Near-luminal classification remains open

After the energy gate closed, a secondary attempt was made to classify the high-`u` region using the existing transfer-matrix branch tracker and increasing Floquet harmonic order.

That test did **not** produce a converged gap width or stable attenuation interval. The apparent onset moved strongly with harmonic order, and high-order transfer matrices became increasingly difficult to classify robustly.

Therefore no near-luminal directional bandgap is claimed from this calculation.

The correct conclusion is:

\[
\boxed{
\text{near-luminal multiband behavior is unresolved by the present branch-tracking solver.}
}
\]

A better-conditioned generalized eigenvalue/scattering formulation is required before labeling the structure a physical stopband, directional gap, mode coalescence, or unidirectional branch.

## 10. Updated evidence hierarchy

1. **Low/moderate `u`:** phase law and bounded `u/(1-u^2)` effective-medium scaling are numerically supported.
2. **Finite-frequency same-channel residual:** survives spatial and Floquet-harmonic convergence in the intended V1 region and scales approximately as `(f0/fm)^2`.
3. **Finite-device energy accounting:** passes direct pump-to-field power closure at the tested V1 point and controls.
4. **Floquet wave action:** central multi-input action-flux Gram test converges toward the expected pseudounitary relation.
5. **Near-luminal regime:** not yet classified; no directional-gap claim is made.
6. **Hardware RF performance:** not experimentally demonstrated.

## References

- D. Globosits, J. Hupfl, and S. Rotter, *Pseudounitary Floquet scattering matrix for wave-front shaping in time-periodic photonic media*, Physical Review A **110**, 053515 (2024). DOI: 10.1103/PhysRevA.110.053515.
- M. G. Silveirinha and P. A. Huidobro, *Homogenization Theory of Space-Time Metamaterials*, Physical Review Applied **16**, 014044 (2021).
- P. A. Huidobro et al., *Fresnel drag in space-time-modulated metamaterials*, Proceedings of the National Academy of Sciences **116**, 24943 (2019).

## Reproducibility note

The numerical scripts used for the direct time-domain energy gate and the finite Floquet scattering Gram test are published with this record. All results remain numerical until reproduced independently and tested in hardware.
