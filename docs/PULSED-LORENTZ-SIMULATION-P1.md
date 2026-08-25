# CRTFE Pulsed Lorentz / Synchronous Conductivity Simulation — P1

**Date:** 2026-08-25  
**Status:** reduced-order theoretical screening; not CFD/PIC, not an experiment, not a vehicle-performance claim.

## Question

Can short-lived atmospheric plasma packets be used as electronically commutated current-carrying regions inside a strong static magnetic field to generate aircraft-scale Lorentz force without maintaining the entire duct continuously conductive?

## Baseline

- target gross mass: 650 kg
- hover thrust: 6.376 kN
- active area: 4.8 m²
- interaction length: 0.5 m
- active volume: 2.4 m³
- sea-level air density: 1.225 kg/m³
- ideal actuator-disk induced velocity: 23.29 m/s
- ideal fluid-power floor: 148.5 kW
- gas residence time through 0.5 m at the induced velocity: 21.47 ms

## Reduced-order equations

For a static transverse field and a conducting gas, the accelerator must overcome the motional back EMF. The useful screening form is

```text
J = sigma (E - u B)
F = J B V
```

Define `E_slip = E - uB`. Then

```text
F = sigma E_slip B V
P_slip = J^2 V / sigma = F^2/(sigma B^2 V)
P_electrical = F u + P_slip
```

`F u` is the useful fluid power; it should not be double-counted as an auxiliary loss.

## Case A — conductivity is available as a continuous material property

If 50 kW is allowed for slip/Joule loss, the conductivity required is:

| Static B | Required sigma | Ideal fluid + slip power |
|---:|---:|---:|
| 3 T | 37.65 S/m | 198.5 kW |
| 5 T | 13.55 S/m | 198.5 kW |
| 8 T | 5.29 S/m | 198.5 kW |
| 12 T | 2.35 S/m | 198.5 kW |
| 20 T | 0.85 S/m | 198.5 kW |

This is why strong localized static fields are mathematically valuable: they lower the conductivity requirement as `1/B²`.

## Case B — each parcel is ionized once and remains conductive for the full interaction

For screening only, use

```text
sigma ~= e n_e mu_e
```

with illustrative electron mobility `mu_e = 0.05 m²/(V s)` and an optimistic mean creation energy of `34 eV` per electron-ion pair. This gives the lower-bound ionization energy density

```text
U_ion ~= sigma * 34 / mu_e  [J/m³]
```

At the 50 kW slip-loss operating points:

| Static B | sigma | lower-bound one-pass ionization | total lower-bound power |
|---:|---:|---:|---:|
| 3 T | 37.65 S/m | 2.861 MW | 3.060 MW |
| 5 T | 13.55 S/m | 1.030 MW | 1.229 MW |
| 8 T | 5.29 S/m | 402 kW | 601 kW |
| 12 T | 2.35 S/m | 179 kW | 377 kW |
| 20 T | 0.85 S/m | 64 kW | 263 kW |

This case is already extremely optimistic because it assumes the created electrons remain useful for the full ~21 ms residence time.

## Case C — short-lived conductivity must be recreated

Atmospheric-pressure laser-spark measurements have reported peak electron density decaying to `1/e` in roughly 50 ns. P1 therefore screens what happens if the current-carrying population must be recreated on a characteristic lifetime `tau`.

Let `D` be conductive duty cycle. A simplified pulsed model gives

```text
F = D sigma E_slip B V
P_J = F²/(D sigma B² V)
P_create = D V U_create/tau
```

If `U_create ~= sigma W_eff/mu_e`, optimizing over duty cycle gives a useful lower bound:

```text
E_slip,opt = sqrt(W_eff/(mu_e tau))
P_extra,min = (2F/B) sqrt(W_eff/(mu_e tau))
```

A significant result is that **sigma cancels from this optimum** when carrier-creation energy scales linearly with carrier density. Merely chasing a larger instantaneous conductivity does not cure rapid carrier loss.

For `tau = 50 ns`:

