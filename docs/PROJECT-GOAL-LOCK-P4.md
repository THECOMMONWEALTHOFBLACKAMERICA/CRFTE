# CRTFE Project Goal Lock — P4 Theoretical Reengineering

**Date:** 2026-08-25  
**Status:** active theoretical design review  
**Purpose:** Prevent useful side research from displacing the original CRTFE objective.

## 1. Original goal remains unchanged

CRTFE is still pursuing a **large-area, no-moving-parts atmospheric electromagnetic propulsion system** intended ultimately for a two-person VTOL/wingborne research aircraft.

The core physical objective is still:

> transfer electromagnetic momentum directly into a large atmospheric-air mass flow without conventional rotors, propellers, turbines or mechanical compressors.

The current target vehicle remains the 650 kg / four-module / 4.8 m² active-area concept unless later vehicle engineering changes it.

## 2. What is now considered the primary branch

The main theoretical branch is a **full-stream segmented synchronous Lorentz duct**:

1. atmospheric air enters the active duct;
2. a strong **stationary magnetic field** is established by HTS or another high-field system;
3. ionization/conductivity is produced only as required;
4. a transverse electric/current drive is synchronized with the conductive state;
5. the resulting `J × B` body force accelerates the same large neutral-air stream needed for efficient hover;
6. segmented cells distribute the interaction through the duct without requiring the entire multi-tesla field to travel.

The important architecture correction is that the static HTS field and the traveling/polyphase field are not interchangeable. P4 therefore does **not** assume the old V5 `B²` relation can substitute a DC bias field for a traveling magnetic field.

## 3. Goal-aligned reduced-order force model

For the synchronous static-field branch:

```text
F = D σ_on E_drive B_static V
σ_eff = D σ_on
P_J = F² / (σ_eff B_static² V)
```

where:

- `D` is the local conductive/current duty factor;
- `σ_on` is conductivity while the plasma cell is active;
- `σ_eff = D σ_on` is the time-averaged effective conductivity relevant to the reduced-order force/power balance;
- `B_static` is the usable static field in the interaction volume;
- `V = A L` is active fluid volume.

Segmentation is useful for timing, field direction, plasma localization and commutation, but **segmentation alone does not remove the average `D σ_on` requirement**.

## 4. Current 650 kg vehicle anchor

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

This actuator-disk floor remains the non-negotiable vehicle anchor.

## 5. Conductivity requirement after the static-field correction

If we provisionally permit **50 kW total Joule/slip loss** in the active gas, the reduced-order effective-conductivity requirement becomes:

| Static field | Required `σ_eff = D σ_on` |
|---:|---:|
| 3 T | ~37.6 S/m |
| 5 T | ~13.6 S/m |
| 8 T | ~5.3 S/m |

This is a better engineering target than the old blanket 60–150 S/m rule.

The project should therefore no longer chase peak conductivity alone. It should seek the best combination of:

```text
B_static
× conductivity impulse
× low plasma-source energy
× installed field-system mass
```

## 6. Pulsed conductivity can remain project-aligned

Published atmospheric nanosecond plasmas can briefly reach much higher instantaneous carrier density than the effective conductivity required by the table above. P4 therefore keeps pulsed conductivity as a core mechanism, provided it is used to support the **same full-stream Lorentz duct**, not to turn CRTFE into a small plasma-jet engine.

For periodic pulses:

```text
σ_eff = f × K_sigma
K_sigma = integral[σ(t) dt] per pulse
```

If each pulse approximates conductivity `σ_peak` for a useful window `t_on`:

```text
D = σ_eff / σ_peak
f = D / t_on
```

Representative cadence for the 50-kW Joule-loss target:

### 5 T static field

`σ_eff ≈ 13.6 S/m`

- `σ_peak = 500 S/m`, `t_on = 5 µs` -> ~5.4 kHz
- `σ_peak = 800 S/m`, `t_on = 5 µs` -> ~3.4 kHz
- if `t_on = 50 ns`, those rates rise into hundreds of kHz

