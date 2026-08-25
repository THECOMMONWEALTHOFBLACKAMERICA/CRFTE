# CRTFE Comparative Research Review — Synchronous Conductivity / Pulsed Lorentz Entrainment Branch

**Status:** Candidate theoretical branch — not a frozen architecture  
**Date:** 2026-08-25

## Why this branch exists

A literature and prior-art review shows that many elements previously treated as potential CRTFE novelty already have substantial precedent:

- traveling magnetic fields accelerating conducting fluid (NASA, 1965)
- one-atmosphere glow-discharge plasma with polyphase traveling electrostatic acceleration (University of Tennessee / NASA Langley)
- weakly ionized neutral-gas acceleration by a traveling electrostatic wave
- weakly ionized plasma accelerated under static magnetic field with momentum transferred to neutrals by ion-neutral collisions
- capacitive / electrodeless MHD power coupling
- air-breathing plasma propulsion and self-neutralized atmospheric plasma thrusters
- rotating/translating magnetic-field plasma propulsion with charge exchange
- MHD bypass/ejector propulsion concepts

CRTFE therefore should not claim novelty for any one of those mechanisms by itself.

The candidate differentiator investigated here is a combined architecture in which **conductivity is the actively commutated element** rather than requiring a continuously conductive duct or a large traveling magnetic field.

## Closest known neighboring concepts

### NASA traveling magnetic-field accelerator

Willis H. Braun, NASA TN D-3006 (1965), analyzed acceleration of a conducting fluid by a traveling magnetic field. This establishes the classical linear-induction MHD precedent.

Reference: https://ntrs.nasa.gov/citations/19650023946

### One-atmosphere peristaltic plasma acceleration

Roth and collaborators demonstrated one-atmosphere glow-discharge plasma actuators and polyphase traveling electrostatic fields that accelerate ions and transfer momentum to neutral air. Early neutral-flow speeds of several m/s were experimentally demonstrated, with larger values theoretically projected.

References:
- https://doi.org/10.1063/1.1564823
- https://voljournals.utk.edu/utk_gradthes/5997/
- https://patents.google.com/patent/US5669583A/en

### Traveling electrostatic-wave neutral acceleration

Lee, Lee and Wong (2018) modeled a weakly ionized gas in which charged species are trapped/accelerated by a traveling electrostatic wave and neutrals are accelerated through ion-neutral collisions. The paper explicitly discusses air/glider propulsion among possible applications.

Reference: https://doi.org/10.1063/1.5013075

### Weakly ionized gas + static magnetic field + neutral coupling

Wong, Lee and Lee (2024) modeled weakly ionized gas with a driven current and static magnetic field. Charged particles receive Lorentz acceleration and transfer momentum to neutrals through ion-neutral collisions.

Reference: https://doi.org/10.1063/5.0168396

### Capacitive Hall MHD coupling

A 2023 experiment demonstrated capacitively coupled Hall-type MHD generation and waveforms consistent with theory, providing direct precedent that dielectric/capacitive interfaces can participate in MHD energy conversion without a conventional immersed-electrode arrangement.

Reference: https://doi.org/10.1541/ieejpes.143.303

### Atmospheric / weak-plasma magnetic-propulsion prior art

US12209576B2 / WO2021194572A2 describes rotating and translating magnetic-field propulsion in weakly ionized media, artificial ionization in otherwise neutral atmospheres, ion-neutral/charge-exchange momentum transfer, and auxiliary static magnetic fields.

References:
- https://patents.google.com/patent/US12209576B2/en
- https://patents.google.com/patent/WO2021194572A2/en

### DARPA Charge Harmony

DARPA Charge Harmony explored self-neutralized air-breathing plasma propulsion using atmospheric air at approximately 70–90 km altitude.

Reference: https://www.darpa.mil/research/programs/charge-harmony

## The overlooked physical point

CRTFE has previously treated plasma persistence across a long interaction duct as a primary requirement.

That may be unnecessarily restrictive.

At atmospheric pressure, charged particles exchange momentum with neutral gas through frequent collisions. Once electromagnetic momentum has been transferred from the charged minority to the neutral majority, the neutral gas can carry that momentum downstream even after electrons attach/recombine and the local electrical conductivity collapses.

Therefore the key timescale requirement may not be:

```text
tau_plasma >= L_channel / u
```

Instead it may be closer to:

```text
tau_plasma >= max(tau_current_establishment, tau_charge-neutral momentum transfer)
```

with repeated local re-ionization along the flow path.

This converts short plasma lifetime from a pure disadvantage into a possible **electronic commutation mechanism**.

## Candidate CRTFE architecture

Working description:

> **Synchronous Conductivity MHD / Pulsed Lorentz Entrainment**

The conceptual sequence is:

1. a strong **static** magnetic field occupies a local interaction cell;
2. a short ionization pulse creates a temporary conductive packet in the cell;
3. a separately controlled, lower-field propulsion electric/current drive produces current transverse to the static magnetic field;
4. `J x B` accelerates the charged population;
5. ion/electron-neutral collisions transfer momentum into the neutral atmospheric gas;
6. the local plasma is allowed to decay;
7. the neutral flow retains the momentum;
8. the next downstream cell repeats the impulse.

This is fundamentally different from requiring one continuously conductive 0.5 m plasma volume.

## Separation of ionization field and propulsion field

A major design principle is to separate two jobs that previous reduced-order CRTFE models implicitly mixed:

### Ionization field

High-field, short-duration pulse used to create charge carriers.

### Propulsion current field

Lower field used to drive current while conductivity exists.

The ionization field therefore does not need to be the same electric field that determines the Lorentz-force Ohmic penalty.

For the propulsion interval:

```text
f = J x B
J ~= sigma_on E_drive
```

