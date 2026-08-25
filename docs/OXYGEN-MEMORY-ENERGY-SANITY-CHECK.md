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

## What remains viable to investigate

The chemistry branch survives only if at least one of the following is true:

1. the required O/metastable fraction is orders of magnitude below percent-level dissociation;
2. the active chemical/plasma volume is a small driver fraction rather than the full thrust-producing airflow;
3. the chemical reservoir is recirculated rather than rebuilt from fresh air;
4. a catalytic / associative-ionization pathway maintains seed electrons with much lower energy than bulk O2 bond breaking;
5. the flow is operated in a different pressure/temperature regime where carrier lifetime improves enough that little chemical conditioning is required.

## New architecture implication

The strongest remaining branch is no longer "chemically condition all the air."

A more defensible direction is a **two-fluid / driver-stream architecture**:

```text
small conditioned plasma driver stream
    -> strong static-field Lorentz acceleration
    -> momentum transfer / entrainment into a much larger neutral-air stream
    -> large-area low-exhaust-velocity thrust
```

This separates the expensive electromagnetic/plasma medium from the majority of the atmospheric working mass. It does not evade conservation of momentum or the actuator-disk power floor; its value would depend on whether driver-stream plasma power plus entrainment/mixing loss is lower than bulk-air ionization cost.

## Next calculation

Compare, on the same force basis:

- full-stream atmospheric MHD;
- chemically conditioned full-stream MHD;
- low-pressure / low-density plasma driver + neutral-air ejector;
- recirculating seeded plasma driver + neutral-air entrainment;
- conventional electric rotor/ducted-fan lower bound.

The correct metric is total electrical power and installed mass for a required thrust, not plasma thrust efficiency alone.
