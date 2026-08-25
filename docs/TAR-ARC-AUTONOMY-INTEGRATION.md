# CRTFE — T.A.R. / A.R.C. Autonomy Integration

**Date:** 2026-08-25  
**Status:** long-range vehicle architecture requirement; not flight-ready software  
**Primary propulsion status:** P4/P4E research remains evidence-gated

## Purpose

CRTFE's long-range vehicle target is now autonomy-first. At high forward speed, millisecond-to-second stabilization and conflict response cannot depend on human reaction alone.

The vehicle therefore uses a layered architecture:

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
CRTFE modules + conventional aerodynamic effectors where present
```

T.A.R. and A.R.C. are not allowed to bypass the independent controller.

## Automation target

The conceptual target is approximately **97% automated routine flight workload**. This is a workload target, not a grant of unrestricted machine authority.

Human responsibility remains at the mission level:

- destination / mission authorization;
- go, hold, reroute, land and abort commands;
- mode selection;
- supervisory override where physically possible.

The autonomy stack handles fast continuous tasks such as:

- stabilization;
- trajectory tracking;
- gust rejection;
- traffic / terrain / weather conflict prediction;
- energy and thermal monitoring;
- navigation-source cross-checking;
- transition management;
- routine approach and landing assistance.

## Sensor-fusion layers

### Fast vehicle-state layer

- IMU / gyros / accelerometers
- air data
- propulsion-module state
- electrical / thermal / magnetic health

### Local perception layer

- radar
- EO/IR
- lidar where useful

### Cooperative/environment layer

- ADS-B or other authorized traffic data
- terrain database
- weather data

### Navigation-resilience layer

- GNSS
- inertial navigation
- LEO signals-of-opportunity
- terrestrial RF signals-of-opportunity where technically and legally appropriate

LEO signals-of-opportunity are not treated as a primary last-second collision sensor.

## High-speed target

The long-range conceptual vehicle may explore **300–500 mph** wingborne operation. These speeds are aspirational design-study points, not validated CRTFE performance.

High speed changes the sensing/control problem because distance traveled per second becomes large:

```text
300 mph ≈ 134 m/s
400 mph ≈ 179 m/s
500 mph ≈ 224 m/s
```

Therefore perception latency, time-to-conflict prediction, turn radius and occupant g/jerk constraints must be built into the digital twin before any high-speed flight claim is made.

## Safety rule

T.A.R. and A.R.C. may recommend a maneuver. The independent flight-safety controller determines whether the maneuver is physically allowed and maps it into bounded control action.

No AI-facing interface should expose raw high-voltage, magnet-current, thrust or control-surface commands as directly executable actions.

## Software bridge

The first bridge implementation is maintained in:

`THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record`

Files:

- `backend/app/tar_arc_bridge.py`
- `backend/app/tar_arc_bridge_api.py`
- `docs/TAR-ARC-FLIGHT-BRIDGE.md`
- `tests/test_tar_arc_bridge.py`

## Grant relevance

The immediate P4E grant experiment does not require autonomous flight. The T.A.R./A.R.C. architecture is included as a **future vehicle integration pathway** demonstrating how a successful plasma/MHD actuator could later be managed safely at high speed.

The grant should remain focused on the falsifiable P4E plasma/MHD experiment rather than claim the full aircraft or autonomy stack is complete.
