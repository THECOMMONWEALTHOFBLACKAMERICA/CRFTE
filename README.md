# CRFTE / CRTFE Atmospheric Electromagnetic Propulsion Research

> **Status:** conceptual / reduced-order research. No working lift hardware has been demonstrated.

This repository documents an ongoing investigation into a two-person eVTOL-scale atmospheric electromagnetic propulsion concept. The current working architecture is a **pre-ionized atmospheric flow + traveling electromagnetic field + Lorentz-force (J×B) momentum transfer** system.

The project originally explored counter-rotating toroidal plasmas, rotating liquid metals, magnetic levitation, resonance, plasma propulsion, and artificial-dynamo analogies. The research has since converged on a much narrower and testable question:

> **Can moving atmospheric air be maintained at roughly 60–150 S/m effective conductivity, at sufficiently low auxiliary power and heating, so that a low-slip traveling electromagnetic field can produce useful MHD thrust?**

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

This remains a research baseline only. It should **not** be presented as a complete two-seat aircraft mass estimate.

## Hypothetical two-seat aircraft packaging baseline

A separate packaging study now includes real room for two occupants, controls, avionics, batteries, thermal hardware, landing gear, environmental-control/oxygen hardware, and distributed propulsion zones.

Use the following conceptual aircraft geometry going forward:

- **Design gross mass:** 650 kg
- **Length:** 6.2 m
- **Wingspan:** 5.4 m
- **Overall height:** 1.8 m
- **Wing reference area:** ~11 m²
- **Crew:** 2 side-by-side
- **Cockpit internal envelope:** ~1.4 m wide × 2.2 m long × 1.2 m usable seated height
- **Centerbody external width:** ~1.6 m
- **Four active lift/propulsion regions:** ~1.2 m² each
- **Total active lift area:** ~4.8 m²

See `docs/HYPOTHETICAL-CRAFT-DESIGN.md` for the full dimension, cockpit, controls, environmental-control, and mass-budget discussion.

At 650 kg the required hover thrust is ~1,594 N/module. Keeping only 0.60 m²/module would push the ideal induced power to ~53 kW/module before plasma/magnet/auxiliary losses, so the aircraft packaging study doubles active area to ~1.20 m²/module. At that area the ideal induced term is ~37.5 kW/module.

At the earlier conditional V5 point (`sigma = 150 S/m`, `B = 1.8 T`) the re-sized 650 kg packaging case gives roughly:

- required slip: **5.47 m/s**
- Ohmic/slip power: **8.71 kW/module**
- assumed auxiliary allowance: **5 kW/module**
- modeled total: **~51.2 kW/module**

This is still **conditional reduced-order math**, not a validated flight prediction, and requires a fresh V5 run if V0.3 succeeds.

## Key equations

```text
F = σ (v_wave - u) B² A L

v_slip = F / (σ B² A L)

P_ohmic = F v_slip = F² / (σ B² A L)

P_total = P_induced + P_ohmic + P_aux
```

Where:

- `σ` = effective conductivity of the moving atmospheric channel
- `B` = magnetic field
- `u` = actuator-zone air speed
- `v_wave` = traveling magnetic field speed
- `A` = active channel area
- `L` = interaction length

## V4 result — discrete filament route fails

The discrete-filament model treated the plasma as short-lived conductive channels instead of a uniform conducting volume.

```text
I_fil = σ_fil E A_fil
F_fil = I_fil L B
P_fil = I_fil E L
P/F = E/B
```

This exposed the central problem: if the filament must be sustained by a large electric field, increasing conductivity or current does not eliminate the power burden. At `E = 10,000 V/m` and `B = 1.5 T`, the thrust-limited electrical power is megawatt-class for a 1,104 N module.

**V4 remains a standing failure model.** If experiments produce filamentary/streamer conduction instead of a volumetric conductive region, measured filament parameters must be fed back into V4 rather than averaged into an optimistic bulk conductivity.

## V5 result — conditional traveling-field closure

V5 replaced the large filament sustaining field with a low-slip, electrodeless traveling electromagnetic field.

The reduced-order model contains a feasible mathematical region. At `B = 1.8 T`, the steady conductivity boundary is approximately:

- **~52 S/m** with 5 kW auxiliary allowance
- **~59 S/m** with 8 kW auxiliary allowance

A stronger research target is approximately **80–150 S/m** to provide margin for conductivity ripple and unmodeled losses.

Representative conditional point from the original 450 kg research baseline:

- σ = 150 S/m
- B = 1.8 T
- slip = 7.57 m/s
- traveling-wave speed = 35.26 m/s
- ideal induced power = 30.57 kW
- Ohmic/slip power = 8.36 kW
- assumed auxiliary = 5.00 kW
- modeled total = **43.93 kW/module**

This is **conditional reduced-order closure, not demonstrated feasibility**.

## Primary unresolved bottleneck

The entire V5 feasible region depends on whether atmospheric air can actually achieve the required conductivity non-thermally, uniformly, long enough, and cheaply enough.

The next decisive step is therefore **V0.3: moving-air conductivity measurement**.

### V0.3 prototype now documented

The repository includes a stationary test-rig plan:

- `docs/V0.3-PROTOTYPE-BUILD-GUIDE.md`

The recommended first rig is approximately **1.2 m long**, with a **100 mm × 100 mm internal duct**, variable blower, flow straightener, removable enclosed plasma cassette, downstream temperature/velocity/impedance diagnostics, camera observation, E-stop, and enclosure interlock.

The current revision adds paired 10/20/30 m/s baselines, a 5×5 XY hot-wire velocity traverse, and 20/50/80 mm multi-length impedance measurements.

Measure:

- `σ_eff(t)` — bulk effective conductivity and decay
- ionization input power
- gas temperature / bulk ΔT
- spatial uniformity vs filamentation
- conductivity lifetime and refresh rate
- downstream momentum coupling

### Decision gates

| Measured result | Action |
|---|---|
| Bulk σ < 20 S/m | Stop / major pivot for the present full-channel design |
| 20–60 S/m | Borderline; redesign / higher-field work only |
| ≥ 60 S/m | Re-run V5 using measured P_aux and thermal data |
| 80–150+ S/m | Preferred region if real power/heating still close |
| Filamentary result | Use V4 failure model, not V5 bulk assumption |
| Thermal/arc-only conductivity | Treat as a different hot-plasma architecture with its full thermal penalty |

## Environmental-control / oxygen position

The first terrestrial demonstrator should not carry a spacecraft-style regenerative oxygen system. The current packaging study reserves room for cabin recirculation, filtration, CO2 monitoring/scrubbing backup, humidity/temperature control, cabin pressure monitoring, and emergency supplemental oxygen.

A true regenerative oxygen-generation/recovery system is a separate high-altitude/long-duration technology program. Early flight-test planning should remain below oxygen-requiring cabin-altitude regimes whenever possible.

## Research discipline

This project does **not** assume antigravity, inertia cancellation, zero-point extraction, or spacetime manipulation. Counter-rotating toroidal plasma / spheromak / FRC concepts may still be investigated as field-topology tools, but any anomalous-force claim must survive subtraction of conventional J×B forces, ion wind, cable forces, magnetic coupling, vibration, acoustics, thermal expansion, and sensor drift.

## Repository contents

- `docs/V4-V5-REVISED.md` — corrected interpretation and simulation summary
- `docs/V0.3-CONDUCTIVITY-GATE.md` — experimental decision protocol
- `docs/V0.3-PROTOTYPE-BUILD-GUIDE.md` — stationary prototype build plan, BOM, paired baselines, XY traverse, and decision gates
- `docs/HYPOTHETICAL-CRAFT-DESIGN.md` — corrected two-seat aircraft dimensions, controls, environmental-control/oxygen packaging, and 650 kg mass/area re-check
- `data/` — reduced-order V4/V5 simulation outputs

## Current scientific conclusion

> **The traveling-field branch has conditional reduced-order closure, contingent on an atmospheric-conductivity state that has not yet been demonstrated for this application.**

The next meaningful progress must come from measured conductivity, ionization-power, heating, lifetime, and spatial-uniformity data — not another unconstrained vehicle-scale sweep.