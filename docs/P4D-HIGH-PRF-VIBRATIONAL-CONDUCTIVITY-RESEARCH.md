# CRTFE P4D — High-PRF Vibrational Conductivity Research

**Date:** 2026-08-25  
**Status:** research branch inside goal-locked CRTFE architecture  
**Goal lock:** full-stream atmospheric air + controlled conductivity/current + stationary high-B field + direct J×B thrust

## Research conclusion

The literature substantially strengthens one pure-air route while exposing a second loss mechanism that must now be modeled explicitly.

### Strongest pure-air route

Use a hybrid discharge:

```text
repetitive nanosecond ionization pulses
+ sub-breakdown RF vibrational pumping
+ high pulse repetition frequency / discharge memory
+ P4B/P4C induced current loop
+ stationary bipolar HTS poles
```

The purpose of the RF field is not propulsion and not additional breakdown. It is selective vibrational excitation of N2/O2 intended to reduce oxygen attachment and increase electron detachment while keeping translational gas temperature low.

## Literature basis

1. Frederickson et al. (J. Appl. Phys. 101, 2007, DOI 10.1063/1.2724796) measured high-pressure O2/N2 plasma with vibrational temperatures ~2000–3000 K while translational/rotational temperature remained ~300 K. Vibrational excitation increased free-electron lifetime by ~100x, nearly mitigated rapid O2 attachment, and modeling inferred O2- detachment enhancement by 4–5 orders of magnitude.

2. Palm et al. (AIAA 2002-0637, DOI 10.2514/6.2002-637) showed that the vibrational excitation can be maintained with a sub-breakdown RF field, removing the need for CO-laser seeding. Their work reported at least three orders of magnitude reduction in effective attachment and up to order-of-magnitude reduction in recombination.

3. Gulko et al. (Plasma Sources Sci. Technol. 29, 104002, 2020, DOI 10.1088/1361-6595/abb3a1) experimentally separated functions in a ns-pulse/RF hybrid plasma: ns pulses produced ionization/electronic excitation while sub-breakdown RF predominantly drove vibrational excitation, maintaining strong vibrational nonequilibrium at low translational-rotational temperature.

4. Mahreen et al. (High Voltage 11, 445–457, 2026, DOI 10.1049/hve2.70140) studied atmospheric-air nanosecond DBD operation from 0.1–100 kHz and found strong high-PRF memory effects, including breakdown voltage reduction attributed to accumulated metastables, negative ions and residual electron sources. Below ~10 kHz, electron detachment from negative ions was identified as a primary breakdown route; above ~10 kHz the breakdown threshold fell well below conventional streamer expectations.

5. Historical Ohio State pulser/sustainer MHD work demonstrated stable diffuse nonequilibrium air/N2 plasma at ~40 kHz with a separate DC sustainer and ~1.5 T magnetic field, including measurable Lorentz-force flow acceleration/deceleration. This establishes that high-PRF pulsed ionization + separately driven MHD current + static B is prior art; CRTFE novelty cannot rest on those ingredients alone.

## Major P4D reframe: PRF

Earlier P4C screens used ~3 kHz, a 333 us period. That spacing is longer than many measured atmospheric afterglow ion/memory times.

A more literature-aligned range is now:

```text
40–100 kHz candidate PRF
10–25 us pulse spacing
~5–10 us useful current/conductivity window
```

This moves CRTFE operation into a measured discharge-memory regime and drastically lowers current impulse per event.

For the current 650 kg / four-module / 8 T bipolar-pole target:

```text
at 3 kHz: required current impulse/module/pulse ~0.0332 A*s
at 50 kHz: ~0.00199 A*s
at 100 kHz: ~0.000996 A*s
```

For a 5 us thrust window, the average pulse current is therefore only ~200 A/module at 100 kHz, rather than several kA in the 3 kHz P4C screen.

## Conductivity target at high PRF

For the current 8 T / 2.4 m3 active-volume baseline, limiting gas-current Joule loss to ~50 kW requires effective cross-field/Pedersen conductivity:

```text
sigma_P,eff ~5.3 S/m
```

Therefore:

