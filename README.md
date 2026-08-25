# CRFTE / CRTFE Atmospheric Electromagnetic Propulsion Research

> **Status:** conceptual / reduced-order research plus planned ground experimentation. No working lift hardware has been demonstrated.

## Project links

- [Website and ecosystem status](PROJECT-LINKS.md)
- [Commonwealth of Black America public record](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/Commonwealth-of-Black-America)
- [T.A.R. — The Akashic Records](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record)

No standalone CRFTE website has been verified or published yet; this repository remains the canonical public project location.

## Current research architecture

CRTFE investigates a **pre-ionized atmospheric flow + traveling electromagnetic field + Lorentz-force (J×B) momentum-transfer** architecture with a two-person eVTOL-scale target vehicle as the long-range application.

The immediate problem is narrower than aircraft design:

> **What combination of plasma excitation, geometry, airflow, residence time and deposited energy produces a repeatable spatially distributed conductive state that is sufficiently persistent and energy-efficient to justify a low-slip traveling-field electromagnetic momentum-transfer experiment?**

The project does not claim that plasma propulsion itself is a new field. The present research contribution is the attempt to experimentally map and optimize the coupled plasma-flow operating region relevant to this architecture and then test electromagnetic momentum transfer under controlled baselines.

## V0.3 P3 — optimization before coupling

V0.3 has been reengineered from a single scalar-conductivity gate into a staged optimization and scaling campaign.

Starting diagnostic baseline:

- 100 mm × 100 mm instrumented duct
- 10 / 20 / 30 m/s comparison points
- 20 / 50 / 80 mm multi-length impedance measurements
- 5×5 XY velocity traverse where instrumentation permits
- plasma-OFF baselines before energized testing
- electrical, thermal, optical and flow diagnostics

The campaign sequence is:

1. **P3-A — baseline validation**
2. **P3-B — plasma-source characterization**
3. **P3-C — operating-envelope sweep**
4. **P3-D — spatial/temporal persistence mapping**
5. **P3-E — multi-objective optimization**
6. **V0.4 — phase/direction-reversible electromagnetic coupling test**

Candidate excitation families for laboratory evaluation include steady/pulsed DC, nanosecond-pulsed, inductive AC and capacitive AC. Actual methods and operating limits are determined with qualified host-laboratory personnel.

The project retains approximately **60–150 S/m** as a hypothesis/engineering target region from the reduced-order model. It is not a measured result.

See:

- [V0.3 P3 Optimization and Scaling Campaign](docs/V0.3-P3-OPTIMIZATION-SCALING.md)
- [V0.3 P3 Optimization Gate](docs/V0.3-CONDUCTIVITY-GATE.md)
- [V0.3 Prototype Build Guide](docs/V0.3-PROTOTYPE-BUILD-GUIDE.md)

## What is optimized

CRTFE does not optimize conductivity alone. Candidate operating points are compared using:

- conductive volume
- spatial uniformity
- persistence / decay time
- repeatability
- energy per useful conductive volume
- thermal penalty
- filament/arc fraction
- flow disturbance
- compatibility with later traveling-field coupling

A configuration that underperforms is diagnosed and used to select the next controlled configuration. Experimental measurements remain falsifiable and are reported as measured.

## V0.4 electromagnetic gate

After V0.3 identifies a sufficiently characterized operating point, V0.4 introduces the traveling-field / magnetic interaction.

V0.4 requires plasma-only, field-only, installed-hardware and combined-operation controls plus phase/direction reversal where supported. The purpose is to distinguish an electromagnetic contribution from ionic wind, thermal expansion, aerodynamic blockage, vibration and measurement bias.

## Key reduced-order equations

```text
F = σ (v_wave - u) B² A L
v_slip = F / (σ B² A L)
P_ohmic = F v_slip = F² / (σ B² A L)
P_total = P_induced + P_ohmic + P_aux
```

These equations define the simplified traveling-field model; they do not establish that the required real atmospheric plasma state exists.

## V4 and V5 interpretation

### V4 — discrete filament route

The discrete-filament model exposed the identity `P/F = E/B`: sustaining a filament with a large electric field creates a severe power burden. Filamentary/streamer-dominated experimental results therefore cannot simply be substituted into the V5 bulk-conductivity model.

### V5 — conditional traveling-field closure

The reduced-order traveling-field model contains a conditional mathematical operating region. Its relevance depends on experimentally measured plasma conductivity, persistence, uniformity, auxiliary power, heating and real electromagnetic coupling.

## Target vehicle — V5

The repository retains a formal long-range target vehicle architecture in `docs/TARGET-VEHICLE-V5.md`.

Current conceptual packaging target:

- crew: 2 side-by-side
- design gross mass: 650 kg
- length: 6.20 m
- span: 5.40 m
- height: 1.80 m
- wing reference area: ~11 m²
- four active lift modules
- total active lift area: ~4.80 m²
- propulsion target: electrodeless conductive-air traveling-field electromagnetic architecture

**This is a design target, not demonstrated flight hardware.** Vehicle-scale engineering is downstream of V0.3, V0.4 and subsequent subscale validation.

## Reduced-order research baseline

Earlier sweeps used a separate 450 kg research baseline with four ~0.60 m² modules and ~0.50 m interaction length. Those values remain useful for historical model comparison but do not define the current diagnostic V0.3 apparatus or prove vehicle performance.

## V-2 hybrid research baseline

V-2 remains an evidence-gated propulsion research architecture while V5 remains the target vehicle. It combines an HTS static bias field, separately driven segmented traveling-wave stator, measured conductive-flow inputs, finite-length channel, external force balance and protective enclosure.

Controlled V-2 files include:

- [V-2 hybrid MHD baseline](docs/V2-HYBRID-MHD-BASELINE.md)
- [V-2 G2 electromagnetic verification and validation](docs/V2-G2-ELECTROMAGNETIC-VALIDATION.md)
- [P2 electrical integration specification](docs/CRTFE-V2-ELECTRICAL-INTEGRATION-P2.md)
- [V-2 blueprint package](docs/blueprints/CRTFE_V-2_Hybrid_MHD_Baseline_Package.pdf)
- [P2 electrical schematic set](docs/blueprints/CRTFE_V2_Electrical_Wiring_Schematic_Set_P2.pdf)
- [P2 integrated engineering manual](docs/manuals/CRTFE_V2_Integrated_Engineering_Assembly_Manual_P2.pdf)
- [P2 Phase 1 grant / partnership presentation](docs/presentations/CRTFE_Phase_1_Grant_Presentation_P2.pptx)

## Vehicle systems and ARC/T.A.R. integration

The target architecture also documents a removable energy sled, protective keel structure, bounded ARC vessel orchestration and T.A.R. signed/versioned knowledge layer.

ARC has no raw actuator authority. Independent deterministic flight/safety controllers remain responsible for validation and execution, with pilot/manual reversion retained.

See:

- [V5 Energy Sled / ARC Update](docs/V5-ENERGY-SLED-ARC-UPDATE.md)
- [ARC and Akashic Record Vessel Integration](docs/ARC-AKASHIC-VESSEL-INTEGRATION.md)
- [Target Vehicle V5](docs/TARGET-VEHICLE-V5.md)
- [Blueprint and Manual Index](docs/BLUEPRINTS-AND-MANUAL.md)

## Current program conclusion

> **The low-slip traveling-field branch remains a conditional engineering hypothesis. The immediate job is to optimize and measure the real moving-air plasma state, then test electromagnetic coupling with controls strong enough to identify the mechanism.**

CRTFE advances toward the target vehicle by converting each major assumption into a controlled measurement, optimization problem or engineering gate.