# CRFTE / CRTFE Atmospheric Electromagnetic Propulsion Research

> **Current status:** theoretical / reduced-order research with a **grant-scale P4E proof-of-physics experiment now defined**. No working lift hardware or flight vehicle has been demonstrated.

## Project links

- [Website and ecosystem status](PROJECT-LINKS.md)
- [Commonwealth of Black America public record](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/Commonwealth-of-Black-America)
- [T.A.R. — The Akashic Records](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record)

This repository remains the canonical public CRTFE project location.

## Project goal — locked

CRTFE remains a **large-area, no-moving-parts atmospheric electromagnetic propulsion research program** with a two-person VTOL / wingborne aircraft as the long-range application.

The core objective is unchanged:

> **Transfer electromagnetic momentum directly into a large atmospheric-air mass flow without conventional rotors, propellers, turbines or mechanical compressors.**

See: [P4 Project Goal Lock](docs/PROJECT-GOAL-LOCK-P4.md).

## Current program structure

### P4 — vehicle-scale primary architecture

The goal-aligned architecture remains a full-stream Lorentz interaction using:

1. atmospheric air as the external working mass;
2. a strong stationary magnetic field;
3. controlled transient conductivity;
4. synchronized transverse current;
5. direct `J × B` body-force transfer;
6. segmentation / commutation rather than a required multi-tesla traveling propulsion field.

Reduced-order anchor:

```text
F = D σ_on E_drive B_static V
σ_eff = D σ_on
P_J = F² / (σ_eff B_static² V)
```

For the long-range 650 kg vehicle reference with `A = 4.8 m²`, `L = 0.5 m`, and `V = 2.4 m³`:

```text
hover thrust ≈ 6.38 kN
ideal hover induced velocity ≈ 23.3 m/s
ideal fluid-power floor ≈ 148.5 kW
```

These remain screening values, not demonstrated vehicle performance.

### P4A / P4B / P4C — current-drive refinement

The present current-drive research separates the large static propulsion field from a smaller pulsed field used only to establish current.

- **P4A:** asymmetric inductive current drive;
- **P4B:** bipolar `+B/-B` static pole geometry so opposite legs of a closed plasma-current loop contribute same-direction Lorentz force;
- **P4C:** coupled primary capacitor / transformer / plasma-loop circuit with active clamping before reverse impulse.

See:

- [P4A asymmetric inductive current drive](docs/P4A-ASYMMETRIC-INDUCTIVE-CURRENT-DRIVE.md)
- [P4A simulation correction](docs/P4A-SIMULATION-CORRECTION.md)
- [P4B bipolar static-pole inductive loop](docs/P4B-BIPOLAR-STATIC-POLE-INDUCTIVE-LOOP.md)
- [P4C coupled primary / plasma driver](docs/P4C-COUPLED-PRIMARY-PLASMA-DRIVER.md)

### P4D — high-PRF vibrational conductivity branch

Literature and reduced-order analysis shifted the plasma question away from a low-duty-cycle 3 kHz assumption and toward:

- tens to hundreds of kHz repetitive nanosecond excitation;
- plasma-memory effects;
- sub-breakdown RF vibrational conditioning;
- suppression of rapid oxygen attachment;
- explicit treatment of electron-ion recombination.

See [P4D High-PRF Vibrational Conductivity Research](docs/P4D-HIGH-PRF-VIBRATIONAL-CONDUCTIVITY-RESEARCH.md).

## P4E — current grant-scale experiment

The immediate funding target is **not a vehicle build**.

P4E asks a falsifiable laboratory question:

> **Does high-repetition-rate nanosecond ionization combined with sub-breakdown RF vibrational conditioning materially increase the conductivity-time integral and polarity-reversible Lorentz momentum transfer of low-temperature atmospheric air per electrical joule?**

The central screening experiment uses approximately:

```text
active interaction volume: ~50 cm^3
flowing atmospheric air
ns repetition rate: 40–100 kHz
RF conditioning: ON/OFF controlled comparison
magnetic field: ~1.5–2.0 T laboratory scale
independently characterized current drive
synchronized plasma / electrical / thermal diagnostics
mN-class force or equivalent momentum measurement
```

Primary go/no-go gates:

- `>=10x` increase in conductivity-time integral with RF conditioning at matched ns-pulse energy;
- bulk gas temperature rise `<150 K` in the controlled comparison;
- distributed conductivity `>=0.01 S/m` without arc-dominated operation;
- `>=3 mN` polarity-reversible force signal;
- measured force consistent with independently reconstructed `integral(J × B)dV` within experimental uncertainty;
- `>=5x` improvement in Lorentz impulse per plasma-conditioning joule versus the nanosecond-only baseline.

