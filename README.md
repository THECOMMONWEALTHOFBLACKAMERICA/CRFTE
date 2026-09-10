# CRFTE / CRTFE Research Program

> **Current status — 10 September 2026:** early-stage research only. No working lift hardware or flight vehicle has been demonstrated.

## Current research priority

CRFTE began as the **Counter-Rotating Field Thrust Engine** concept and later evolved through atmospheric plasma / MHD propulsion studies.

The immediate research priority has now broadened beyond configuration-specific atmospheric-plasma conductivity inference toward a more general **programmable electromagnetic-medium / constitutive-control** research direction, referred to internally as **CRTFE-HCM**.

The pivot follows technical review of the earlier V0.3/P4E approach. The central issue is that a conductivity value inferred from one plasma-flow setup may not generalize because plasma state, geometry, flow evolution, energy-deposition method, sheath behavior, and temperature are strongly coupled. The new direction therefore emphasizes directly measured, reproducible electromagnetic-medium behavior rather than extrapolating from a single plasma configuration.

See: [CRTFE-HCM public research pivot](docs/CRTFE-HCM-PUBLIC-RESEARCH-PIVOT-2026-09-09.md).

### Public mathematical note

A dated public note records the weak-order continuous-relative-phase relation used in the current CRTFE-HCM analysis:

\[
\tilde\xi_D(\delta)=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta.
\]

Within the CRTFE-HCM publication record, this explicit weak-order engineering parametrization and its associated fixed-depth phase-sweep/falsification formulation are referred to as the **Dorian Phase Relation**.

The naming boundary is explicit: relative electric/magnetic modulation phase as a nonreciprocity tuning parameter, space-time modulation, synthetic magnetoelectric coupling generally, and the underlying homogenization framework are prior art. The name applies to the specific CRTFE-HCM parametrization and associated falsification framing recorded by Dorian Martin-Smith; it does not claim invention of the underlying prior-art theory.

