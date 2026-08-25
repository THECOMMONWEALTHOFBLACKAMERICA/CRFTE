# CRTFE Oxygen-Memory Energy Sanity Check

**Status:** theoretical lower-bound screening  
**Date:** 2026-08-25

## Purpose

The carrier-memory branch proposed using atomic oxygen / metastable chemistry to detach electrons from negative ions and extend the effective conducting state between nanosecond pulses. This note checks whether creating that chemical reservoir in **fresh atmospheric flow** is energetically compatible with aircraft-scale propulsion.

## Key literature input

Published nanosecond-pulsed atmospheric-air experiments have reported that approximately 35% of deposited electrical energy went into O2 dissociation and approximately 21% into gas heating for the studied preheated-air discharge. This does not define CRTFE efficiency, but it provides a useful experimental-scale warning against treating atomic-oxygen production as energetically free.

## Bond-energy floor

Take the O2 dissociation energy as approximately 5.12 eV per molecule.

For sea-level air with approximately 21% O2 by number, the thermodynamic dissociation-energy floor is about:

```text
~4.39 MJ/m^3 for 100% O2 dissociation
~0.439 MJ/m^3 for 10% O2 dissociation
~43.9 kJ/m^3 for 1% O2 dissociation
~4.39 kJ/m^3 for 0.1% O2 dissociation
```

These values are bond-energy lower bounds only. They exclude imperfect excitation pathways, heating, radiation, recombination losses, power electronics and plasma-source inefficiency.

## Apply to the current 650 kg target flow scale

Using the current target active area `A = 4.8 m^2` and ideal hover induced velocity around `23.3 m/s`, the corresponding through-flow scale is roughly:

```text
Q = A u ~ 112 m^3/s
```

If every incoming cubic meter of fresh air had to be chemically conditioned once, the **O2 bond-energy floor alone** would be approximately:

| O2 dissociation fraction | Bond-energy floor |
|---:|---:|
| 0.1% | ~0.49 MW |
| 1% | ~4.9 MW |
| 10% | ~49 MW |
| 50% | ~245 MW |

If only 35% of deposited electrical energy reached O2 dissociation, using the published experiment strictly as an illustrative energy-partition reference, the corresponding deposited-power scale would be approximately:

| O2 dissociation fraction | Illustrative deposited power |
|---:|---:|
| 0.1% | ~1.4 MW |
| 1% | ~14 MW |
| 10% | ~140 MW |
| 50% | ~701 MW |

## Interpretation

This is a decisive result for the open-flow chemistry branch:

> **A high-dissociation atomic-oxygen reservoir cannot be regenerated from fresh atmospheric air across the full aircraft mass flow on every pass without overwhelming the propulsion power budget.**

The carrier-memory idea therefore cannot rely on bulk O2 dissociation of the complete hover stream.

## Correction to the small-driver-stream idea

A small conditioned plasma driver was considered as a way to avoid ionizing most of the atmospheric mass flow. Momentum theory shows why this does not solve hover power.

For the current 650 kg / 4.8 m^2 target, the ideal actuator-disk mass flow is approximately:

```text
m_dot ~ rho A v_i ~ 137 kg/s
```

If only a fraction `f` of that mass initially carries the full vehicle momentum, its minimum kinetic-power requirement is approximately:

```text
P_driver,min = F^2 / (2 f m_dot)
```

so:

| Initial momentum-carrying mass fraction | Ideal driver kinetic-power floor |
|---:|---:|
| 100% | ~148 kW |
| 50% | ~297 kW |
| 20% | ~742 kW |
| 10% | ~1.48 MW |
| 1% | ~14.8 MW |

An ejector/entrainment stage can redistribute that momentum into more air, but it cannot erase the kinetic energy already required to put the momentum into a small driver stream; real mixing adds loss.

**Therefore a tiny plasma driver stream is not a low-power escape route for hover.** CRTFE still needs electromagnetic coupling to a large effective atmospheric mass flow if it wants rotor-like induced-power scaling.

## What remains viable to investigate

The chemistry branch survives only if at least one of the following is true:

1. the required chemical-memory fraction is far below percent-level O2 dissociation;
2. naturally long-lived ion/metastable channels provide useful **time-integrated conductivity** without requiring bulk dissociation;
3. associative-ionization / detachment pathways maintain carriers with far less energy than rebuilding ion pairs from neutral gas;
4. a pressure/temperature state is created as part of the aerodynamic acceleration itself, extending carrier lifetime without a separate vacuum-energy penalty;
5. another field/current topology uses the long-lived ion current directly rather than requiring electron-dominated conductivity throughout the force pulse.

## Revised architecture implication

The design objective is no longer to move the plasma problem into a small driver stream. Instead it is:

> **Find the lowest-energy way to give a large atmospheric mass flow enough time-integrated transverse conductivity for a strong static magnetic field to apply the required axial impulse.**

That shifts the theoretical metric from peak conductivity to the integrated conductivity of *all* charge carriers:

```text
K_sigma = integral sigma(t) dt
        = e * sum_s integral n_s(t) mu_s(t) dt
```

Long-lived positive and negative ions may materially contribute even when free electrons have attached, because their much longer lifetimes can partly compensate for their much lower mobilities.

## Next calculation

The next model must include:

- electron conductivity spike;
- O2-/O-/O3- negative-ion tails;
- O2+/NO+ positive-ion tails;
- measured/estimated ion mobilities;
- chemical detachment / associative-ionization memory;
- total `integral sigma dt` per deposited joule;
- Lorentz impulse per deposited joule;
- static-field structural penalty.

The correct metric is total electrical power and installed mass for required thrust, not plasma thrust efficiency alone.