The reduced-order model predicts a conditioned test region in the **mN** range rather than requiring a vehicle-scale force demonstration. The experiment is designed to identify whether attachment, recombination, nonuniformity, thermal deposition or another loss mechanism prevents further scaling.

### Grant package

- [P4E submission package index](funding/P4E-SUBMISSION-PACKAGE.md)
- [P4E technical abstract](funding/P4E-GRANT-ABSTRACT.md)
- [P4E specific aims and milestones](funding/P4E-SPECIFIC-AIMS-AND-MILESTONES.md)
- [P4E budget and facilities template](funding/P4E-BUDGET-AND-FACILITIES-TEMPLATE.md)
- [P4E readiness checklist](funding/P4E-READINESS-CHECKLIST.md)
- [P4E grant-scale simulation](docs/P4E-GRANT-SCALE-SIMULATION.md)
- [P4E reproducible screening code](tools/p4e_grant_scale_kinetics_force.py)

**Technical package status:** ready for adaptation to a specific solicitation.  
**Actual submission still requires:** eligible submitting institution / PI, facilities confirmation, final sponsor-specific budget, required institutional forms and the target solicitation.

## Known experimental lineage

CRTFE does not claim that pulsed cold-air MHD or ns/RF hybrid plasma is new by itself.

Relevant prior work separately establishes:

- repetitive pulsed nonequilibrium plasma in air / nitrogen;
- measurable Lorentz-force effects on low-temperature high-speed flow;
- ns-pulse / RF hybrid vibrational excitation;
- negative-ion / metastable plasma memory;
- inductive and capacitive plasma-current coupling in adjacent MHD / plasma systems.

P4E is framed around the **combination and efficiency question**, with explicit control experiments and falsification gates.

No patent-novelty claim is made by this repository without a formal search.

## Vehicle target — future integration only

The long-range vehicle reference remains:

- crew: 2 side-by-side;
- design gross mass: ~650 kg;
- four distributed active modules;
- total active lift area: ~4.8 m²;
- VTOL / wingborne transition;
- no-moving-parts atmospheric electromagnetic propulsion as the research objective.

A **300–500 mph wingborne envelope** is now retained only as an aspirational design-study range for future aerodynamic and control simulation. It is not a demonstrated or funded P4E deliverable.

See:

- [Target Vehicle V5](docs/TARGET-VEHICLE-V5.md)
- [T.A.R. / A.R.C. autonomy integration](docs/TAR-ARC-AUTONOMY-INTEGRATION.md)

## T.A.R. / A.R.C. autonomy path

Future high-speed vehicle integration is autonomy-first:

```text
sensors / RF environment
      ↓
T.A.R. perception + fusion
      ↓
A.R.C. mission-level reasoning
      ↓
independent deterministic flight-safety controller
      ↓
verified vehicle control allocation
```

The conceptual target is approximately **97% automated routine flight workload**, not unrestricted AI control authority. T.A.R. and A.R.C. are not allowed to bypass the independent safety/control layer.

The first software bridge is implemented in the T.A.R. repository and supports IMU, air data, radar, EO/IR, lidar, GNSS, LEO signals-of-opportunity, ADS-B, terrain, weather and propulsion-health observations as normalized perception sources. The bridge produces **non-executable** A.R.C. advisories and fails closed on stale/low-confidence fast-loop sensing.

## V0.3 / OSU status

The older V0.3 / P3 broad plasma-optimization campaign remains **on hold** and is retained as research history / diagnostic reference.

P4E supersedes P3 as the immediate grant-scale proof-of-physics target. This repository update does **not** authorize contacting OSU or transmitting a new experimental pitch.

## Branch control

### Primary

**P4 full-stream Lorentz architecture**, with P4A–P4D as supporting refinements.

### Immediate experimental gate

**P4E grant-scale vibrationally conditioned pulsed-air MHD experiment.**

### Retained comparison

**V5 traveling-field induction MHD** remains a comparison model only.

### Boundary studies

Small plasma jets/ejectors, bulk oxygen conditioning and neutral-paramagnetic-air acceleration are retained as boundary studies and do **not** replace the vehicle goal.

## Current program conclusion

> **CRTFE remains an aircraft-scale atmospheric electromagnetic propulsion research program, but the immediate credible funding request is a much smaller controlled plasma/MHD experiment. P4E is designed to decide whether the missing conductivity-efficiency physics is real before further aircraft-scale development.**
