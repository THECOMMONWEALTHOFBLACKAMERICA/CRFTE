# CRTFE Carrier-Memory Simulation — P2

**Status:** theoretical reduced-order design review  
**Date:** 2026-08-25  
**Purpose:** determine whether atmospheric plasma memory can make the pulsed Lorentz-entrainment branch materially more efficient than recreating fresh ionization for every force pulse.

## 1. Result in one sentence

Negative-ion/metastable memory can reduce repeated breakdown cost, but **carrier reuse alone does not close the vehicle power budget if useful free-electron conductivity still collapses on ~10–100 ns timescales**. A viable memory branch needs a chemically sustained effective conducting state in roughly the `10^-4–10^-3 s` range, much stronger localized static fields, or both.

## 2. Literature facts used as bounding inputs

The model does not treat these values as universally transferable to CRTFE air. They are used to establish plausible timescale ranges.

- Atmospheric-pressure pulsed-air measurements have reported free-electron density decaying to `1/e` in about **50 ns** after formation in one laser-spark configuration.
- Atmospheric-pressure Ar/O2 afterglow measurements found characteristic lifetimes of about **7.3 us (O-)**, **17 us (O2-)**, **23 us (O3-)**, **28 us (O2+)**, and **117 us (NO+)**. These are not dry-air lifetimes but demonstrate microsecond-scale ionic memory.
- Atmospheric-pressure air repetitive-discharge studies show high repetition frequency can lower breakdown voltage through accumulated negative ions, metastables and related memory species.
- Atomic oxygen produced by nanosecond air discharges can persist for **hundreds of microseconds** in air in some experiments.
- At sufficiently high O-atom density, published kinetic modeling reports effective electron detachment from negative ions, shifting the afterglow loss mechanism toward electron-ion recombination and maintaining higher electron density between pulses.

## 3. Reduced-order model

For the pulsed Lorentz branch:

```text
F = D sigma E B V
P_J = F^2 / (D sigma B^2 V)
```

If the mobile carrier population must be activated at an effective energy cost `W` and remains useful for an effective conducting lifetime `tau`:

```text
P_activation = D sigma V W / (mu_e tau)
```

where `W` is expressed in electron-volts per elementary charge (numerically equivalent to volts in the derived expression).

Optimizing over duty cycle gives the lower-bound relation:

```text
P_extra,min = (2 F / B) sqrt(W / (mu_e tau))
```

The important consequence is that **conductivity cancels from this optimized lower bound**. Conductivity still matters for required voltage/current density, geometry and stability, but merely raising peak sigma does not defeat the carrier-creation/lifetime penalty.

The controlling plasma figure of merit becomes approximately:

```text
mu_e * tau / W
```

## 4. Idealized storage/reuse model

For a stored carrier population with exponential storage lifetime `tau_s`, pulse period `T`, and perfect reattachment/recovery after every activation, the maximum idealized activation count is:

```text
N_reuse = 1 / (1 - exp(-T/tau_s))
```

This is an optimistic ceiling. Real recombination, wall loss, chemistry changes and incomplete reattachment will reduce it.

If initial ion-pair creation costs `W_create` and each reactivation costs `W_reactivate`:

```text
W_eff = W_reactivate + W_create / N_reuse
```

Even with optimistic storage, `W_eff` approaches the reactivation-energy floor; it cannot go to zero.

## 5. What the reuse sweep says

Using illustrative values:

- `W_create = 34 eV`
- `W_reactivate = 0.45 eV` as a thermodynamic-scale lower-bound reference, not an achieved system efficiency
- `mu_e = 0.055 m^2/(V s)` as an atmospheric-order placeholder
- `B = 8 T`
- free-electron conducting lifetime = `50 ns`

then even very optimistic reuse leaves the extra-power lower bound in the **tens of megawatts**.

Examples under perfect recovery:

| Storage lifetime | Repetition | Ideal reuse count | Effective activation energy | Extra power lower bound @ 8 T / 50 ns |
|---:|---:|---:|---:|---:|
| 20 us | 100 kHz | ~2.5 | ~13.8 eV | ~113 MW |
| 117 us | 100 kHz | ~12.2 | ~3.24 eV | ~54.7 MW |
| 117 us | 1 MHz | ~117 | ~0.74 eV | ~26.1 MW |
| 300 us | 1 MHz | ~300 | ~0.56 eV | ~22.8 MW |