### 8 T static field

`σ_eff ≈ 5.3 S/m`

- `σ_peak = 500 S/m`, `t_on = 5 µs` -> ~2.1 kHz
- `σ_peak = 800 S/m`, `t_on = 5 µs` -> ~1.3 kHz
- if `t_on = 50 ns`, rates remain ~130–210 kHz

### Design implication

The goal is **not necessarily millisecond plasma lifetime**. A microsecond-scale high-conductivity window may be useful if:

1. pulse energy is low enough;
2. repetition frequency is practical;
3. the current can be commutated into the correct direction;
4. the resulting momentum is transferred into the neutral full stream;
5. heating remains acceptable.

## 7. The new plasma figure of merit

Define the conductivity impulse per pulse:

```text
K_sigma = integral[σ(t) dt]
```

and deposited plasma-source energy density per pulse:

```text
ε_p = J/m³ per pulse
```

Then define:

```text
R_p = ε_p / K_sigma
```

Lower `R_p` is better.

For periodic pulsing:

```text
P_plasma+Joule
  = F²/(B² V σ_eff)
  + V σ_eff R_p
```

Optimizing over `σ_eff` gives:

```text
P_extra,min = (2F/B) sqrt(R_p)
```

This is now the **primary plasma-source screening metric**.

It directly answers the project question:

> how much useful conductivity-time can a plasma source buy per joule?

For no more than ~80 kW optimized plasma + Joule overhead at the current 6.38 kN thrust target, the approximate upper limits are:

| Static field | Required `R_p` or better |
|---:|---:|
| 3 T | <= ~354 (V/m)² |
| 5 T | <= ~984 (V/m)² |
| 8 T | <= ~2,518 (V/m)² |

These are reduced-order screening numbers, not validated acceptance criteria.

## 8. Branch ranking — prevent project drift

### PRIMARY — keep developing

**Full-stream segmented synchronous Lorentz duct**

- strong stationary magnetic field;
- pulsed/distributed conductivity;
- transverse current/electric field;
- direct `J × B` momentum transfer to the full atmospheric stream;
- no conventional moving propulsion parts.

This remains closest to the original CRTFE concept and vehicle goal.

### COMPARISON BRANCH — retain

**V5 traveling-field induction MHD**

Keep as a reference solution, but repair the electromagnetic model so the amplitude of the traveling field is not confused with the static HTS bias field.

### SUPPORTING RESEARCH — useful only if it improves PRIMARY

- carrier-memory chemistry;
- negative-ion / metastable pre-ionization;
- capacitive/electrodeless current coupling;
- resonant recovery of reactive electrode energy;
- high-field magnet topology;
- Hall/tensor conductivity modeling.

These are subsystem solutions, not new project goals.

### SCREENING ONLY — do not steer CRTFE toward them

- small high-speed plasma driver with neutral-air ejector;
- bulk O2 chemical conditioning of the whole hover stream;
- neutral paramagnetic O2 propulsion as the primary vehicle mechanism.

They remain documented because they reveal limits or possibly useful subsystem effects, but they do not replace the original propulsion concept.

## 9. What must be solved before another lab pitch

The next theoretical deliverable is not another broad plasma experiment. It is a coupled cell model that computes:

```text
plasma pulse -> sigma(t)
             -> current waveform J(t)
             -> J x B impulse
             -> neutral-air momentum gain
             -> gas heating
             -> surface/sheath charge
             -> circuit energy recovery
             -> next cell
```

The model must use the same target force and mass-flow conditions as the vehicle so subsystem optimization cannot drift away from the mission.

## 10. Program rule

> **CRTFE side research is retained only when it improves the probability, power, mass, control or evidence quality of the full-stream atmospheric electromagnetic propulsion architecture.**

The target is still the aircraft-scale propulsion mechanism—not plasma physics for its own sake.
