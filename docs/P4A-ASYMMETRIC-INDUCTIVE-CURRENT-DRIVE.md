# CRTFE P4A — Asymmetric Inductive Current Drive

**Date:** 2026-08-25  
**Status:** primary-architecture subbranch / theoretical screening  
**Goal lock:** full-stream atmospheric electromagnetic propulsion; no rotor, propeller, turbine, or plasma-jet substitution

## Why this branch exists

The P4 goal-locked architecture requires a transverse current through a temporarily conductive atmospheric flow inside a strong stationary magnetic field. Direct plasma-contact electrodes create erosion and sheath problems, while dielectric/capacitive current injection accumulates surface charge and requires current commutation.

P4A keeps the same propulsion mechanism but changes only **how the transverse current is driven**:

```text
pre-ionized / transiently conductive full-stream air
        ↓
small fast-changing induction flux
        ↓
closed transverse plasma current loop
        ×
strong stationary HTS B0
        ↓
J × B0 body force on atmospheric working mass
        ↓
neutral-air momentum / aircraft thrust
```

The changing field is not intended to be the propulsion field. It only induces the current. The high-field Lorentz leverage comes from the stationary HTS bias field.

## Relation to known systems

This concept does **not** claim that pulsed inductive plasma acceleration is new. Pulsed inductive thrusters and FARAD already induce plasma current electrodelessly. The important CRTFE distinction under investigation is the separation of roles:

- **known PIT/FARAD family:** the pulsed induction field both induces current and participates directly in the acceleration process, generally in low-pressure / space-propulsion conditions;
- **CRTFE P4A candidate:** separate pre-ionization, large stationary `B0`, and a much smaller asymmetric induction-flux pulse used only to create the transverse current in full atmospheric mass flow.

Patent novelty is not established by this note.

## Governing reduced-order relations

For target thrust `F`, stationary field `B0`, and active volume `V`:

```text
J_avg = F / (B0 V)
```

For pulse repetition rate `f` and useful current-pulse width `tau_f`:

```text
D = f tau_f
J_on = J_avg / D
```

If on-state conductivity is `sigma_on`:

```text
E_ind = J_on / sigma_on
```

For an effective induced-current loop path length `l_loop`:

```text
EMF_loop = E_ind l_loop
```

The fast magnetic-flux change required to provide that loop EMF is approximately:

```text
DeltaPhi = EMF_loop tau_f
DeltaB_drive = DeltaPhi / A_link
```

where `A_link` is the effective transformer-linked area.

The average gas-current Joule loss remains:

```text
sigma_eff = D sigma_on
P_J = F^2 / (B0^2 V sigma_eff)
```

P4A does not evade the effective-conductivity requirement. Its potential benefit is removing plasma-contact electrodes and avoiding the need for a multi-tesla traveling AC propulsion field.

## Representative aircraft-scale screen

Vehicle anchor:

```text
mass = 650 kg
hover thrust = 6.376 kN
active volume = 4.8 m^2 x 0.5 m = 2.4 m^3
pulse rate = 3 kHz
useful conductive/current window = 5 us
D = 0.015
illustrative loop path = 2.0 m
illustrative linked area = 0.10 m^2
```

### 8 T static field, 800 S/m on-state conductivity

```text
J_avg = 332 A/m^2
J_on = 22.1 kA/m^2
E_ind = 27.7 V/m
loop EMF = 55.4 V
required flux swing = 0.277 mWb/pulse
required drive-field swing over 0.10 m^2 = 2.77 mT
sigma_eff = 12 S/m
P_J = 22.1 kW
```

This is the key result of the current screen:

> **A several-tesla time-varying stator field is not required merely to create the transverse current. Under the reduced-order assumptions, a millitesla-scale fast flux swing can provide the needed loop EMF while the stationary 8 T field supplies the Lorentz force.**

### 8 T static field, 300 S/m on-state conductivity

```text
J_on = 22.1 kA/m^2
E_ind = 73.8 V/m
loop EMF = 147.6 V
required drive-field swing = 7.38 mT
sigma_eff = 4.5 S/m
P_J = 58.8 kW
```

### 5 T static field, 800 S/m on-state conductivity

```text
J_avg = 531 A/m^2
J_on = 35.4 kA/m^2
E_ind = 44.3 V/m
loop EMF = 88.6 V
required drive-field swing = 4.43 mT
sigma_eff = 12 S/m
P_J = 56.5 kW
```

The strongest current operating point remains the high-static-field / high-transient-conductivity corner. This does not mean an 8 T aircraft magnet has been shown practical.

## Why asymmetric flux reset matters

