# CRFTE V5 Target Vehicle — Concept Definition

> **Status:** Hypothetical target vehicle / research architecture. This is not a flight-ready design, certification drawing set, or evidence that CRFTE propulsion works. The propulsion concept remains contingent on V0.3/V0.4 experimental validation.

## Target configuration

The target is a two-seat, wingborne-transition VTOL research aircraft built around four modular conductive-air traveling-field MHD lift/propulsion modules.

| Parameter | Target |
|---|---:|
| Crew | 2, side-by-side |
| Design gross mass | 650 kg |
| Length | 6.20 m |
| Span | 5.40 m |
| Height | 1.80 m |
| Wing reference area | ~11 m² |
| Active lift area | 4 × 1.20 m² = 4.80 m² |
| Cockpit internal width | ~1.40 m |
| Lift modules | 4 |

The original 4 × 0.60 m² geometry remains the **450 kg reduced-order research baseline**. It is not the target vehicle geometry. At 650 kg, the target vehicle carries ~1.20 m² effective active area per module.

## Packaging / fuselage stations

Conceptual nose-to-tail envelopes:

- **0.00–1.20 m:** nose crash structure, air-data and avionics bay.
- **1.20–2.50 m:** two-seat cockpit, flight controls, displays, restraints, emergency oxygen/ECS interfaces.
- **2.50–4.10 m:** central battery packs, HV distribution, BMS and propulsion power electronics near CG.
- **4.10–5.20 m:** HTS cryogenic equipment, thermal-management hardware and service interfaces.
- **5.20–6.20 m:** aft avionics/telemetry, heat-rejection hardware and tail structure.

These are packaging targets, not structural bulkhead drawings.

## Hover sanity check

For `m = 650 kg`, `rho = 1.225 kg/m³`, and total effective lift area `A = 4.80 m²`:

```text
W = mg ≈ 6.374 kN
F_module ≈ 1.594 kN
Disk loading ≈ 1,328 N/m²
v_i = sqrt(W/(2 rho A)) ≈ 23.3 m/s
P_induced,ideal = W v_i ≈ 148.5 kW total
P_induced,ideal/module ≈ 37.1 kW
```

This is an ideal momentum-theory lower bound. It is not a prediction of CRFTE electrical power.

## Working power budget

The current conceptual hover budget is ~228 kW total:

| Item | Total working allowance |
|---|---:|
| Ideal/useful induced-fluid work | ~100–150 kW depending model definition |
| Channel / Ohmic loss allowance | ~40 kW |
| Ionization / pre-ionization | ~32 kW |
| Traveling-field losses | ~20 kW |
| HTS magnet + cryogenic support | ~12 kW |
| Pumps / cooling / auxiliaries | ~16 kW |
| Avionics / controls / ECS | ~8 kW |

**Important:** the non-induced values are placeholders. V0.3 must replace the conductivity/ionization assumptions with measured data. A detailed energy accounting must avoid double-counting induced work and electromagnetic input.

## Mass budget

| System | kg | % gross |
|---|---:|---:|
| Primary structure / airframe | 150 | 23.1% |
| Four propulsion modules / housings | 160 | 24.6% |
| Battery system | 120 | 18.5% |
| Cryogenic / HTS system | 60 | 9.2% |
| Power electronics / distribution | 50 | 7.7% |
| Avionics / controls / sensors | 30 | 4.6% |
| Thermal management / ECS | 40 | 6.2% |
| Landing gear / brakes | 20 | 3.1% |
| Cockpit / seats / restraints | 20 | 3.1% |
| **Total** | **650** | **100%** |

This budget has effectively no mature-aircraft growth reserve. Detailed engineering may force a 750–900 kg design gross mass unless propulsion, cryogenic, battery and structural masses beat these placeholders.

## Propulsion core

Each of four modules conceptually contains:

- ~1.20 m² effective lift/interaction area;
- replaceable pre-ionization architecture selected after V0.3;
- traveling-field electromagnetic coil array;
- HTS bias-field magnet assembly;
- structural reaction path for magnet loads;
- module controller and independent instrumentation;
- guarded inlet/outlet and service disconnects.

Working interaction length remains ~0.5 m until detailed module optimization.

