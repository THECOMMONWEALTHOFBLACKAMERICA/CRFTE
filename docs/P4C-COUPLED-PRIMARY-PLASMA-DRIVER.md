# CRTFE P4C — Coupled Primary / Plasma-Loop Driver Simulation

**Date:** 2026-08-25  
**Status:** reduced-order theoretical screen inside the primary CRTFE architecture  
**Goal lock:** full-stream atmospheric air + pulsed conductivity + stationary high-B HTS poles + direct J×B thrust; no rotor/propeller/turbine substitution

## Purpose

P4B showed that a bipolar static-pole plasma loop can make both transverse legs contribute thrust while keeping the closed induced-current loop compact and low-inductance. P4C adds the missing primary pulse circuit instead of treating the induced plasma-loop voltage as an ideal source.

The model contains:

```text
primary pulse capacitor C
primary inductance L1
primary resistance R1
mutual inductance M = k sqrt(L1 L2)
plasma-loop inductance L2
plasma-loop resistance R2(t)
stationary +B/-B propulsion poles
```

The coupled equations are the standard transformer-equivalent form used in inductive plasma devices:

```text
L1 dI1/dt + M dI2/dt + R1 I1 = Vc
M dI1/dt + L2 dI2/dt + R2(t) I2 = 0
C dVc/dt = -I1
```

P4C does not yet model plasma chemistry, Hall conductivity, 3D flux leakage, switch losses, HTS cryogenics, or structural magnet mass.

## Vehicle / force anchor

```text
vehicle mass = 650 kg
hover thrust = 6.376 kN
modules = 4
thrust/module = 1.594 kN
stationary field magnitude = 8 T
active transverse leg length = 1.0 m
pulse rate = 3 kHz
```

Because the bipolar geometry makes two opposite-current / opposite-B legs add thrust,

```text
F_module = 2 B l f ∫I2(t)dt
```

so the required current impulse is

```text
∫I2 dt = 0.03321 A*s per module per pulse.
```

## Representative circuit

The central screen uses:

```text
C = 20 uF
L1 = 1.0 uH
R1 = 3 mOhm
L2 = 0.39 uH
R2 = 10 mOhm at pulse start
k = 0.8
```

`R2 = 10 mOhm` is the same optimistic broad-current-sheet value used in P4B for approximately 800 S/m on-state conductivity. It is not a measured atmospheric-air value.

## Constant-resistance 5 us result

At `k = 0.8`, the capacitor voltage required to reproduce the target current impulse is approximately:

```text
V0 ≈ 1.14 kV
primary peak current ≈ 7.7 kA/module
plasma-loop peak current ≈ 9.2 kA/module
initial capacitor energy ≈ 13.1 J/module/pulse
primary resistive loss ≈ 0.53 J/module/pulse
plasma-loop Joule loss ≈ 2.59 J/module/pulse
residual magnetic energy at pulse end ≈ 9.5 J/module
```

If 98% of the residual magnetic energy is eventually recovered, the four-module 3 kHz electromagnetic loss scale is approximately:

```text
P_EM ≈ 40 kW
```

This excludes plasma creation power and the stationary HTS system.

## Coupling-coefficient sensitivity

With the same `20 uF / 1 uH / 0.39 uH / 5 us` circuit:

| Coupling k | Required V0 | Primary peak | Plasma peak | Initial cap energy | Four-module EM loss @ 98% recovery |
|---:|---:|---:|---:|---:|---:|
| 0.6 | ~2.25 kV | ~11.8 kA | ~10.5 kA | ~50.7 J | ~55 kW |
| 0.7 | ~1.63 kV | ~9.5 kA | ~9.9 kA | ~26.7 J | ~46 kW |
| **0.8** | **~1.14 kV** | **~7.7 kA** | **~9.2 kA** | **~13.1 J** | **~40 kW** |
| 0.9 | ~0.78 kV | ~6.7 kA | ~9.2 kA | ~6.1 J | ~35 kW |

### Interpretation

The transformer coupling coefficient is now a first-class CRTFE design variable.

A weakly coupled plasma loop does not make P4C impossible, but it raises circulating capacitor energy, primary current, recovery burden, and voltage very quickly. The preferred region from this screen is approximately:

```text
k >= 0.7–0.8
L1 ~ order 1 uH
L2 < ~0.5 uH
```

Whether atmospheric plasma sheets can actually produce `k` in that range with practical coil stand-off and insulation is not established.

## Conductivity-decay correction

A constant 10 mOhm plasma loop for the full pulse is optimistic. To screen turn-off, P4C also uses

```text
R2(t) = R2,0 exp(t / tau_sigma)
```

with

```text
tau_sigma = 5 us.
```

