# CRFTE Project Goal Lock — P4 Atmospheric Electromagnetic Propulsion

**Date:** 2026-08-25  
**Status:** active theoretical design review  
**Purpose:** preserve the vehicle objective while allowing the propulsion mechanism to change when modeling or experiments require it.

## 1. Program identity versus mechanism

CRFTE is the program identifier. It originated from the historical name **Counter-Rotating Field Thrust Engine**.

The current P4 architecture is **not** defined by counter-rotating magnetic fields. The program has evolved toward a full-stream Lorentz/MHD mechanism using controlled atmospheric-air conductivity, transverse current and a predominantly stationary magnetic field.

See [CRFTE Name and Architecture Lineage](CRFTE-NAME-AND-ARCHITECTURE-LINEAGE.md).

## 2. Goal remains unchanged

CRFTE is pursuing a **large-area, no-moving-parts atmospheric electromagnetic propulsion system** intended ultimately for a two-person VTOL / wingborne research aircraft.

The core physical objective remains:

> transfer electromagnetic momentum directly into a large atmospheric-air mass flow without conventional rotors, propellers, turbines or mechanical compressors.

The current target vehicle remains the 650 kg / four-module / 4.8 m² active-area concept unless later vehicle engineering changes it.

## 3. Current primary branch — P4 Atmospheric Electromagnetic Propulsion

The main theoretical branch is a **full-stream segmented Lorentz interaction**:

1. atmospheric air enters the active region;
2. a strong predominantly **stationary magnetic field** is established by HTS or another high-field system;
3. ionization / conductivity is produced only as required;
4. a transverse electric/current drive is synchronized with the conductive state;
5. the resulting `J × B` body force accelerates the same large neutral-air stream needed for efficient hover and forward propulsion;
6. segmented cells distribute and commutate the interaction without requiring the entire multi-tesla propulsion field to rotate or travel.

This architecture deliberately separates the large propulsion field from smaller pulsed/inductive fields that may be used to establish or shape current.

## 4. Goal-aligned reduced-order force model

For the synchronous static-field branch:

```text
F = D σ_on E_drive B_static V
σ_eff = D σ_on
P_J = F² / (σ_eff B_static² V)
```

where:

- `D` is the local conductive/current duty factor;
- `σ_on` is conductivity while the plasma cell is active;
- `σ_eff = D σ_on` is the effective conductivity relevant to the reduced-order force/power balance;
- `B_static` is the usable stationary field in the interaction volume;
- `V = A L` is active fluid volume.

Segmentation helps timing, field direction, plasma localization and commutation, but does not eliminate the average conductivity requirement.

## 5. Current 650 kg vehicle anchor

Using:

```text
m = 650 kg
A = 4.8 m²
L = 0.5 m
V = 2.4 m³
rho = 1.225 kg/m³
```

we retain:

```text
hover thrust ≈ 6.38 kN
ideal induced velocity ≈ 23.3 m/s
ideal fluid-power floor ≈ 148.5 kW
```

This actuator-disk floor remains a non-negotiable vehicle reference. It is not a demonstrated electrical-power result.

## 6. Conductivity screening target

If 50 kW total Joule/slip loss is provisionally allowed in the active gas, the reduced-order effective-conductivity requirement is approximately:

| Static field | Required `σ_eff = D σ_on` |
|---:|---:|
| 3 T | ~37.6 S/m |
| 5 T | ~13.6 S/m |
| 8 T | ~5.3 S/m |

The project therefore screens combinations of:

```text
B_static
× conductivity-time integral
× low plasma-source energy
× installed field-system mass
```

rather than chasing peak conductivity alone.

## 7. P4A / P4B / P4C current-drive refinements

P4A–P4C investigate ways to produce the required transverse current without making the large propulsion magnetic field itself rotate.

- **P4A:** asymmetric inductive current drive;
- **P4B:** adjacent opposite-polarity static magnetic poles combined with a closed plasma-current loop;
- **P4C:** coupled primary / plasma-loop driver with controlled energy recovery and clamping.

The smaller changing field used to induce current is not the main propulsion field.

## 8. P4D / P4E plasma validation path

P4D investigates high-PRF nanosecond ionization and RF vibrational conditioning as a route to useful conductivity-time at acceptable plasma-source energy.

P4E is the current **grant-scale proof-of-physics experiment**. It is not the finished vehicle engine. Its purpose is to determine whether the plasma/MHD mechanism can produce controlled, polarity-reversible Lorentz momentum transfer efficiently enough to justify further P4 scaling.

## 9. Historical / comparison branches

### HISTORICAL OR COMPARISON

**Counter-rotating and traveling-field concepts**

These mechanisms remain part of the research record and may be revisited if a quantitative model demonstrates a real force, power, mass, stability or control advantage.

They are not current P4 design requirements.

### RETAINED COMPARISON

**V5 traveling-field induction MHD**

Retained as a comparison model. Its traveling-field amplitude must never be confused with the stationary HTS bias field used by P4.

### SUPPORTING RESEARCH

- carrier-memory chemistry;
- negative-ion / metastable pre-ionization;
- capacitive/electrodeless current coupling;
- resonant recovery of reactive energy;
- high-field magnet topology;
- Hall/tensor conductivity modeling.

These are subsystem studies, not replacements for the program goal.

## 10. What must be solved before vehicle-scale claims

The coupled model must compute:

```text
plasma pulse -> sigma(t)
             -> current waveform J(t)
             -> J x B impulse
             -> neutral-air momentum gain
             -> gas heating
             -> circuit / field-system losses
             -> control response
```

The model must use the same target force, active area and mass-flow conditions as the vehicle so subsystem optimization cannot drift away from the mission.

## 11. Program rule

> **CRFTE keeps the aircraft-scale atmospheric-electromagnetic propulsion objective fixed while allowing the proposed mechanism to change when quantitative evidence demands it. The current mechanism is P4 atmospheric electromagnetic propulsion, not a requirement for counter-rotating magnetic fields.**
