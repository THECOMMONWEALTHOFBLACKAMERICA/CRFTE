# CRTFE Neutral-Paramagnetic Air Branch — First Screening

**Status:** speculative alternative branch / theoretical screening  
**Date:** 2026-08-25

## Why this branch was checked

CRTFE's plasma branches pay a large energy penalty to create and maintain electrical conductivity in fresh atmospheric air. Ordinary air already contains a naturally field-responsive species: ground-state molecular oxygen is paramagnetic, while nitrogen is weakly diamagnetic.

Strong magnetic-field gradients have experimentally altered oxygen-containing gas flows, and pulsed-coil molecular decelerators have directly changed the velocity of paramagnetic O2 beams. This makes it reasonable to ask whether a no-ionization atmospheric accelerator can be built from magnetic-potential stages.

This is **not** a claim of practical propulsion. It is a screening calculation intended to determine whether the force/energy scale is worth deeper study.

## Governing bulk-force scale

For a weakly magnetic gas under the linear-susceptibility approximation:

```text
f_m = chi / (2 mu0) * grad(B^2)
```

and the ideal magnetic-potential-energy density available across a `0 -> B` field change is:

```text
u_m = chi B^2 / (2 mu0)
```

Using room-temperature air volume susceptibility of order:

```text
chi_air ~ +3.6e-7
```

and sea-level density:

```text
rho ~ 1.225 kg/m^3
```

provides an ideal specific magnetic-energy scale:

```text
e_stage = chi B^2 / (2 mu0 rho)
```

## Current hover target

For the current 650 kg target with 4.8 m^2 active area:

```text
v_i ~ 23.3 m/s
far-wake increment scale ~ 46.6 m/s
specific kinetic energy ~ 1.09 kJ/kg
```

Any no-moving-parts accelerator still has to supply this fluid kinetic energy in ideal hover.

## Ideal magnetic-stage count

If each perfectly timed magnetic stage contributes at most one full `0 -> B` magnetic-potential step to the bulk air:

| Peak field | Ideal magnetic energy / kg / stage | Stages for ~1.09 kJ/kg |
|---:|---:|---:|
| 5.2 T | ~3.2 J/kg | ~340 |
| 8 T | ~7.5 J/kg | ~145 |
| 12 T | ~16.8 J/kg | ~65 |
| 20 T | ~46.8 J/kg | ~23 |

This is an ideal energy accounting. Real air mixture response, magnetic-state populations, field nonuniformity, stage timing, collisions and coil losses will reduce performance.

## Packaging consequence

If all stages are packed into a 0.5 m interaction length, ideal stage pitch is roughly:

| Peak field | Stage pitch | Switching scale at ~30 m/s gas speed |
|---:|---:|---:|
| 5.2 T | ~1.5 mm | ~20 kHz |
| 8 T | ~3.4 mm | ~8.7 kHz |
| 12 T | ~7.7 mm | ~3.9 kHz |
| 20 T | ~22 mm | ~1.4 kHz |

Therefore the branch eliminates plasma ionization but replaces it with an extreme magnetic-switching problem.

## Why static magnets alone do not provide net thrust

A static conservative field gradient accelerates paramagnetic gas entering a high-field region and decelerates it as it leaves. A propulsion device needs a non-conservative cycle such as:

- timed coil switching (molecular-coilgun analogue);
- a traveling magnetic potential;
- or controlled switching of molecular magnetic state/susceptibility.

The first two require rapid large-field modulation. The third would require state control that survives sufficiently long in dense atmospheric collisions.

## Relevance of prior work

Existing work demonstrates important ingredients but not aircraft-scale bulk-air propulsion:

- magnetic gradients can alter/separate O2/N2 transport in air;
- pulsed electromagnetic coils have slowed supersonic O2 molecular beams;
- molecular coilguns use stage timing to avoid giving kinetic energy back to the field.

The remaining CRTFE-specific question would be whether dense-air collisions can be used as the momentum-transfer mechanism from magnetically acted-on O2 into the full N2/O2 mixture while maintaining acceptable stage efficiency.

## First conclusion

> **Neutral paramagnetic acceleration is physically real and removes the plasma-creation penalty, but the weak susceptibility of air demands either many multi-tesla stages or very high peak fields. In the present 0.5 m geometry, the required field-switching rate and AC magnetic-system burden appear severe.**

It remains worth retaining as an alternative theoretical branch because its fundamental failure mode is different from plasma MHD: it is limited by magnetic potential per kilogram and field-switching technology rather than electron lifetime.

## Reproducibility

The companion screening script is:

`tools/paramagnetic_air_stage_bound.py`