This represents an effective conductivity collapsing on the same microsecond scale that P4 has been targeting.

With `k=0.8`, 98% residual-field recovery, and the required force impulse preserved:

| Drive window | Required V0 | Primary peak | Plasma peak | Four-module EM loss | Current reversal inside window? |
|---:|---:|---:|---:|---:|:---:|
| 3 us | ~2.55 kV | ~15.3 kA | ~18.4 kA | ~106 kW | no |
| 4 us | ~1.63 kV | ~10.3 kA | ~12.0 kA | ~82 kW | no |
| 5 us | ~1.23 kV | ~7.8 kA | ~9.1 kA | ~68 kW | no |
| 6 us | ~1.04 kV | ~6.6 kA | ~7.6 kA | ~59 kW | no |
| 7 us | ~0.96 kV | ~6.1 kA | ~7.1 kA | ~53 kW | no |
| **7.5 us** | **~0.95 kV** | **~6.0 kA** | **~7.0 kA** | **~52 kW** | **no** |

In the same oscillator, the plasma-loop current begins to reverse shortly after this region if the circuit is allowed to ring freely. A current reversal under fixed +B/-B poles would produce reverse thrust.

Therefore the preferred P4C pulse is not an unconstrained resonant ring. It is:

```text
capacitor / transformer forward pulse
        -> build desired plasma-loop impulse
        -> interrupt or clamp before I2 crosses zero
        -> recover remaining magnetic/capacitive energy
        -> reset during low conductivity
```

This is consistent with prior pulsed-inductive propulsion work that uses diode clamping, pulse-compression, and energy-recovery circuits. It does not prove a 3 kHz aircraft implementation.

## Important comparison to existing pulsed-power hardware

Published inductive-pulsed-plasma work has demonstrated pulsed-power hardware at approximately 3.3 kV, 20 kA peak current, and 15 kA/us switching rate with a recovery-oriented pulse-compression-ring circuit. P4C's representative primary pulse is therefore not outside the known *instantaneous* voltage/current class.

The CRTFE challenge is substantially harder in other dimensions:

- approximately 3 kHz continuous repetition rather than occasional laboratory pulses;
- four distributed aircraft modules;
- atmospheric-pressure air rather than low-pressure propellant plasma;
- simultaneous proximity to multi-tesla HTS fields;
- heat rejection, switch RMS current, insulation, EMI, and installed mass.

## New electrical design target

P4C gives a cleaner current-drive target:

```text
per module, representative:
~1 kV capacitor bus/pulse voltage
~6–8 kA primary peak
~7–9 kA plasma-loop peak
~10–15 J circulating pulse energy
~7 us forward thrust pulse
3 kHz repetition
clamp/recovery before current reversal
```

At the `k=0.8`, decaying-conductivity, ~7.5 us point, the model places electromagnetic dissipation/recovery penalty near **52 kW across all four modules**. This leaves only about 28 kW if the earlier P4 provisional 80 kW plasma+EM-overhead allowance is retained.

Therefore the next decisive question is still plasma-source efficiency: can the required broad transient conductivity be created for roughly tens of kilowatts total rather than hundreds of kilowatts or megawatts?

## What improved

P4C supports three useful conclusions without changing CRTFE's goal:

1. **The main propulsion field can remain static.** The primary drive circuit does not need a traveling multi-tesla field.
2. **Sub-microhenry plasma-loop geometry remains valuable.** It keeps pulse voltage and circulating energy within a known pulsed-power class.
3. **Pulse shape matters.** The transformer pulse should be matched to conductivity decay and actively clamped before reversal rather than assuming an arbitrary 5 us rectangular drive.

## What is not solved

P4C does not demonstrate flight feasibility. Remaining gates include:

```text
measured atmospheric sigma(t)
plasma energy per conductivity impulse
real mutual coupling k
Hall/tensor conductivity under 8 T
3D +B/-B static-field map
primary winding and switch AC loss
HTS fringe-field exposure and cryogenic loss
module structural mass / Maxwell stress
neutral-flow response and actuator-disk closure
```

## Next simulation

The next model should couple the P4C circuit to the plasma source itself:

```text
plasma-source pulse energy
 -> electron density / mobility / sigma(t)
 -> R2(t)
 -> induced I2(t)
 -> JxB impulse
 -> neutral-flow momentum
 -> gas heating
```

That will let the project optimize **thrust impulse per total electrical joule**, the metric that matters for the aircraft.

## Reproducibility

See:

- `tools/p4c_coupled_primary_plasma_driver.py`
- `tools/bipolar_static_pole_inductive_loop.py`
- `docs/P4B-BIPOLAR-STATIC-POLE-INDUCTIVE-LOOP.md`
- `docs/PROJECT-GOAL-LOCK-P4.md`
