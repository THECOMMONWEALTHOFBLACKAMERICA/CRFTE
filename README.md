# CRFTE / CRTFE Atmospheric Electromagnetic Propulsion Research

> **Status:** conceptual / reduced-order research. No working lift hardware has been demonstrated.

## Project links

- [Website and ecosystem status](PROJECT-LINKS.md)
- [Commonwealth of Black America public record](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/Commonwealth-of-Black-America)
- [T.A.R. — The Akashic Records](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record)

No standalone CRFTE website has been verified or published yet; this repository remains the canonical public project location.

This repository documents an ongoing investigation into a two-person eVTOL-scale atmospheric electromagnetic propulsion concept. The current working architecture is a **pre-ionized atmospheric flow + traveling electromagnetic field + Lorentz-force (J×B) momentum transfer** system.

The project originally explored counter-rotating toroidal plasmas, rotating liquid metals, magnetic levitation, resonance, plasma propulsion, and artificial-dynamo analogies. The research has since converged on a much narrower and testable question:

> **Can moving atmospheric air be maintained at roughly 60–150 S/m effective conductivity, at sufficiently low auxiliary power and heating, so that a low-slip traveling electromagnetic field can produce useful MHD thrust?**

## Target vehicle — CRFTE V5

The repository now defines a formal **target vehicle architecture** in `docs/TARGET-VEHICLE-V5.md`.

Current target packaging baseline:

- **Crew:** 2 side-by-side
- **Design gross mass:** 650 kg conceptual target
- **Length:** 6.20 m
- **Span:** 5.40 m
- **Height:** 1.80 m
- **Wing reference area:** ~11 m²
- **Four active lift modules:** ~1.20 m² effective area each
- **Total active lift area:** ~4.80 m²
- **Propulsion:** electrodeless conductive-air traveling-field MHD concept
- **Energy source:** battery/hybrid research architecture; final sizing pending measured propulsion power

The target vehicle document includes the propulsion core, HTS/cryogenic system, batteries and HV distribution, thermal management, two-seat fuselage packaging, flight controls, avionics, ECS/emergency oxygen, safety architecture, mass budget, power budget, development gates, and drawing-status limitations.

**The V5 target vehicle is a design target, not a claim of demonstrated flight capability.** Vehicle-scale performance remains contingent on V0.3/V0.4 and subsequent subscale propulsion testing.

## Reduced-order research baseline

The original propulsion sweeps use:

- Vehicle gross mass: **450 kg**
- Four lift modules
- Effective area per module: **0.60 m²**
- MHD interaction length: **0.50 m**
- Hover thrust per module: **~1,104 N**
- Ideal actuator velocity: **~27.68 m/s**
- Air mass flow per module: **~19.9 kg/s**
- Ideal induced power per module: **~30.57 kW**
- Working power cap: **60 kW/module**

This remains a research baseline only and is not the target aircraft geometry.

## 650 kg target-vehicle hover sanity check

At 650 kg with 4.80 m² total effective lift area, sea-level ideal actuator-disk momentum theory gives approximately:

- weight: **6.37 kN**
- hover thrust per module: **1.59 kN**
- disk loading: **~1.33 kN/m²**
- ideal induced velocity: **~23.3 m/s**
- ideal induced hover power: **~148.5 kW total / ~37.1 kW per module**

These are ideal lower bounds, not predicted CRFTE electrical input.

## Key equations

```text
F = σ (v_wave - u) B² A L
v_slip = F / (σ B² A L)
P_ohmic = F v_slip = F² / (σ B² A L)
P_total = P_induced + P_ohmic + P_aux
```

Where `σ` is effective conductivity, `B` magnetic field, `u` actuator-zone air speed, `v_wave` traveling-field speed, `A` active channel area and `L` interaction length.

## V4 result — discrete filament route fails

The discrete-filament model exposed the identity `P/F = E/B`: if a filament must be sustained by a large electric field, increasing conductivity/current does not eliminate the power burden. V4 remains the standing failure model for filamentary/streamer experimental results.

## V5 result — conditional traveling-field closure

The reduced-order traveling-field model contains a feasible mathematical region, but it remains contingent on atmospheric conductivity that has not been demonstrated for this application. The stronger research target remains approximately **80–150 S/m**, with the lower conditional boundary around the 50–60 S/m region depending on auxiliary power and geometry.

## Primary unresolved bottleneck

The next decisive step remains **V0.3: moving-air conductivity measurement**.

The V0.3 rig uses a 100 mm × 100 mm test duct, paired 10/20/30 m/s plasma-OFF baselines, 5×5 XY velocity traverse, 20/50/80 mm multi-length impedance measurements, temperature measurements, imaging and strict volumetric/filamentary/arc classification.

### Decision gates

| Measured result | Action |
|---|---|
| Bulk σ < 20 S/m | Stop / major pivot for the present full-channel design |
| 20–60 S/m | Borderline; diagnose and redesign |
| ≥ 60 S/m | Re-run V5 using measured auxiliary power and thermal data |
| 80–150+ S/m | Preferred region if real power/heating still close |
| Filamentary result | Use V4 failure model, not V5 bulk assumption |
| Thermal/arc-only conductivity | Treat as a different hot-plasma architecture with full thermal penalty |