while the high-field ionization pulse is accounted separately in auxiliary power.

## Pulsed duty-cycle model

Let:

- `F` = required time-averaged force
- `D` = conductive duty cycle
- `sigma_on` = conductivity during the active plasma state
- `B` = static magnetic flux density
- `V` = active interaction volume
- `E` = propulsion electric field during the active state

For an idealized unidirectional active interval:

```text
F = D sigma_on E B V
```

so

```text
E = F / (D sigma_on B V)
```

and the average propulsion-current Joule loss is

```text
P_J = D sigma_on E^2 V
    = F^2 / (D sigma_on B^2 V)
```

This is important: reducing duty cycle reduces plasma-maintenance time but raises required instantaneous current/electric field and increases the propulsion-current Joule term as `1/D`.

Assume an on-state ionization/maintenance power density `p_i` so that

```text
P_i = D p_i V
```

Then the simplified auxiliary-power objective is

```text
P_aux(D) = F^2/(D sigma_on B^2 V) + D p_i V
```

which has an interior optimum at

```text
D* = F / (B V sqrt(sigma_on p_i))
```

when `0 < D* < 1`.

The corresponding minimum of these two terms is

```text
P_aux,min = (2 F / B) sqrt(p_i / sigma_on)
```

This creates a new CRTFE design problem: **optimize pulsed conductivity rather than maximize persistence.**

## Why this may matter

Published atmospheric-pressure nanosecond discharges can generate high instantaneous electron densities for very short periods. A pulsed architecture may exploit the high `sigma_on` state only while it is useful, rather than paying to sustain it continuously.

The architecture is attractive only if:

- current establishes rapidly enough during the plasma pulse;
- charged-neutral momentum transfer is fast compared with the active interval;
- real ionization energy per pulse is low enough;
- surface charging / sheath behavior does not block the desired current;
- current closure is physically realizable;
- the static magnetic system has acceptable mass, stored energy and cryogenic burden;
- repeated impulses sum to the required neutral-flow momentum without excessive heating.

## Capacitive/electrodeless current coupling challenge

A purely dielectric/capacitive transverse drive cannot be assumed to support indefinite DC conduction through the plasma. Surface charge and sheath formation must be included.

Two possible commutation families should be modeled rather than assumed:

### A. Plasma-on conduction / displacement-current reset

A short conductive pulse transfers charge and momentum during the thrust-producing interval. The external resonant network then restores electrode/dielectric charge primarily through displacement current while plasma conductivity is low.

### B. Alternating static-field polarity cells

Adjacent interaction cells use opposite static `B` polarity. Conductivity/current timing is selected so alternating current directions still produce the same axial `J x B` direction. This may provide charge-balanced operation without requiring a traveling high-field magnet.

Both are hypotheses requiring Maxwell/circuit/plasma validation.

## Magnetic-volume reengineering

The vehicle should not assume a uniform multi-tesla field throughout the entire large duct volume.

A potentially better architecture is a tiled set of short, high-field interaction gaps with local magnetic return paths. The relevant optimization quantity is not simply `B_max`, but useful electromagnetic interaction per magnet-system mass, for example:

```text
M_metric = integral(sigma B^2 dV) / m_magnet+cryo
```

or, for imposed current,

```text
J_metric = integral(J B dV) / m_magnet+cryo
```

The static-field geometry should be co-designed with the pulse cells rather than inherited from the V5 vehicle envelope.

## Neutral momentum — not plasma persistence — becomes the stored state

The key conceptual reframe is:

```text
OLD:
create plasma -> keep plasma conductive -> accelerate plasma over long distance

CANDIDATE:
create plasma -> deliver short electromagnetic impulse -> transfer impulse to neutrals -> allow plasma to die -> repeat downstream
```

The state that persists is **neutral-gas momentum**, not electron density.

## Novelty boundary

This review does **not** establish patent novelty.

Known prior art already covers important neighboring elements including:

- traveling magnetic fluid accelerators;
- one-atmosphere peristaltic plasma/EHD acceleration;
- traveling electrostatic-wave weakly ionized-gas propulsion;
- static-B Lorentz acceleration with neutral coupling;
- capacitive Hall MHD generation;
- translating/rotating magnetic-field atmospheric plasma propulsion;
- conductivity waves in induction MHD generators.

The candidate differentiator that remains worth a dedicated prior-art search is the exact integration of:

1. **atmospheric weak-ionization pulses,**
2. **separate low-field propulsion-current drive,**
3. **strong static magnetic interaction cells,**
4. **conductivity used as a phase/duty-cycle commutator,**
5. **intentional rapid transfer of Lorentz impulse to the neutral majority,**
6. **allowing plasma decay between impulses,**
7. **distributed downstream re-ionization rather than long-distance conductivity persistence,** and
8. **reactive/capacitive energy recovery in the pulsed drive system.**

That combination should be treated as a hypothesis until a deeper patent and technical-literature search is complete.

## Next theoretical work

Before laboratory planning:

1. derive a multi-fluid charged-neutral momentum model;
2. obtain air ion/electron mobility and collision frequencies versus `E/N`;
3. construct a transient conductivity model from published atmospheric-pressure pulse data;
4. couple it to a static-field `J x B` cell model;
5. include sheath, surface-charge and external resonant-circuit dynamics;
6. solve the duty-cycle optimum using literature-derived ionization energy density;
7. optimize cell length, repetition rate, `B`, `sigma_on`, current density and active volume;
8. compare mass/power against the existing continuous V5 branch;
9. perform a focused patent search before claiming novelty.

## Research integrity statement

No practical propulsion performance is claimed here. This document records a candidate theoretical branch generated by comparative research and first-principles scaling. Its purpose is to identify a potentially more original and testable architecture before further funding or laboratory commitments.