- [CRTFE-HCM Continuous-Phase Mathematical Note — Dorian Martin-Smith, 9 September 2026](docs/CRTFE-HCM-CONTINUOUS-PHASE-MATHEMATICAL-NOTE-2026-09-09.md)
- **Zenodo DOI:** [10.5281/zenodo.22681634](https://doi.org/10.5281/zenodo.22681634)

### Open technical disclosure

As of 10 September 2026, CRTFE-HCM is being developed as an openly documented research program rather than held back for a planned patent filing. The public technical disclosure includes the analytical/Floquet validation, signed directional retrieval, multi-observable constitutive-state estimation, reachable-manifold inverse control, identifiability/conditioning gates, refusal behavior, V1 operating guidance, and the adaptive magnet-free RF-front-end application path.

See: [CRTFE-HCM — Open Technical Disclosure: Physics, Floquet Validation, and Constitutive-State Control](docs/CRTFE-HCM-OPEN-TECHNICAL-DISCLOSURE-2026-09-10.md).

### Direct falsification tests after adversarial review

An adversarial review correctly identified that the previously reported direct energy-balance closure is an algebraic identity of the ideal time-varying L/C ladder model. It is therefore a simulator/unit-consistency test rather than an independent falsification of the Dorian Phase Relation.

Two direct numerical tests that can actually fail the relation were then run.

**Terminated-device reciprocity test:** left- and right-incidence carrier transmission were independently extracted over a relative-phase sweep. The centered signed nonreciprocal phase `arg(S21/S12)` fits a cosine with approximately `0.0314%` relative RMS error. The phase reverses sign between `delta = 0 deg` and `180 deg` and falls near the small finite-frequency/background level around `90 deg` and `270 deg`.

**Velocity functional-form competition:** over `u = 0.05` to `0.70`, with `f0/fm = 0.02`, `N = 192`, `H = 4`, and `m_e = m_m = 0.10`, the extracted phase-law amplitudes strongly select `u/(1-u^2)` over `u`, `u/(1-u)`, and `u/(1-u^2)^(3/2)`. The best-fit coefficient is `0.005033`, close to the analytic weak-order coefficient `m_e m_m / 2 = 0.005`. With that analytic coefficient fixed rather than fitted, the mean absolute relative error is approximately `0.287%` and the worst pointwise error approximately `1.14%` across the tested range.

- [Direct Falsification Tests After Adversarial Review](docs/CRTFE-HCM-DIRECT-FALSIFICATION-TESTS-2026-09-10.md)
- [Direct S21/S12 phase-sweep data](data/CRTFE-HCM-direct-reciprocity-delta-test-2026-09-10.csv)
- [u-model selection data](data/CRTFE-HCM-u-model-selection-data-2026-09-10.csv)
- [u-model selection summary](data/CRTFE-HCM-u-model-selection-summary-2026-09-10.csv)

These remain numerical results. They do not validate hardware behavior, real material loss, fabrication tolerance, or the unresolved near-luminal multiband regime.

### Energy and wave-action consistency checks — corrected interpretation

The finite terminated-ladder energy and wave-action calculations remain useful, but their evidentiary role has been corrected.

The direct relation

\[
P_{\rm in}+P_{\rm pump}-P_{\rm out}-\frac{dU}{dt}=0
\]

is an algebraic identity of the ideal ladder model when `P_pump` and stored energy are defined from the same time-varying `C_n(t)` and `L_n(t)`. Its numerical closure therefore verifies simulator/integration consistency; it is **not** an independent physics falsification gate.

Likewise, the Floquet pseudounitary Gram calculation is retained as a sideband/scattering consistency check. Pseudounitarity does not by itself establish passivity, bounded gain, stability, nonreciprocity, or the Dorian Phase Relation.

The canonical ladder topology is now specified explicitly as 48 capacitors and 48 series inductors, with the final series inductor feeding the 50-ohm load. This resolves a topology ambiguity exposed by an independent adversarial reimplementation that used 48 capacitors but 47 inductors.

- [Corrected Finite-Ladder Energy and Wave-Action Consistency Record](docs/CRTFE-HCM-ENERGY-WAVE-ACTION-GATE-2026-09-10.md)
- [Separated Energy-Gate Convergence Addendum](docs/CRTFE-HCM-ENERGY-CONVERGENCE-ADDENDUM-2026-09-10.md)
- [Near-Luminal H-Convergence Warning](docs/CRTFE-HCM-NEAR-LUMINAL-H-CONVERGENCE-WARNING-2026-09-10.md)
- [Energy consistency script](analysis/crtfe_hcm_energy_gate.py)
- [Separated convergence script](analysis/crtfe_hcm_energy_convergence.py)
- [Floquet scattering / action-flux Gram script](analysis/crtfe_hcm_floquet_smatrix_gate.py)
- [Energy and wave-action numerical results](data/CRTFE-HCM-energy-wave-action-gate-results-2026-09-10.csv)
- [Separated energy convergence data](data/CRTFE-HCM-energy-convergence-separated-2026-09-10.csv)
- [Near-luminal convergence data](data/CRTFE-HCM-near-luminal-H-convergence-2026-09-10.csv)

### Current evidence boundary

The present public numerical record supports:

1. the analytic weak-order phase relation in its stated asymptotic regime;
2. direct terminated-device nonreciprocal phase behavior consistent with the `cos(delta)` law;
3. explicit functional-form selection of `u/(1-u^2)` over tested alternatives on `u = 0.05` to `0.70`;
4. spatial- and harmonic-convergence checks on the finite-frequency residual in the intended V1 regime.

The direct energy-balance and Floquet pseudounitary calculations are now classified as simulator/scattering consistency checks, not independent falsifiers of the phase relation.

The near-luminal multiband regime remains unresolved, and no hardware RF-performance claim has been demonstrated.

## Long-range aerospace objective

The long-range CRFTE objective remains research into large-area atmospheric electromagnetic momentum transfer without conventional rotors, propellers, turbines, or mechanical compressors.

That remains a research objective, not a claim of demonstrated propulsion.

## Program lineage

- **CRTFE-HCM:** current experimental-development priority; the core mathematical, validation, and constitutive-control architecture is now intentionally public.
- **P4 / P4E:** atmospheric electromagnetic propulsion branch retained as research and falsification history.
- **P4A / P4B / P4C / P4D:** earlier current-drive, magnetic-geometry, and plasma-conditioning studies retained for comparison and historical continuity.
- **Counter-rotating / traveling-field studies:** historical branches unless later evidence establishes a measurable advantage.

See: [CRFTE name and architecture lineage](docs/CRFTE-NAME-AND-ARCHITECTURE-LINEAGE.md).

## Evidence boundaries

CRFTE distinguishes among literature-supported mechanisms, calculations, simulations, proposed experiments, engineering drawings, and measured experimental results.

A simulation is not a test. A blueprint is not working hardware. A mathematically allowed operating region is not experimental validation.

## Public disclosure boundary

CRTFE-HCM's core constitutive-control architecture is now intentionally part of the public research record. Other CRFTE material that has not been deliberately released remains subject to the repository's existing disclosure controls.

See: [IP disclosure hold](IP-DISCLOSURE-HOLD.md).

## Related projects

- [Project links and ecosystem status](PROJECT-LINKS.md)
- [Commonwealth of Black America](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/Commonwealth-of-Black-America)
- [T.A.R.](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record)

This repository is the canonical public CRFTE / CRTFE research location.