## Repository contents

- `docs/TARGET-VEHICLE-V5.md` — **formal target vehicle architecture**, packaging, systems, mass/power budgets and development gates
- `docs/HYPOTHETICAL-CRAFT-DESIGN.md` — earlier two-seat packaging study
- `docs/V4-V5-REVISED.md` — corrected simulation interpretation
- `docs/V0.3-CONDUCTIVITY-GATE.md` — experimental decision protocol
- `docs/V0.3-PROTOTYPE-BUILD-GUIDE.md` — stationary prototype plan, BOM and paired-baseline measurement protocol
- `data/` — reduced-order V4/V5 simulation outputs


## V5 energy sled, protective shield and THE ARC

The target-vehicle architecture now includes:

- a removable ventral keel energy sled at/near the center of gravity
- a preliminary 1.45 m x 1.05 m x 0.34 m maximum packaging envelope
- a multi-layer replaceable keel shield with standoff, anti-penetration, crush and fire/thermal layers
- guarded down/aft venting, drainage, impact sensing, dry-break cooling and isolated HV interfaces
- an inert-mockup assembly sequence and candidate fastener study
- A3 graph-paper general-arrangement drawings using only supported project dimensions
- **THE ARC**, a bounded vessel AI orchestration architecture
- T.A.R.'s signed/versioned **Akashic Record** knowledge layer

THE ARC may plan and request actions under authenticated human command, but it has no raw actuator authority. Independent deterministic flight/safety controllers validate and execute any bounded request, and pilot/manual reversion remains available.

See [V5 Energy Sled, Protective Shield and THE ARC Update](docs/V5-ENERGY-SLED-ARC-UPDATE.md).

Current controlled concept files:

- [A3 blue-pencil graph drawing set](docs/blueprints/CRTFE_V5_Blue_Pencil_Graph_Drawing_Set.pdf)
- [V5 energy-sled engineering and assembly manual](docs/manuals/CRTFE_V5_Energy_Sled_Preliminary_Engineering_Manual.pdf)
- [Blueprint and manual revision index](docs/BLUEPRINTS-AND-MANUAL.md)


## Current scientific conclusion

> **The traveling-field branch has conditional reduced-order closure, contingent on an atmospheric-conductivity state that has not yet been demonstrated for this application.**

The V5 aircraft is the project's **target vehicle**. The engineering program advances toward it only when each experimental gate is satisfied.

## CRTFE V-2 hybrid research baseline — Revision 1.2

V-2 is the next evidence-gated propulsion research architecture while V5 remains the target vehicle and packaging reference. It combines an HTS static bias field, a separately driven segmented traveling-wave stator, measured conductive-flow inputs, a finite-length channel, a variable-area nozzle, an external force balance and a field-compatible protective enclosure.

The electromagnetic gate is now staged from numerical verification through bare-coil, installed-hardware, combined HTS/stator and plasma-loaded validation. Preliminary comparison objectives are not released acceptance criteria; final limits must be pre-registered from measurement uncertainty and design sensitivity.

Controlled V-2 files:

- [V-2 hybrid MHD baseline](docs/V2-HYBRID-MHD-BASELINE.md)
- [V-2 Revision P1.2 blueprint package](docs/blueprints/CRTFE_V-2_Hybrid_MHD_Baseline_Package.pdf)
- [V-2 G2 electromagnetic verification and validation](docs/V2-G2-ELECTROMAGNETIC-VALIDATION.md)
- [ARC and Akashic Record vessel integration](docs/ARC-AKASHIC-VESSEL-INTEGRATION.md)
- [P2 electrical integration specification](docs/CRTFE-V2-ELECTRICAL-INTEGRATION-P2.md)
- [P2 eight-sheet electrical wiring schematic set](docs/blueprints/CRTFE_V2_Electrical_Wiring_Schematic_Set_P2.pdf)
- [P2 47-page integrated engineering, wiring and assembly manual](docs/manuals/CRTFE_V2_Integrated_Engineering_Assembly_Manual_P2.pdf)
- [P2 Phase 1 grant and partnership presentation](docs/presentations/CRTFE_Phase_1_Grant_Presentation_P2.pptx)
- [Blueprint, schematic and manual revision index](docs/BLUEPRINTS-AND-MANUAL.md)

Revision P2 is a concept and ground-research release only. It does not release flight hardware, energized work, final conductor sizes, final connector pinouts, protection-device ratings or HV/HTS test limits.

The Akashic Record is the signed knowledge and mission-memory layer. It is an avionics/compute electrical load, not the ship's energy source. ARC vessel integration Revision 1.4 adds regime-aware evidence retrieval, explicit contradiction mapping, explainable non-executable research plans and uncertainty-aware digital-twin comparison on top of Revision 1.3's persistent mediation service. Independent deterministic controls, hardwired safety protection and pilot authority remain outside ARC.