**Conclusion:** reusing charge chemistry is valuable, but it cannot compensate for a `50 ns` conducting window by itself.

## 6. Chemical-memory branch

The more promising interpretation is not simply `negative ion = battery`.

The stronger possibility is a chemically conditioned afterglow in which atomic oxygen / metastable chemistry continuously returns attached electrons to the mobile population, so the **effective conducting lifetime** is much longer than the raw free-electron attachment time.

Published air-plasma kinetics at high O-atom density report exactly this qualitative behavior: electron detachment from negative ions becomes effective and the afterglow becomes recombination-limited rather than attachment-limited.

This turns CRTFE's target from:

```text
maximize instantaneous electron density
```

into:

```text
maximize useful conducting lifetime per deposited chemical/plasma energy
```

## 7. Power sweep for a chemically sustained effective state

For the 650 kg target, retain:

```text
F_hover ~ 6377 N
P_fluid,ideal ~ 148.5 kW
```

Using the optimistic `W = 0.45 eV` reactivation-scale lower bound:

| Static B | tau_eff = 100 us | tau_eff = 300 us | tau_eff = 1 ms | tau_eff = 3 ms |
|---:|---:|---:|---:|---:|
| 5 T | ~730 kW extra | ~421 kW | ~231 kW | ~133 kW |
| 8 T | ~456 kW | ~263 kW | ~144 kW | ~83 kW |
| 12 T | ~304 kW | ~176 kW | ~96 kW | ~56 kW |
| 20 T | ~182 kW | ~105 kW | ~58 kW | ~33 kW |

These are lower bounds before cryogenic, inverter, dielectric, plasma-source, thermal-management and installation losses.

## 8. The field-strength penalty

Higher static field is mathematically powerful, but the structural penalty rises as:

```text
magnetic pressure = B^2 / (2 mu0)
```

Approximate Maxwell pressure:

| B | Magnetic pressure |
|---:|---:|
| 5 T | ~10 MPa |
| 8 T | ~25 MPa |
| 12 T | ~57 MPa |
| 20 T | ~159 MPa |

Therefore the 12–20 T branch cannot be treated as a free efficiency lever. Coil mass, support structure, stored energy, quench protection, cryogenics, fringe fields and local field geometry become primary aircraft constraints.

## 9. The overlooked design variable

The simulation indicates that **air chemistry may matter more than peak conductivity**.

The candidate operating cycle is now:

```text
nanosecond pulse
    -> create O / metastable / ion memory
    -> attached-electron reservoir forms
    -> chemical detachment returns electrons
    -> transverse propulsion current
    -> J x B impulse to the gas
    -> attachment / storage
    -> repeat before chemical memory decays
```

The charge carriers are not recreated from completely neutral air on every pulse. The discharge maintains a chemically prepared working state.

## 10. New gating questions

Before any hardware campaign, theory must answer:

1. Can dry atmospheric air be driven into an O/metastable state whose effective mobile-electron conductivity persists/repeats for `>= 0.1–1 ms` without excessive gas heating?
2. What deposited energy per cubic meter is required to sustain that chemistry?
3. What is the resulting time-dependent `sigma(t)` under the much lower transverse propulsion field rather than the ionization field?
4. Can the chemistry be maintained while the gas convects through multiple cells?
5. What fraction of deposited energy goes into O2 dissociation, vibration, heat and useful carrier maintenance?
6. Does the magnetic field materially alter electron/negative-ion kinetics at the selected `E/N`?
7. Does a 5–12 T localized-gap architecture beat the mass/energy penalty of trying to reach 20 T?

## 11. Current interpretation

The carrier-memory idea **survives only in a stronger form**:

> CRTFE should investigate a chemically conditioned, repetitively pulsed atmospheric working fluid where long-lived atomic/metastable chemistry continuously recycles attached electrons into a mobile conducting population, allowing repeated Lorentz-force impulses without paying full ionization energy every pulse.

This is not yet a feasibility result. It is the next theoretical branch to test against published plasma chemistry and a time-dependent multi-species solver.

## 12. Reproducibility

The companion script is:

`tools/carrier_memory_reduced_order.py`

It exposes storage lifetime, repetition rate, field strength, carrier mobility, activation energy and conducting lifetime as explicit inputs so assumptions can be replaced as better data are found.
