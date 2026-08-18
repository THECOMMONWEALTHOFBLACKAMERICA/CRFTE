# CRFTE / CRTFE Atmospheric Electromagnetic Propulsion Research

> **Status:** conceptual / reduced-order research. No working lift hardware has been demonstrated.

This repository documents an ongoing investigation into a two-person eVTOL-scale atmospheric electromagnetic propulsion concept. The current working architecture is a **pre-ionized atmospheric flow + traveling electromagnetic field + Lorentz-force (J×B) momentum transfer** system.

The project originally explored counter-rotating toroidal plasmas, rotating liquid metals, magnetic levitation, resonance, plasma propulsion, and artificial-dynamo analogies. The research has since converged on a much narrower and testable question:

> **Can moving atmospheric air be maintained at roughly 60–150 S/m effective conductivity, at sufficiently low auxiliary power and heating, so that a low-slip traveling electromagnetic field can produce useful MHD thrust?**

## Current baseline

- Vehicle gross mass: **450 kg**
- Four lift modules
- Effective area per module: **0.60 m²**
- MHD interaction length: **0.50 m**
- Hover thrust per module: **~1,104 N**
- Ideal actuator velocity: **~27.68 m/s**
- Air mass flow per module: **~19.9 kg/s**
- Ideal induced power per module: **~30.57 kW**
- Working power cap: **60 kW/module**

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

Representative conditional point:

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

The repository now includes a buildable stationary test-rig plan:

- `docs/V0.3-PROTOTYPE-BUILD-GUIDE.md`

The recommended first rig is approximately **1.2 m long**, with a **100 mm × 100 mm internal duct**, variable blower, flow straightener, removable enclosed plasma cassette, downstream temperature/velocity/impedance diagnostics, camera observation, E-stop, and enclosure interlock.

Working planning budget:

- **~$1,000–$1,800** for the mechanical duct/frame/basic sensors
- **~$3,220–$5,600 total** if the enclosed plasma source and diagnostic instruments must also be purchased

The rig intentionally treats the high-voltage plasma source as a professionally enclosed or institutional subsystem rather than a DIY pulser.

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

## Research discipline

This project does **not** assume antigravity, inertia cancellation, zero-point extraction, or spacetime manipulation. Counter-rotating toroidal plasma / spheromak / FRC concepts may still be investigated as field-topology tools, but any anomalous-force claim must survive subtraction of conventional J×B forces, ion wind, cable forces, magnetic coupling, vibration, acoustics, thermal expansion, and sensor drift.

## Repository contents

- `docs/V4-V5-REVISED.md` — corrected interpretation and simulation summary
- `docs/V0.3-CONDUCTIVITY-GATE.md` — experimental decision protocol
- `docs/V0.3-PROTOTYPE-BUILD-GUIDE.md` — stationary prototype build plan, BOM, test procedure, and decision gates
- `data/` — reduced-order V4/V5 simulation outputs

## Current scientific conclusion

> **The traveling-field branch has conditional reduced-order closure, contingent on an atmospheric-conductivity state that has not yet been demonstrated for this application.**

The next meaningful progress must come from measured conductivity, ionization-power, heating, lifetime, and spatial-uniformity data — not another unconstrained vehicle-scale sweep.