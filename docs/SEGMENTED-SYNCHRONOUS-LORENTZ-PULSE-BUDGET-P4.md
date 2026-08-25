# CRTFE P4 — Segmented Synchronous Lorentz Pulse-Budget Screen

**Date:** 2026-08-25  
**Status:** reduced-order theoretical screening  
**Branch:** PRIMARY — full-stream atmospheric electromagnetic propulsion

## Purpose

This calculation stays tied to the original CRTFE goal. It does not replace the project with a plasma jet, neutral-magnetic engine, or chemistry experiment.

The model asks:

> If a segmented plasma cell briefly reaches high conductivity inside a strong stationary magnetic field, how much pulse lifetime, repetition rate and plasma-source energy can the aircraft-scale force budget tolerate?

## Vehicle anchor

```text
mass = 650 kg
hover thrust = 6.376 kN
active area = 4.8 m²
interaction length = 0.5 m
active volume = 2.4 m³
ideal hover fluid-power floor = 148.5 kW
```

The screen provisionally allows **80 kW total** for:

```text
plasma-source power + gas-current Joule loss
```

before magnet, cryogenic, inverter, thermal-management and other system losses.

## Pulse model

Assume each ionization event gives a conductivity waveform

```text
σ(t) = σ_peak exp(-t/τ)
```

and the propulsion electric field is applied only during the useful window `w` after the pulse.

The conductivity impulse used by the drive is:

```text
K_sigma = σ_peak τ [1 - exp(-w/τ)]
```

At repetition rate `f`:

```text
σ_eff = f K_sigma
```

The aircraft-scale reduced-order coupling is then:

```text
F = σ_eff E_drive B V
P_J = F² / (σ_eff B² V)
```

The remaining overhead power defines the largest tolerable plasma-source energy per pulse:

```text
ε_p,max = (P_overhead - P_J) / (V f)
```

This is the quantity that published plasma sources and future detailed chemistry models must beat.

## Representative 5 µs conductive-window cases

### 5 T, 500 S/m peak, 8 kHz

```text
σ_eff ≈ 12.64 S/m
P_J ≈ 53.6 kW
remaining plasma-source allowance ≈ 26.4 kW
max deposited pulse energy density ≈ 1.37 J/m³/pulse
max whole-active-volume pulse energy ≈ 3.30 J/pulse
```

This is a narrow result: the electromagnetic part nearly closes, but the plasma source would have to produce a 500 S/m, ~5 µs useful state over the effective active volume for only a few joules per synchronized event.

### 5 T, 800 S/m peak, 8 kHz

```text
σ_eff ≈ 20.23 S/m
P_J ≈ 33.5 kW
remaining plasma-source allowance ≈ 46.5 kW
max deposited pulse energy density ≈ 2.42 J/m³/pulse
max whole-active-volume pulse energy ≈ 5.81 J/pulse
```

Higher peak conductivity improves the electromagnetic loss margin, but does not automatically make the plasma source practical. The energy needed to create the assumed waveform is still the decisive unknown.

### 8 T, 500 S/m peak, 5 kHz

```text
σ_eff ≈ 7.90 S/m
P_J ≈ 33.5 kW
remaining plasma-source allowance ≈ 46.5 kW
max deposited pulse energy density ≈ 3.87 J/m³/pulse
max whole-active-volume pulse energy ≈ 9.30 J/pulse
```

### 8 T, 800 S/m peak, 3 kHz

```text
σ_eff ≈ 7.59 S/m
P_J ≈ 34.9 kW
remaining plasma-source allowance ≈ 45.1 kW
max deposited pulse energy density ≈ 6.26 J/m³/pulse
max whole-active-volume pulse energy ≈ 15.0 J/pulse
```

Of the screened cases, the stronger static field gives the plasma source the largest per-pulse energy allowance while keeping the same full-stream force objective.

## What the simulation says about the original concept

### 1. The project does not require continuously high conductivity if the pulse is strong enough

The correct reduced-order quantity is the **conductivity impulse** and its repetition rate, not peak conductivity by itself.

A few-microsecond useful window at several hundred S/m can mathematically reproduce a several-S/m effective conductivity at low-kHz repetition rates.

This is much closer to the original ionize-and-push concept than the broad P3 program that tried to make the whole duct continuously conductive.

### 2. Nanosecond-only conductivity remains difficult

If the same peak state lasts only ~50 ns instead of ~5 µs, required repetition rate rises by about two orders of magnitude. The electromagnetic equations still work, but plasma-source and switching power become much harder.

Therefore the near-term theoretical target is:

> **find or engineer a post-pulse conducting state in the microsecond range without paying thermal-ionization energy for the whole air stream.**

That can come from afterglow chemistry, detachment, metastables or another non-equilibrium mechanism—but only as a subsystem serving the main Lorentz duct.

### 3. Strong static field is still one of the highest-leverage variables

Moving from 5 T to 8 T materially reduces required `σ_eff` and increases the plasma-energy allowance. However, field strength cannot be optimized independently of:

- HTS mass;
- stored energy;
- structural magnetic stress;
- quench protection;
- cryogenic power;
- interaction-volume field coverage.

P4 therefore needs a **force-per-installed-magnet-mass** model next, not simply a higher `B` target.

### 4. Segmentation is retained for the right reason

Segmenting the duct does not create free force. Its value is:

- synchronize plasma creation with current;
- keep force direction positive;
- minimize powered plasma volume at any instant;
- permit resonant/capacitive energy recovery;
- manage sheath and surface charge;
- distribute heat;
- phase the interaction with moving air.

That keeps the design conceptually close to an electronic linear motor acting directly on air.

## Current primary architecture

```text
FULL ATMOSPHERIC MASS FLOW
        ↓
segmented short-lived non-equilibrium conductivity
        ↓
transverse synchronized current
        ×
strong stationary HTS magnetic field
        ↓
J × B body-force impulse
        ↓
neutral-air momentum
        ↓
large-area low-velocity thrust
```

No rotor, propeller or mechanical compressor is introduced by this reengineering.

## Next model

The next goal-aligned model should couple one cell's:

```text
plasma source energy
σ(t)
current waveform
surface/sheath charging
J × B force
neutral momentum transfer
gas temperature
recovered reactive electrical energy
```

and then tile that verified cell across the four-module aircraft geometry.

The experimental question will only be frozen after that calculation identifies a narrow measurable parameter that published data cannot supply.

## Reproducibility

See:

- `tools/goal_aligned_synchronous_lorentz.py`
- `tools/segmented_cell_pulse_budget.py`
- `docs/PROJECT-GOAL-LOCK-P4.md`