## Cryogenic system

Target architecture reserves volume and mass for:

- HTS cryostat vacuum vessels;
- cryocooler or consumable-cryogen system to be selected after magnet design;
- thermal isolation between ionization/duct hardware and HTS components;
- quench detection and energy-dump circuitry;
- current leads and service connections;
- cryogenic plumbing where applicable.

## Power generation and storage

- high-energy/high-power battery pack centered near aircraft CG;
- BMS and pack-level fault isolation;
- propulsion HV DC bus;
- independent essential 12/24/48-V low-voltage bus;
- four module inverters/drivers;
- DC-DC conversion;
- precharge, contactors and isolation monitoring;
- ground-power/charging interface.

A final battery capacity cannot be specified until measured propulsion and auxiliary power are available.

## Thermal management

Separate thermal paths are required for:

- propulsion power electronics;
- plasma/ionization and duct waste heat;
- battery pack;
- cryogenic equipment heat rejection;
- cabin/environmental control.

The target vehicle reserves pumps, reservoirs, heat exchangers, radiators and temperature/flow sensing. Heat-rejection sizing remains open.

## Flight controls and avionics

Target architecture:

- dual flight-control computers;
- independent module-level thrust control for amplitude/phase/slip/duty cycle;
- dual IMUs / attitude reference;
- air-data system and GNSS;
- conventional wingborne control surfaces;
- cockpit displays and control inceptors;
- independent data logging/telemetry;
- essential-bus backup instrumentation.

## Occupant and environmental system

The terrestrial demonstrator does **not** assume a spacecraft-style regenerative oxygen loop.

Packaging is reserved for:

- two seats and restraints;
- ventilation / filtered recirculation;
- temperature and humidity control;
- O2 and CO2 monitoring;
- emergency supplemental oxygen;
- optional CO2 scrubbing backup;
- cabin-pressure monitoring if higher-altitude development is pursued.

A fully closed-loop oxygen-generation/recovery system would be a separate technology program.

## Safety architecture

- HV isolation monitoring and physical segregation from low-voltage wiring;
- module-level shutdown and fault isolation;
- HTS quench detection/protection;
- battery thermal-runaway containment and venting;
- fire detection/suppression in critical bays;
- guarded propulsion inlets;
- emergency E-stop architecture;
- crashworthy occupant cell / energy absorption study;
- emergency egress;
- whole-aircraft parachute feasibility study;
- no assumption that one-module-out operation can sustain hover until demonstrated.

## Aspirational performance targets

These are **program targets**, not predictions:

| Requirement | Status |
|---|---|
| VTOL / hover | Target |
| Wingborne transition | Target |
| 250+ kt cruise | Aspirational; requires aero + propulsion validation |
| 60–120 nm range | Aspirational; battery/power dependent |
| 20,000+ ft ceiling | Aspirational; ECS/oxygen/certification dependent |
| ±6 g structural target | Conceptual; requires full loads/aeroelastic analysis |
| All-weather/night | Long-term target |

## Development gates

1. **V0.3 — conductivity:** independently verify useful bulk conductivity in moving atmospheric air at acceptable power and temperature. Filamentary/arc behavior is classified separately and fed to V4.
2. **V0.4 — magnetic interaction:** calibrated traveling-field/bias-field force test with artifact subtraction.
3. **Subscale propulsion module:** repeatable thrust, thermal stability, efficiency and controllability.
4. **Four-module iron-bird:** full power/controls/thermal/cryo integration with no occupants.
5. **Tethered unmanned demonstrator:** only after independent safety review and adequate thrust margin.
6. **Crewed demonstrator:** substantially later, after unmanned validation and aviation engineering/certification work.

## Blueprint status

The project blueprint is a **concept-architecture illustration** intended to communicate packaging, dimensions, systems and interfaces. It is not a fabrication drawing. Structural laminate schedules, fastener patterns, pressure boundaries, electrical clearances, magnet containment, flutter/aeroelasticity, crash loads and certification compliance remain open engineering tasks.

The printable concept package generated for the project is named `CRFTE_V5_Target_Vehicle_Concept_Package.pdf`; the high-resolution blueprint source is maintained with the project working artifacts.