| B | Fresh-air creation, W_eff=34 eV | Idealized 0.45 eV reactivation |
|---:|---:|---:|
| 5 T | 297 MW | 34.2 MW |
| 8 T | 186 MW | 21.4 MW |
| 12 T | 124 MW | 14.3 MW |
| 20 T | 74.4 MW | 8.55 MW |

Even the 0.45 eV column is only a mathematical reactivation-energy thought experiment; it does not account for optical efficiency, incomplete detachment, chemistry, driver losses, or the fact that the free electron can reattach again.

## Carrier-lifetime requirement

Suppose the propulsion program reserves only ~80 kW for plasma creation/reactivation plus slip loss beyond the ideal fluid-power term. The optimistic pulsed bound requires approximately:

| B | lifetime if W_eff=34 eV | lifetime if W_eff=4 eV | lifetime if W_eff=0.45 eV |
|---:|---:|---:|---:|
| 5 T | 0.691 s | 81.3 ms | 9.15 ms |
| 8 T | 0.270 s | 31.8 ms | 3.57 ms |
| 12 T | 0.120 s | 14.1 ms | 1.59 ms |
| 20 T | 43.2 ms | 5.08 ms | 0.572 ms |

Measured free-electron decay on nanosecond scales is therefore many orders of magnitude short of the direct fresh-pulse requirement.

## What the simulation says

### Finding 1 — the Lorentz-force equation itself is not the blocker

If conductivity were available continuously, a strong static field can move the required operating point into single-digit S/m conductivity at 8–20 T.

### Finding 2 — carrier creation/retention is the dominant problem

A scheme that creates a fresh atmospheric electron population every nanosecond/microsecond pulse is not competitive for the present 650 kg hover target. The lower-bound refresh power alone becomes megawatt to hundreds-of-megawatts scale.

### Finding 3 — instantaneous high conductivity is not the correct optimization target

For the recreated-pulse lower bound, conductivity cancels. The important figure of merit is closer to

```text
(mu_e * tau) / W_eff
```

combined with magnetic field strength.

The project therefore needs a carrier state that is either:

- mobile for much longer than ordinary free electrons in atmospheric air;
- reusable without paying full ionization energy each cycle;
- created in a low-ionization-energy working species;
- maintained by a plasma-chemistry memory mechanism at much lower incremental energy;
- or isolated from the bulk ambient-air stream so the same plasma working fluid can be reused.

### Finding 4 — a new branch is suggested

The pulsed-Lorentz concept should not be framed as `fresh air -> ionize -> push -> recombine -> repeat`.

A more promising theoretical search is **carrier reuse / plasma-memory propulsion**:

1. create a persistent ionic/metastable/seed reservoir;
2. temporarily liberate or mobilize high-mobility charge carriers only in the active magnetic cell;
3. apply the Lorentz impulse;
4. allow carriers to return to the reservoir rather than being permanently lost;
5. repeat without paying full atmospheric ionization energy each time.

Recent atmospheric-pressure DBD research reports high-repetition-rate memory effects associated with accumulated metastables and negative ions, while photodetachment experiments demonstrate that electrons can be liberated from negative oxygen ions in an atmospheric-pressure plasma afterglow. These phenomena do not prove propulsion viability, but they identify the physics that would have to be exploited for the pulsed branch to survive the energy screen.

## Research decision

**Do not build the pulsed atmospheric-ionization propulsion cell yet.**

The next simulation should replace the single `tau` parameter with a multi-species charge-reservoir model:

```text
free electrons <-> negative ions
positive ions
metastables
seed species
```

and calculate the energy cost of repeatedly returning bound/attached charge to a mobile state inside a static high-B interaction cell.

If that carrier-reuse model cannot reduce effective creation energy and extend usable mobility by several orders of magnitude, direct sea-level pulsed CRTFE hover should be considered energetically non-closing in its present form.

## Reproducibility

The corresponding screening code is `tools/pulsed_lorentz_reduced_order.py`.
