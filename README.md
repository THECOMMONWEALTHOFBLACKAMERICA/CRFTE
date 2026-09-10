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
\tilde\xi(\delta)=\frac{m_em_m}{2}\frac{u}{1-u^2}\cos\delta.
\]

The current attribution boundary recognizes that relative E/M modulation phase as a nonreciprocity tuning parameter is prior art; the Martin-Smith public record focuses on the explicit engineering reduction, fixed-depth falsification protocol, signed-propagation retrieval, finite-frequency validation, and constitutive-control architecture.

- [CRTFE-HCM Continuous-Phase Mathematical Note — Dorian Martin-Smith, 9 September 2026](docs/CRTFE-HCM-CONTINUOUS-PHASE-MATHEMATICAL-NOTE-2026-09-09.md)
- **Zenodo DOI:** [10.5281/zenodo.22681634](https://doi.org/10.5281/zenodo.22681634)

### Open technical disclosure

As of 10 September 2026, CRTFE-HCM is being developed as an openly documented research program rather than held back for a planned patent filing. The public technical disclosure includes the analytical/Floquet validation, signed directional retrieval, multi-observable constitutive-state estimation, reachable-manifold inverse control, identifiability/conditioning gates, refusal behavior, V1 operating guidance, and the adaptive magnet-free RF-front-end application path.

See: [CRTFE-HCM — Open Technical Disclosure: Physics, Floquet Validation, and Constitutive-State Control](docs/CRTFE-HCM-OPEN-TECHNICAL-DISCLOSURE-2026-09-10.md).

### Energy and wave-action falsification gate

A terminated finite-ladder calculation has now been used to test explicit modulation-pump work and Floquet wave-action conservation independently of the earlier bulk propagation retrieval.

At the representative V1 point (`N=48`, `M=4`, `m_e=m_m=0.10`, `f_m=3 MHz`, `f_0=150 kHz`, 50-ohm terminations), the direct time-domain energy balance closes to a relative residual of approximately `5.75e-11` after settling. A single-input action-flux calculation gives an outgoing/incoming action ratio of approximately `0.999999965`, and a central multi-input photon-flux-normalized Gram test converges toward the expected pseudounitary relation as output-sideband coverage and numerical resolution are increased.

A follow-up convergence study separates the previously coupled numerical variables. At fixed dynamics, the energy-closure residual falls by approximately fourfold for each doubling of final quadrature samples, consistent with second-order trapezoidal convergence. At fixed settling, the ODE solution is effectively converged by about 60 points per pump period under the stated tolerances. Settling is separately measured by state periodicity rather than by the conservation residual itself.

The same work also records an important limitation: the existing near-luminal transfer-matrix branch tracker does **not** yet produce a stable H-converged gap width or attenuation interval. No near-luminal directional bandgap is claimed.

- [Finite-Ladder Energy and Wave-Action Falsification Gate](docs/CRTFE-HCM-ENERGY-WAVE-ACTION-GATE-2026-09-10.md)
- [Separated Energy-Gate Convergence Addendum](docs/CRTFE-HCM-ENERGY-CONVERGENCE-ADDENDUM-2026-09-10.md)
- [Near-Luminal H-Convergence Warning](docs/CRTFE-HCM-NEAR-LUMINAL-H-CONVERGENCE-WARNING-2026-09-10.md)
- [Energy-gate script](analysis/crtfe_hcm_energy_gate.py)
- [Separated convergence script](analysis/crtfe_hcm_energy_convergence.py)
- [Floquet scattering / action-flux Gram script](analysis/crtfe_hcm_floquet_smatrix_gate.py)
- [Energy and wave-action numerical results](data/CRTFE-HCM-energy-wave-action-gate-results-2026-09-10.csv)
- [Separated energy convergence data](data/CRTFE-HCM-energy-convergence-separated-2026-09-10.csv)
- [Near-luminal convergence data](data/CRTFE-HCM-near-luminal-H-convergence-2026-09-10.csv)

These remain numerical results. No experimental isolation, insertion-loss, efficiency, or gain claim is made.

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
