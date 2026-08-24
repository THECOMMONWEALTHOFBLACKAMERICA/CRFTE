# CRTFE V5 Energy Sled, Protective Keel Shield and THE ARC Update

> Status: preliminary concept architecture. Not a fabrication drawing, flight release or claim of demonstrated propulsion.

## Updated vehicle systems

The V5 target vehicle now includes three coordinated additions:

1. a removable ventral keel energy sled
2. a multi-layer protective keel shield
3. THE ARC vessel-wide AI command and knowledge architecture, with T.A.R.'s Akashic Record as its provenance-aware knowledge layer

## Energy sled envelope

Known coordination envelope:

- maximum sled length: 1.45 m
- maximum sled width: 1.05 m
- maximum sled height: 0.34 m
- location: at or near the vehicle center of gravity
- existing battery-system mass allowance: 120 kg
- existing central power-bay envelope: approximately 1.60 m longitudinally

The 120 kg allowance must include cells, containment, structure, shield, cooling, BMS, switching, buswork, harnesses, sensors and fasteners unless the vehicle mass budget is revised.

At the existing 228 kW placeholder total hover input:

| Duration | Energy before reserve/losses |
|---|---:|
| 5 minutes | 19.0 kWh |
| 10 minutes | 38.0 kWh |
| 15 minutes | 57.0 kWh |

This exposes a major sizing gate. Cell chemistry, usable state-of-charge window, C-rate, reserve, thermal rejection and containment mass must be selected before voltage, cell count or credible hover endurance can be released.

## Shield stack

Outside to inside:

1. replaceable titanium/composite strike skin
2. inspectable standoff and debris gap
3. aramid/ceramic anti-penetration layer
4. energy-absorbing crush core
5. fire/thermal barrier
6. structural sled and segmented module volume

The guarded vent path routes down and aft, away from the occupants. Its area, burst behavior and gas/particle/fire performance remain TBD by representative-cell testing.

## Candidate mockup fasteners

The current assembly manual studies metric candidates from M4 through M12 using A286, Ti-6Al-4V and ground-equipment class 10.9 hardware as appropriate.

These are fit-check/mockup selections, not released flight fasteners. Flight release requires joint loads, grip-stack control, preload scatter, combined shear/tension analysis, composite bearing/bypass and pull-through testing, fatigue, vibration, galvanic review and torque-tension testing.

## Scaled drawing basis

The graph-paper general arrangement carries only dimensions supported by the project:

- vehicle length: 6.20 m
- span: 5.40 m
- height: 1.80 m
- wing reference area: approximately 11 m2
- four lift modules at approximately 1.20 m2 effective area each
- sled envelope: 1.45 x 1.05 x 0.34 m maximum

Bulkhead stations, bolt-hole coordinates, shield-layer thicknesses, vent area, connector positions and laminate schedules remain preliminary/TBD.

## THE ARC and the Akashic Record

THE ARC is the proposed adaptive reasoning and command-orchestration layer. It can plan, diagnose, research and coordinate vessel systems under authenticated human command.

It is not the final actuator controller.

```text
Human command
  -> THE ARC bounded request
  -> independent safety validation
  -> deterministic flight/module controller
  -> vehicle action
```

T.A.R.'s Akashic Record supplies signed, versioned records for:

- verified science
- space knowledge
- competing theories with evidence and falsification tests
- CRTFE project data and digital twin
- procedures and checklists
- mission logs
- sensor history

See [THE ARC and the Akashic Record](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record/blob/main/docs/THE-ARC-AKASHIC-RECORD.md).

## Development sequence

1. inert full-scale energy-sled packaging mockup
2. shield material and joint coupons
3. subscale containment and vent testing
4. instrumented inert full-scale sled
5. representative module abuse testing in a remote facility
6. integrated electrical/thermal iron-bird
7. ARC knowledge prototype and software-in-the-loop
8. ARC hardware-in-the-loop and fault injection
9. bounded uncrewed test only after propulsion, structural and safety gates

No crewed integration is authorized by this concept update.