A transformer or induction coil cannot accumulate flux indefinitely. The drive flux must reset. If the plasma remains conductive during the reverse flux ramp, the induced current reverses and produces reverse `J x B0` force.

P4A therefore uses an **asymmetric cycle**:

```text
1. create conductive air state
2. fast forward flux ramp -> useful induced current
3. J x B0 transfers momentum to air
4. conductivity collapses / packet advects
5. reset transformer flux while effective conductivity is low
6. repeat
```

For an exponential effective-conductivity decay with time constant `tau_sigma`, a reset beginning after delay `t_d` and lasting `tau_r` gives the approximate reverse-to-forward current-impulse ratio:

```text
r_reset = exp(-t_d/tau_sigma)
          * (tau_sigma/tau_r)
          * [1 - exp(-tau_r/tau_sigma)]
```

Illustrative case:

```text
reset delay = 10 us
reset duration = 50 us
```

Then:

```text
tau_sigma = 0.5 us  -> r_reset ~ 2e-11
tau_sigma = 5 us    -> r_reset ~ 1.35%
tau_sigma = 20 us   -> r_reset ~ 22%
tau_sigma = 100 us  -> r_reset ~ 71%
```

This reveals an important trade:

> A useful microsecond conductivity window is desirable for thrust, but conductivity that persists too strongly into the reset interval creates reverse impulse. The propulsion source therefore needs a **high conductivity impulse with controllable turn-off**, not simply the longest possible plasma lifetime.

## Closed-loop force caveat

A closed current loop in a perfectly uniform magnetic field has zero net magnetic force. P4A therefore requires the **return-current leg to close through a low-field region**, while the force-producing leg lies inside the strong HTS interaction field.

The required geometry is conceptually analogous to a current loop with only one leg inside the high-field gap:

```text
LOW-B RETURN LEG
   ↑          ↓
   |          |
   |   air    |
   |          |
   +-- HIGH-B ACTIVE LEG --> J
          B0 ⊙ / ⊗
          J x B0 -> axial air force
```

The vehicle-mounted magnetic structure receives the equal-and-opposite reaction while the atmospheric working mass carries momentum away. The detailed field/return geometry must be included in the next finite-element model; a uniform-B closed-loop simplification would incorrectly predict usable net force.

## Why this remains CRTFE rather than becoming a different project

P4A preserves all core project goals:

- atmospheric air is the external working mass;
- large mass flow / low induced velocity remains the hover strategy;
- propulsion force is direct electromagnetic `J x B` momentum transfer;
- no mechanical rotor, turbine, propeller, or compressor is introduced;
- ionization and current are electronically timed;
- HTS provides the strong stationary field;
- the architecture remains modular and distributed across the aircraft.

Only the current-injection mechanism changes from capacitive/electrode-style drive to an electrodeless induced loop.

## Literature implications

Relevant adjacent research already establishes several pieces separately:

- pulsed inductive thrusters and FARAD demonstrate electrodeless induction of plasma current and show that separating pre-ionization from acceleration can reduce discharge-energy requirements;
- capacitive-coupled MHD generator work demonstrates that MHD electrical coupling can be performed without conventional exposed electrodes;
- recent DBD research shows surface charge is a primary control variable, reinforcing the value of avoiding wall-charge throughput if an inductive loop can be made to work;
- multi-kHz inductive plasma-thruster switching and partial energy-recovery circuits have already been demonstrated in low-pressure propulsion systems.

None of those facts validates P4A at atmospheric pressure.

## Next theoretical gate

Do **not** build hardware from this note.

The next calculation is a coupled one-cell electromagnetic circuit model containing:

```text
sigma(t)
plasma-loop resistance R_p(t)
plasma-loop inductance L_p
mutual inductance M(t)
primary current / flux ramp
stationary B0 map
return-leg B leakage
J x B0 impulse
Joule heating
flux-reset reverse impulse
HTS AC-field exposure / loss
```

The decisive result is whether the required **millitesla drive flux** remains millitesla after realistic plasma-loop inductance, mutual coupling, Hall conductivity, field penetration, and finite geometry are included.

If that survives, P4A becomes the preferred current-drive implementation of the existing CRTFE P4 architecture. If it does not, the project returns to another current-drive method without changing the propulsion goal.

## Reproducibility

See:

- `tools/asymmetric_inductive_current_drive.py`
- `tools/goal_aligned_synchronous_lorentz.py`
- `docs/SEGMENTED-SYNCHRONOUS-LORENTZ-PULSE-BUDGET-P4.md`
- `docs/PROJECT-GOAL-LOCK-P4.md`
