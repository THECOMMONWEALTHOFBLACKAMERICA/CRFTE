# V4–V5 Revised Interpretation

## Critical correction

V5 does **not** establish practical propulsion feasibility. It establishes a conditional result only:

> If moving atmospheric air can be made sufficiently and uniformly conductive — roughly 60–150 S/m in the present reduced-order model — at low enough auxiliary power and acceptable temperature, then the traveling-field MHD thrust/power equations close.

The conductivity state itself has **not** been demonstrated for this application.

## V4 — discrete filament failure model

V4 removed the assumption of a uniform plasma and treated conduction as discrete streamer/filament channels.

```text
I_fil = σ_fil E A_fil
F_fil = I_fil L B
P_fil = I_fil E L
P/F = E/B
```

For the tested case `E = 10,000 V/m`, `B = 1.5 T`, the electrical cost is about 6.67 kW per newton. That makes a 1,104 N module megawatt-class whenever thrust sets the required number of channels.

V4 also introduced spatial momentum coverage. With:

- L = 0.5 m
- flow speed = 48 m/s
- residence time ≈ 10.4 ms
- assumed effective momentum diffusivity D_mom = 0.4 m²/s

we get a momentum-spread radius of roughly 9.1 cm over the residence time. Even an extremely strong filament case therefore requires many spatial sites just to influence the full 0.6 m² duct.

### Standing rule

V4 is not archived. It is the **failure/falsification model** for any experiment that returns a streamer/filament-dominated conductive state.

If V0.3 is filamentary, feed measured:

- filament radius
- current
- lifetime
- repetition rate
- number density
- momentum footprint
- sustaining field

into V4.

Do **not** average those channels into an optimistic bulk σ and use V5.

## V5 — traveling-field conditional closure

V5 uses a distributed conductive atmospheric volume and a traveling electromagnetic field moving slightly faster than the air.

```text
F = σ (v_wave - u) B² A L

v_slip = F / (σ B² A L)

P_ohmic = F v_slip = F²/(σ B² A L)

P_total = P_induced + P_ohmic + P_aux
```

For the current baseline:

- F = 1,104 N/module
- A = 0.60 m²
- L = 0.50 m
- u ≈ 27.68 m/s
- ideal induced power ≈ 30.57 kW/module
- working cap = 60 kW/module

At B = 1.8 T, the steady reduced-order conductivity boundary is approximately:

- 52 S/m if P_aux = 5 kW
- 59 S/m if P_aux = 8 kW

A safer research target is roughly **80–150 S/m** to preserve margin for conductivity ripple and unmodeled losses.

### Representative conditional point

| Quantity | Value |
|---|---:|
| σ | 150 S/m (assumed) |
| B | 1.8 T |
| slip | 7.57 m/s |
| traveling-wave speed | 35.26 m/s |
| ideal induced power | 30.57 kW |
| Ohmic/slip power | 8.36 kW |
| auxiliary power | 5.00 kW (assumed) |
| modeled total | 43.93 kW/module |

This point is a **mathematical closure example only**.

## P_aux rule

The assumed 5–8 kW auxiliary allowance must be replaced as soon as real data exists.

```text
P_aux,measured = P_ionization
               + P_field-drive losses
               + P_cryo
               + P_controls
               + other measured auxiliaries
```

If measured P_aux destroys the feasible region, the model must show that result honestly.

## Revised decision logic

| Experimental result | Action |
|---|---|
| Bulk σ < 20 S/m | Stop / major pivot for current full-channel design |
| 20–60 S/m | Borderline; redesign / higher-field work only |
| ≥ 60 S/m | Re-run V5 using measured P_aux, heating, lifetime, and uniformity |
| 80–150+ S/m | Preferred region if measured losses still close |
| Filamentary/streamer result | Use V4, not V5 |
| Thermal/arc conductivity only | Treat as a hot-plasma architecture with full thermal penalty |

## Current scientific status

Established by the simulations:

1. Sparse high-sustaining-field filament propulsion does not satisfy the current power target.
2. A low-slip traveling-field MHD model contains a feasible mathematical region.
3. The region is strongly controlled by σ, B, and measured auxiliary power.

Not established:

- that atmospheric air can sustain 60–150 S/m bulk conductivity non-thermally;
- that the conductivity will be spatially uniform;
- that the state can persist long enough;
- that ionization power is only a few kW/module;
- that real HTS magnet/cryostat/aerodynamic losses fit the remaining budget.

## Correct conclusion

> **The traveling-field branch has conditional reduced-order closure, contingent on an atmospheric-conductivity state that has not yet been demonstrated for this application.**

Further broad vehicle optimization should wait until V0.3 produces measured conductivity and auxiliary-power data.