```text
100 kHz, 5 us on-time (D=0.5): sigma_P,on ~10.6 S/m
50 kHz, 10 us on-time (D=0.5): sigma_P,on ~10.6 S/m
40 kHz, 10 us on-time (D=0.4): sigma_P,on ~13.2 S/m
50 kHz, 5 us on-time (D=0.25): sigma_P,on ~21.2 S/m
```

This is a major correction from the earlier ~400–1000 S/m transient target, which was driven largely by the low 3 kHz duty cycle.

Using an illustrative electron mobility ~0.055 m2/V/s and including a simple 8 T Hall/Pedersen correction, these on-state conductivities correspond to electron densities on the order of ~1–3 x 10^15 cm^-3. Atmospheric nanosecond diffuse discharges have experimentally reached ~10^15 cm^-3 over significant discharge volume, although their naturally useful lifetime is much shorter than CRTFE requires.

## Remaining pure-air wall: molecular-ion recombination

Suppressing O2 attachment does not eliminate electron loss.

At atmospheric-air molecular-ion recombination coefficients around ~1e-7 cm3/s, the characteristic recombination time at ne ~1e15 cm^-3 is only order 10 ns. Even coefficients reduced to ~1e-8 cm3/s give only order 0.1 us at that density.

Published vibrationally excited air/plasma work reports strong attachment suppression but typically only ~order-of-magnitude recombination reduction. Therefore P4D cannot assume that a ~5–10 us electron-conductivity window automatically follows from attachment suppression.

This is now the primary pure-air physics gate:

> Can vibrationally conditioned atmospheric air maintain the required cross-field conductivity for ~5–10 us at ne ~10^15 cm^-3 without molecular-ion dissociative recombination dominating?

## Seeded fallback — technically interesting, operationally poor

Classic nonequilibrium MHD used potassium/cesium seed because alkali ions can have much slower three-body recombination than molecular air ions. A 1972 potassium-seeded argon MHD experiment reported electron-density relaxation ~4e-4 s under its hot-argon conditions. Modern 2025 work has revisited UV photoionization of potassium-seeded MHD gases and found that net energy return can be feasible in targeted regions.

However, for CRTFE full-stream air, charge neutrality requires seed density at least comparable to desired electron density. At sea-level number density, ne ~7e14 cm^-3 corresponds to ~30 ppm fully ionized seed. With the current ~112 m3/s hover airflow, 30 ppm potassium would be roughly 5.5 g/s, ~20 kg/hour, if lost with open airflow.

Therefore alkali seeding is retained only as a physics fallback unless a credible recovery/recirculation mechanism appears. It is not the preferred CRTFE architecture.

## Current preferred P4D architecture

```text
FULL ATMOSPHERIC AIR
   -> high-PRF ns pulse ionization / reactivation
   -> sub-breakdown RF vibrational conditioning
   -> reduced O2 attachment / enhanced detachment
   -> short 5–10 us conductive window
   -> P4B/P4C low-inductance closed current loop
   -> adjacent +B/-B stationary HTS poles
   -> same-direction JxB force from both loop legs
   -> low-conductivity/reset phase
   -> repeat at ~40–100 kHz
```

This remains the original CRTFE propulsion mechanism. The RF and ns pulses are plasma-conditioning subsystems, not substitute propulsion methods.

## New simulation gate

The next model must stop imposing sigma(t) by assumption. It must solve or parameterize:

```text
ns ionization source S(t)
N2/O2 vibrational energy population
negative-ion attachment/detachment
positive molecular-ion composition
recombination beta(Te, species)
electron temperature / mobility
Hall/Pedersen conductivity under B0
RF vibrational power
sigma_P(t)
P4C current pulse
JxB impulse
```

The correct performance metric remains:

```text
net atmospheric momentum / total battery joule
```

## Decision

P4D HIGH-PRF VIBRATIONAL PURE-AIR ROUTE: **PROMOTED TO PRIMARY RESEARCH CANDIDATE**

Reason: it directly addresses the attachment/lifetime problem with demonstrated atmospheric/high-pressure physics and simultaneously reduces the peak conductivity/current burden by moving from 3 kHz toward 40–100 kHz.

Molecular-ion recombination at the required carrier density remains **UNRESOLVED** and is the next decisive theoretical/experimental gate.

No flight-feasibility or novelty claim is made by this research note.
