# CRTFE V-2 Hybrid MHD Research Baseline

> Revision P1 — 2026-08-24  
> Status: controlled preliminary research architecture. Not a fabrication drawing, flight release, or claim of demonstrated propulsion.

## Configuration decision

CRTFE V-2 is the next evidence-gated propulsion research architecture. The existing V5 aircraft remains the target vehicle and packaging reference; V-2 does not replace it.

The V-2 propulsion chain is:

1. externally conditioned or ionized atmospheric flow
2. conduction-cooled HTS static bias field
3. separately controlled segmented polyphase traveling-wave stator
4. finite-length MHD interaction channel
5. variable-area nozzle or diffuser/nozzle test section
6. external force stand and far-wake momentum closure
7. field-compatible protective enclosure

The traveling magnetic field is produced by time-varying stator currents. Displacement current is not the assumed traveling-wave mechanism at the intended MHD test frequencies.

## What V-2 borrows and what it must invent

| Subsystem | Existing technical precedent | V-2 engineering work |
|---|---|---|
| Static magnetic field | HTS magnet technology and conduction cooling | Field volume, current margin, cryogenic load, AC exposure, quench protection, mass and structural reaction path |
| Traveling field | Polyphase finite stators and traveling-wave MHD literature | Wavelength, phase progression, end winding, mutual coupling, installed-hardware losses and force direction |
| Conductive flow | Hot/seeded MHD and externally ionized-flow research | Measured `sigma(x,t)`, decay, Hall effects, total ionizer power, gas heating and flow uniformity for the selected regime |
| Flow-energy conversion | Compressible duct and nozzle physics | Coupled variable-area flow/body-force/heat model and measured pressure-to-momentum conversion |
| Protection | Aerospace containment, fire, impact and cryogenic practices | A shield that protects the module without becoming a conductive shorted turn or imposing unacceptable field loss |
| Vessel intelligence | Provenance-aware software, deterministic controls and safety monitors | ARC/T.A.R. integration with bounded authority, redundant power and independent safety enforcement |

## Evidence labels

Every project number or claim must be labeled as one of:

- `MEASURED`
- `DERIVED`
- `PREDICTED`
- `MODELED PLACEHOLDER`
- `UNVALIDATED`
- `HYPOTHESIS`
- `SPECULATIVE`
- `REFUTED`

Results from different pressure, temperature, ionization, seeding, plasma, geometry or time regimes may not be mixed without an explicit transfer model.

## Model and experiment gates

| Gate | Minimum pass evidence |
|---|---|
| G1 Conductivity | Repeatable spatial/temporal effective conductivity with uncertainty, decay, temperature and total ionizer power |
| G2 Electromagnetics | Staged G2A-G2E correlation of a mesh-converged finite-coil/circuit model with vector field, phase, impedance and power measurements |
| G3 Coupling | Measured force direction and magnitude follow phase-sequence and field-polarity reversals |
| G4 Nozzle | Measured pressure rise converts to exit/far-wake momentum within the uncertainty budget |
| G5 Net thrust | External stand force exceeds combined uncertainty and survives blanks, reversals and artifact controls |
| G6 Energy | Electrical input, heat, stored-energy change and fluid energy reconcile |
| G7 HTS | Field volume, thermal margin, cryogenic power, AC loss, mass and quench safety pass |
| G8 Protection | Structural, impact, fire, pressure, thermal and electromagnetic tests pass |
| G9 Replication | An independent laboratory reproduces the one-module result |
| G10 Synchronization | Two modules phase-lock without destructive electromagnetic, structural or control coupling |

No vehicle-scale or flight claim is permitted until one full module closes the external force and energy balances with traceable uncertainty.

## Immediate deliverables

1. Release the V-2A test plan and instrument uncertainty budget.
2. Complete G2A numerical verification and G2B bare-coil validation.
3. Measure `sigma(x,t)` and real auxiliary power in the selected non-flight test regime.
4. Extend the coupled 1-D model to variable area and test it against measured pressure and velocity data.
5. Freeze no magnet, shield, nozzle or vehicle allocation until the applicable gate passes.

## Controlled references

- [ASME Verification, Validation and Uncertainty Quantification](https://www.asme.org/codes-standards/publications-information/verification-validation-uncertainty)
- [CRTFE V5 target vehicle](TARGET-VEHICLE-V5.md)
- [V0.3 conductivity gate](V0.3-CONDUCTIVITY-GATE.md)
- [V-2 G2 electromagnetic validation](V2-G2-ELECTROMAGNETIC-VALIDATION.md)
- [ARC/Akashic vessel integration](ARC-AKASHIC-VESSEL-INTEGRATION.md)

