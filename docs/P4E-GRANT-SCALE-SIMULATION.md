# CRTFE P4E — Grant-Scale Simulation and Experimental Gate

**Date:** 2026-08-25  
**Status:** grant-scale reduced-order research package  
**Goal lock:** preserve CRTFE's full-stream atmospheric electromagnetic propulsion objective while testing only the smallest decisive mechanism first.

## Why P4E exists

Vehicle-scale CRTFE remains unproven. P4E therefore does not ask a funder to finance an aircraft or accept a lift claim.

It asks a much narrower question:

> **Can high-repetition-rate nanosecond ionization plus sub-breakdown RF vibrational conditioning sustain a low-temperature, spatially distributed atmospheric-air conductivity long enough to produce a repeatable, polarity-reversible Lorentz-force signal at useful energy cost?**

That question is directly connected to the final CRTFE architecture but is experimentally falsifiable at laboratory scale.

## Literature basis

The P4E parameterization is anchored to several demonstrated results:

1. Frederickson et al., *Journal of Applied Physics* 101 (2007), DOI 10.1063/1.2724796: vibrational nonequilibrium in high-pressure O2/N2 increased free-electron lifetime by roughly two orders of magnitude while bulk gas temperature remained near room temperature; modeling inferred O2- detachment increases of four to five orders of magnitude.
2. Palm et al., AIAA 2002-0637: sub-breakdown RF vibrational excitation in atmospheric-pressure air reduced effective attachment by at least three orders of magnitude and electron-ion recombination by up to about one order of magnitude.
3. Mahreen et al., *High Voltage* 11(2), 2026, DOI 10.1049/hve2.70140: atmospheric-air nanosecond DBD operation from 0.1-100 kHz showed strong high-PRF memory effects and reduced breakdown voltage associated with accumulated metastables and negative ions.
4. Adamovich et al., pulser-sustainer MHD work: 40 kHz pulse-ionized air/nitrogen with a separate sustainer current and ~1.5 T field produced stable uniform plasma and polarity-dependent Lorentz-force flow effects. Published air conductivity reached ~0.09 S/m in low-pressure supersonic test-section conditions.

P4E does not assume those results automatically transfer to 1-atm low-speed air. Their intersection defines the proposed experiment.

## Reduced-order kinetic model

Between ionizing pulses, electron density is screened by

```text
dn_e/dt = - beta n_e^2 - n_e/tau_attach
```

and each nanosecond pulse adds

```text
Delta n_e
```

The parameters `beta` and `tau_attach` are treated as experimentally measurable variables rather than fixed truths.

Representative bounds used in the grant screen:

```text
unconditioned:
    beta ~ 1e-7 cm^3/s
    tau_attach ~ 0.15 us

RF-vibrationally conditioned target region:
    beta ~ 1e-8 to 3e-8 cm^3/s
    tau_attach ~ 100 us or greater
```

The conditioned values are intentionally aggressive but are within the qualitative improvement factors reported in the cited vibrational-nonequilibrium literature.

Conductivity is mapped using

```text
sigma = e n_e mu_e / [1 + (mu_e B)^2]
```

with screening mobility

```text
mu_e = 0.05 m^2/V/s.
```

The laboratory Lorentz-force estimate is

```text
F = sigma E_drive B V
```

and gas-current Joule power is

```text
P_J = sigma E_drive^2 V.
```

## Proposed grant-scale cell

The simulation deliberately uses a small test volume:

```text
active plasma/MHD volume = 50 cm^3
static magnetic field = 1.5-2.0 T
propulsion/sustainer field = up to ~5 kV/m
nanosecond PRF = 40-100 kHz
controlled dry-air flow = ~5-20 m/s
```

A 50 cm^3 cell is large enough to generate a millinewton-class Lorentz-force signal but small enough that plasma conditioning power is in the laboratory hundreds-of-watts class rather than vehicle-scale megawatts.

## Central simulation cases

For `B = 2 T`, `E_drive = 5 kV/m`, `V = 50 cm^3`, `Delta n = 3e12 cm^-3/pulse`, and `f = 50 kHz`:

| Case | Mean ne | sigma | Predicted Lorentz force | MHD Joule power | 75 eV/pair ionization lower bound |
|---|---:|---:|---:|---:|---:|
| unconditioned (`beta=1e-7`, `tau_a=0.15 us`) | ~4.1e10 cm^-3 | ~3.3e-4 S/m | ~0.16 mN | ~0.4 W | ~90 W |
| attachment suppressed only | ~9.7e11 cm^-3 | ~7.7e-3 S/m | ~3.84 mN | ~9.6 W | ~90 W |
| moderate RF-conditioned (`beta=3e-8`, `tau_a=100 us`) | ~1.9e12 cm^-3 | ~1.52e-2 S/m | **~7.6 mN** | **~19 W** | ~90 W |
| strong RF-conditioned (`beta=1e-8`, `tau_a=100 us`) | ~3.3e12 cm^-3 | ~2.62e-2 S/m | **~13.1 mN** | **~33 W** | ~90 W |

