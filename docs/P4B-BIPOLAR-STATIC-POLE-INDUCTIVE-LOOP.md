# CRTFE P4B — Bipolar Static-Pole Inductive Plasma Loop

**Date:** 2026-08-25  
**Status:** reduced-order simulation candidate inside the primary CRTFE architecture  
**Goal lock:** full-stream atmospheric electromagnetic propulsion; no rotor/propeller/turbine substitution

## Why this branch exists

P4A showed that using a small time-varying drive field to induce plasma current while a large stationary HTS field supplies the propulsion Lorentz force can remove the requirement for a multi-tesla traveling magnetic field.

The first P4A resistive-only estimate, however, understated the drive requirement because a real plasma current loop has inductance. A 5 microsecond pulse that must build kiloampere current is governed by

```text
L dI/dt + R I = V_induced
```

not just `V = I R`.

P4B changes only the magnetic/current geometry, not the project goal.

## P4B topology

Use two adjacent stationary HTS pole regions with opposite field polarity:

```text
       +Bz pole             -Bz pole
      ┌────────┐           ┌────────┐
J --> │ plasma │           │ plasma │ <-- J
      │  leg A │           │  leg B │
      └────────┘           └────────┘
            \_______________/
              closed induced
               plasma loop
```

The current reverses in the second transverse leg because it is a closed loop. The magnetic field also reverses. Therefore the axial Lorentz force keeps the same sign:

```text
leg A:   (+Jy) x (+Bz) -> +Fx
leg B:   (-Jy) x (-Bz) -> +Fx
```

Both legs contribute thrust.

This also allows the current loop to remain geometrically compact, reducing plasma-loop inductance compared with a design that sends the return leg far outside the magnetic field.

## Force relation

For one module with transverse leg length `l`, pulse repetition `f` and identical `|B|` under each pole,

```text
F_module = 2 B l f integral(I(t) dt)
```

For the 650 kg / four-module vehicle baseline:

```text
total hover thrust = 6.376 kN
thrust/module = 1.594 kN
B = 8 T
l = 1.0 m
f = 3 kHz
```

required current impulse per pulse per module is approximately

```text
integral(I dt) = 0.0332 A*s
```

which is half the single-active-leg value.

## Representative geometry screen

The screening model uses:

```text
module height = 1.2 m
transverse leg length = 1.0 m
each +B/-B pole length = 0.25 m
conductive cross section per transverse leg ~ 1.2 x 0.25 = 0.30 m^2
linked drive area = 0.10 m^2
pulse = 5 us
repetition = 3 kHz
```

A broad paired-sheet estimate is used for plasma-loop inductance:

```text
L_loop ~ kL mu0 d l / h
```

with `kL = 1.5` as a screening allowance for closure/fringe effects. This gives about

```text
L_loop ~ 0.39 uH
```

for the 0.25 m pole spacing/length scale.

Resistance is modeled as two broad plasma legs plus a connector penalty:

```text
R_loop ~ kR 2 l / (sigma h d)
```

with `kR = 1.2`.

These are not detailed 3D field solutions.

## 8 T simulation results, 3 kHz, 5 us, 98% recovery

| On-state conductivity | Loop R | Loop L | Drive pulse | Equivalent linked drive-field swing | End current | Joule loss | 2% unrecovered loop-field energy | Total EM overhead |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 S/m | 80.0 mOhm | 0.39 uH | 1.43 kV | 71 mT | 11.4 kA | 263 kW | 6 kW | 269 kW |
| 300 S/m | 26.7 mOhm | 0.39 uH | 1.16 kV | 58 mT | 12.6 kA | 92 kW | 7 kW | 99 kW |
| **800 S/m** | **10.0 mOhm** | **0.39 uH** | **1.09 kV** | **54 mT** | **13.0 kA** | **35 kW** | **8 kW** | **43 kW** |
| 1500 S/m | 5.33 mOhm | 0.39 uH | 1.07 kV | 53 mT | 13.1 kA | 19 kW | 8 kW | 27 kW |

The drive-field number above is the equivalent flux swing `Delta Phi / A_link`; it is not a claim that a uniform 54 mT field can actually be produced with a practical coil geometry at the required repetition rate.

## Main result

The original P4A statement that only a few millitesla of drive field might be needed was too optimistic because it neglected `L dI/dt`.

With a realistic sub-microhenry current loop, the drive requirement moves into approximately:

```text
~1 kV induced loop EMF
~50 mT linked flux swing
~13 kA pulse current per module
```

for the representative 8 T / 800 S/m case.

That is still dramatically smaller than making the main multi-tesla propulsion field travel at kilohertz rates.

## Inductance sensitivity

At approximately 10 mOhm loop resistance in the same 8 T case:

```text
L = 0.05 uH -> ~0.18 kV drive, ~9 mT linked swing
L = 0.10 uH -> ~0.31 kV drive, ~16 mT linked swing
L = 0.30 uH -> ~0.84 kV drive, ~42 mT linked swing
L = 0.50 uH -> ~1.37 kV drive, ~69 mT linked swing
L = 1.00 uH -> ~2.70 kV drive, ~135 mT linked swing
L = 3.00 uH -> ~8.0 kV drive, ~401 mT linked swing
```

The P4A/P4B architecture therefore has a hard geometry requirement:

> **keep the induced plasma loop in the sub-microhenry regime.**

Multi-microhenry loops erase much of the benefit.

## Conductivity threshold

For the representative `8 T / 0.39 uH / 3 kHz / 5 us / 98% recovery` point, the electromagnetic overhead alone is approximately:

```text
~80 kW at sigma_on ~ 382 S/m
~50 kW at sigma_on ~ 662 S/m
~40 kW at sigma_on ~ 874 S/m
```

Therefore P4B does **not** eliminate CRTFE's plasma challenge.

It changes the challenge from continuously maintaining 60–150 S/m across the entire duct to producing a much higher but short-lived conductivity state in broad, low-inductance current sheets while keeping plasma-source energy low enough to fit the aircraft budget.

## Remaining system constraint

The static HTS field is still the largest installed-field burden. At 8 T, magnetic energy density / Maxwell pressure scale is

```text
B^2/(2 mu0) ~ 25.5 MJ/m^3 = 25.5 MPa
```

P4B does not solve magnet mass, structural stress, quench protection, cryogenic load or field-volume packaging. It only reduces the **time-varying** field requirement.

## Prior-art position

Inductive MHD accelerators and pulsed inductive plasma thrusters already use transformer-like coupling between a drive circuit and plasma. Historical induction-MHD work also used induced eddy currents. Alternating-polarity static magnetic arrays are common elsewhere in plasma physics.

This note therefore makes **no novelty claim** for the ingredients. The candidate distinction to investigate is their specific integration:

```text
full-stream atmospheric air
+ short-lived distributed conductivity
+ low-inductance closed plasma current loops
+ adjacent opposite-polarity stationary high-B poles
+ small pulsed transformer drive field
+ same-direction JxB force from both loop legs
```

A formal patent/literature search is required before any novelty statement.

## Decision after this simulation

P4B remains inside the primary CRTFE branch because it preserves:

- atmospheric air as working mass;
- no rotating propulsion machinery;
- direct electromagnetic body-force transfer;
- pulsed pre-ionization/conductivity;
- stationary strong HTS magnetic field;
- large-area, low-exhaust-velocity vehicle goal.

It should replace neither the project goal nor the evidence gates.

## P4C primary-driver follow-up

P4C now adds the capacitor, primary inductance/resistance, mutual coupling and plasma-loop `L/R` dynamics instead of assuming an ideal induced-voltage source.

The representative `20 uF / L1=1 uH / L2=0.39 uH / k=0.8` circuit reproduced the target force impulse with approximately:

```text
~1.14 kV initial capacitor voltage
~7.7 kA primary peak
~9.2 kA plasma-loop peak
~13 J initial pulse energy/module
~40 kW four-module electromagnetic loss at 98% recovery
```

for a constant 10 mOhm plasma loop during a 5 us pulse.

When plasma resistance is allowed to increase with a 5 us conductivity-decay time, a ~7–7.5 us forward pulse followed by clamping before current reversal is electrically better than forcing a 5 us pulse. The representative 7.5 us screen requires roughly:

```text
~0.95 kV initial capacitor voltage
~6.0 kA primary peak
~7.0 kA plasma peak
~52 kW four-module electromagnetic loss at 98% recovery
```

The free-running RLC pulse must not be allowed to reverse plasma current under fixed static poles, because that would create reverse thrust. P4C therefore requires pulse interruption/clamping plus energy recovery/reset during low conductivity.

See `docs/P4C-COUPLED-PRIMARY-PLASMA-DRIVER.md` and `tools/p4c_coupled_primary_plasma_driver.py`.

## Next simulation

The next useful model couples the P4C circuit directly to the plasma source and flow:

```text
plasma-source energy
sigma(t) / Rp(t)
primary-secondary circuit
JxB impulse
neutral momentum transfer
gas heating
```

The gating question is no longer only whether the transformer works. It is whether the required conductivity impulse can be purchased cheaply enough that **total propulsion electrical power**, including plasma generation, remains competitive with the aerodynamic power floor.

## Reproducibility

See:

- `tools/bipolar_static_pole_inductive_loop.py`
- `tools/asymmetric_inductive_current_drive.py`
- `tools/p4c_coupled_primary_plasma_driver.py`
- `docs/P4C-COUPLED-PRIMARY-PLASMA-DRIVER.md`
- `docs/P4A-ASYMMETRIC-INDUCTIVE-CURRENT-DRIVE.md`
- `docs/PROJECT-GOAL-LOCK-P4.md`
