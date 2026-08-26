# CRFTE Target Vehicle — Current Concept Definition

> **Status:** hypothetical target vehicle / research architecture. This is not a flight-ready design, certification drawing set, or evidence that CRFTE propulsion works. Vehicle scaling remains contingent on the P4E proof-of-physics result and later subscale propulsion validation.

## Naming note

CRFTE is the legacy program identifier originating from the historical **Counter-Rotating Field Thrust Engine** concept.

The present vehicle does **not** require counter-rotating magnetic fields. Its current propulsion concept is the **P4 Atmospheric Electromagnetic Propulsion architecture**: controlled conductivity, transverse current, and a predominantly stationary magnetic field producing `J × B` momentum transfer in atmospheric air.

See [CRFTE Name and Architecture Lineage](CRFTE-NAME-AND-ARCHITECTURE-LINEAGE.md).

## Target configuration

The long-range target is a two-seat, wingborne-transition VTOL research aircraft built around four distributed P4 atmospheric-electromagnetic propulsion modules.

| Parameter | Target |
|---|---:|
| Crew | 2, side-by-side |
| Design gross mass | ~650 kg reference |
| Length | ~6.20 m concept envelope |
| Span | ~5.40 m concept envelope |
| Height | ~1.80 m concept envelope |
| Wing reference area | ~11 m² |
| Total active propulsion area | ~4.80 m² |
| Cockpit internal width | ~1.40 m |
| Propulsion modules | 4 |

The geometry is a systems-integration reference, not a fabrication drawing.

## P4 propulsion concept

Each distributed module is currently modeled around:

- atmospheric air as the working mass;
- ~1.20 m² effective interaction area per module in the 650 kg reference;
- controlled pulsed / distributed conductivity;
- a predominantly stationary high-field magnetic region;
- separately established or induced transverse plasma current;
- direct Lorentz `J × B` momentum transfer;
- segmented timing / commutation;
- module-level electrical, thermal, magnetic and plasma diagnostics.

**Counter-rotating magnetic fields are not a current vehicle requirement.**

P4A/P4B/P4C remain candidate current-drive refinements. P4D/P4E address the conductivity/energy physics that must be demonstrated before vehicle-scale hardware is justified.

## Hover sanity check

For `m = 650 kg`, `rho = 1.225 kg/m³`, and total effective lift area `A = 4.80 m²`:

```text
W = mg ≈ 6.38 kN
F_module ≈ 1.59 kN
Disk loading ≈ 1.33 kN/m²
v_i ≈ 23.3 m/s
P_induced,ideal ≈ 148.5 kW total
```

This is an ideal momentum-theory lower bound. It is not a prediction of CRFTE electrical power or proof that P4 can reach hover thrust.

## Propulsion evidence gates

The vehicle concept cannot advance on assumed thrust alone.

### Gate 1 — P4E plasma/MHD proof of physics

Demonstrate a controlled, polarity-reversible Lorentz-force response and quantify conductivity-time and electrical-energy cost in moving atmospheric air.

### Gate 2 — electrodeless / induced-current translation

If P4E passes, test whether P4B/P4C-style current drive can reproduce the useful force/impulse without relying on the laboratory sustainer architecture.

### Gate 3 — subscale module

Demonstrate repeatable thrust / momentum transfer, controllability, thermal stability, plasma uniformity and a complete energy ledger.

### Gate 4 — multi-module iron-bird

Integrate propulsion, power, thermal, magnetic, cryogenic, sensing and deterministic control systems with no occupants.

### Gate 5 — unmanned vehicle

Only after independent safety review and demonstrated control authority.

### Gate 6 — crewed demonstrator

Substantially later, following unmanned validation and formal aviation engineering / certification work.

## Power and mass status

The earlier project contained placeholder vehicle power and mass budgets. They remain packaging studies only.

The only robust current vehicle-level energy anchor is the ideal fluid-power floor. Propulsion electrical power cannot be closed until P4E and later module tests measure:

```text
plasma conditioning energy
+ gas-current Joule loss
+ current-drive loss
+ magnet / cryogenic burden
+ thermal-rejection burden
+ power-electronics loss
```

Any vehicle power figure that depends on unmeasured conductivity or plasma efficiency remains provisional.

## Flight-control architecture

The vehicle is autonomy-first because the conceptual high-speed envelope can exceed useful human reaction capability for some disturbances and conflicts.

```text
vehicle + environmental sensors
        ↓
T.A.R. perception / sensor fusion
        ↓
A.R.C. mission-level reasoning
        ↓
independent deterministic flight-safety controller
        ↓
verified control allocation
        ↓
P4 propulsion modules + aerodynamic effectors where present
```

T.A.R. and A.R.C. do not directly command raw propulsion voltages, currents, magnetic-field setpoints or control-surface positions.

The conceptual target is approximately **97% automated routine flight workload**, while the operator retains mission-level authority and emergency command capability.

See [T.A.R. / A.R.C. autonomy integration](TAR-ARC-AUTONOMY-INTEGRATION.md).

## Sensor concept

Future vehicle studies may fuse:

- redundant IMU / attitude sensing;
- air data;
- propulsion electrical / thermal / magnetic / plasma health;
- local radar;
- EO/IR;
- lidar where useful;
- GNSS + inertial navigation;
- ADS-B / authorized cooperative traffic data;
- terrain and weather data;
- LEO and terrestrial signals-of-opportunity as navigation-resilience inputs.

LEO signals-of-opportunity are not treated as a primary last-second collision sensor.

## Aspirational speed and occupant-load envelope

These are design-study targets, not demonstrated performance:

| Parameter | Working study target |
|---|---:|
| Normal cruise | ~300 mph |
| High-speed cruise | ~350 mph |
| Dash / design study point | ~400 mph |
| Stretch study range | ~450–500 mph |
| Routine maneuver target | ~1.5–2 g |
| Aggressive non-routine study target | ~2.5–3 g |

The control system should favor:

```text
high speed
+ moderate acceleration
+ low jerk
+ large-radius turns
```

The system does not assume any form of inertial cancellation. Occupants experience the acceleration of the vehicle.

## Structure / packaging / safety

Vehicle packaging continues to reserve space and mass for:

- crashworthy occupant structure and restraints;
- battery / HV isolation and containment;
- power electronics;
- high-field magnet structural reaction paths;
- HTS cryogenic equipment if required by the selected field system;
- quench detection / protection;
- thermal management;
- redundant deterministic flight-control hardware;
- emergency egress and whole-aircraft parachute feasibility studies;
- independent essential avionics power.

No assumption is made that one-module-out operation can sustain hover until demonstrated.

## Historical traveling-field vehicle records

Earlier versions of this document and related project files described **traveling-field electromagnetic coil arrays** as the primary propulsion mechanism.

Those records remain part of the research history, but traveling / counter-rotating propulsion fields are now comparison branches rather than requirements of the current vehicle.

The mechanism changed because the project is evidence-gated; the aircraft-scale objective did not.

## Current vehicle conclusion

> **The CRFTE target vehicle is now defined around four distributed P4 Atmospheric Electromagnetic Propulsion modules, not around a requirement for counter-rotating magnetic fields. P4E must first determine whether the underlying low-temperature atmospheric plasma/MHD momentum-transfer physics is efficient and controllable enough to justify scaling.**