The ionization term is a lower-bound screening number, not a predicted pulser wall-plug power.

The important result is the **signal contrast**:

```text
RF-off / unconditioned force ~0.1-0.2 mN
RF-conditioned force        ~5-13 mN
```

The modeled gain is roughly **50-80x** between the unconditioned and strongly conditioned kinetic limits at identical pulse-added carrier density.

That is large enough to form a decisive experimental hypothesis.

## High-PRF alternative

At `100 kHz`, a smaller `Delta n = 1e12 cm^-3/pulse`, `beta=1e-8`, and `tau_attach=100 us` gives approximately:

```text
mean ne ~2.7e12 cm^-3
sigma ~0.021 S/m
Lorentz force ~10.6 mN in 50 cm^3
MHD Joule power ~26.6 W
75 eV/pair lower-bound ionization power ~60 W
```

Thus the proposal should sweep both 40-60 kHz and 80-100 kHz rather than freeze one repetition rate.

## Why this is grant-worthy even though the aircraft is not

The proposal no longer depends on demonstrating high thrust.

It offers a testable scientific contribution:

> **Does vibrationally conditioned, high-PRF atmospheric plasma produce a large enough conductivity-time integral to measurably amplify MHD momentum transfer at fixed ionization-pulse energy?**

This bridges three previously separate literature areas:

- vibrational suppression of electron attachment/recombination;
- high-PRF atmospheric plasma memory;
- pulser-sustainer MHD momentum transfer.

The experiment can return a publishable negative result if the mechanisms do not combine as predicted.

## Experimental aims

### Aim 1 — conductivity-memory map

Measure, versus PRF and RF conditioning:

```text
n_e(t)
conductivity / impedance
attachment-decay time
recombination-dominated decay
vibrational-state indicators
gas temperature
spatial uniformity
energy per pulse
```

Primary comparison:

```text
ns pulses only
vs
ns pulses + sub-breakdown RF vibrational conditioning
```

### Aim 2 — controlled Lorentz-force demonstration

Place the characterized conductive-flow cell in a 1.5-2 T transverse static field and apply a separately controlled low-field sustainer/current drive.

Use four force-sign combinations:

```text
+B, +J
+B, -J
-B, +J
-B, -J
```

True Lorentz forcing must reverse according to `J x B` while thermal expansion, aerodynamic blockage, vibration, and most plasma-only effects do not.

Target signal from the simulation:

```text
>= 3 mN minimum useful force signal
5-15 mN preferred conditioned range
```

### Aim 3 — electrodeless CRTFE-current-drive translation

Only if Aims 1-2 pass, replace the laboratory sustainer with the P4B/P4C induced-loop topology:

```text
closed low-inductance plasma loop
+ adjacent +B/-B static poles
+ externally driven transformer flux
```

This preserves the final no-exposed-propulsion-electrode goal without making it a prerequisite for learning the plasma physics.

## Grant go/no-go gates

### Gate A — vibrational-conditioning effect

PASS if, at matched ns-pulse energy,

```text
integral sigma(t) dt with RF
    >= 10x
integral sigma(t) dt without RF
```

while bulk gas temperature rise remains `< 150 K`.

### Gate B — conductivity level

PASS if a spatially distributed moving-air state reaches at least

```text
sigma_mean >= 0.01 S/m
```

for a repeatable high-PRF operating point without arc-dominated conduction.

### Gate C — Lorentz-force identification

PASS if

```text
|F_B,J| >= 3 mN
```

and the measured force reverses with `J x B`, with magnitude agreeing with the independently measured `integral J x B dV` estimate to within approximately ±30% after calibration uncertainty.

### Gate D — energy benefit

PASS if RF conditioning improves

```text
Lorentz impulse / total plasma-conditioning joule
```

by at least `5x` relative to ns-pulse-only operation.

### Gate E — CRTFE continuation

Only if A-D pass should the program invest in electrodeless induced-current geometry and stronger static fields.

## Failure modes that remain scientifically useful

The project pivots or stops if any of the following occurs:

- RF increases vibrational excitation but does not increase conductivity-time integral;
- molecular-ion recombination dominates before useful conductivity develops;
- conductivity becomes filamentary/arc-like rather than distributed;
- apparent force does not reverse with `J x B`;
- heating reproduces the apparent force signal;
- energy per useful conductivity impulse remains too high.

Each failure directly answers a CRTFE uncertainty and is publishable mechanism data.

## Program conclusion

P4E is the first branch in the current CRTFE reengineering that meets a reasonable **grant-readiness** standard:

- established literature basis;
- distinct unanswered combined-mechanism question;
- laboratory-scale hardware rather than aircraft hardware;
- simulation-defined expected signal;
- multiple orthogonal controls;
- quantitative success and failure gates;
- direct path back to the original CRTFE propulsion architecture if successful.

It should be presented as a **fundamental plasma/MHD momentum-transfer experiment**, not as a request to fund a flying vehicle.

## Reproducibility

See `tools/p4e_grant_scale_kinetics_force.py`.
