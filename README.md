# CRFTE / CRTFE Atmospheric Electromagnetic Propulsion Research

> **Status:** theoretical / reduced-order research with ground experimentation on hold pending P4 model consolidation. No working lift hardware has been demonstrated.

## Project links

- [Website and ecosystem status](PROJECT-LINKS.md)
- [Commonwealth of Black America public record](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/Commonwealth-of-Black-America)
- [T.A.R. — The Akashic Records](https://github.com/THECOMMONWEALTHOFBLACKAMERICA/The-Akashic-record)

No standalone CRFTE website has been verified or published yet; this repository remains the canonical public project location.

## Project goal — locked

CRTFE remains a **large-area, no-moving-parts atmospheric electromagnetic propulsion research program** with a two-person VTOL/wingborne aircraft as the long-range application.

The core objective is unchanged:

> **Transfer electromagnetic momentum directly into a large atmospheric-air mass flow without conventional rotors, propellers, turbines or mechanical compressors.**

Recent literature review and reduced-order simulation are being used to avoid re-testing established plasma/MHD physics and to identify which CRTFE-specific coupling problem actually requires experiment.

See: [P4 Project Goal Lock](docs/PROJECT-GOAL-LOCK-P4.md).

## Current primary theoretical branch — P4

The main branch is now a **full-stream segmented synchronous Lorentz duct**:

1. atmospheric air enters the active duct;
2. a strong stationary magnetic field is established by an HTS/high-field system;
3. conductivity is produced in controlled spatial/temporal windows;
4. a transverse current/electric drive is synchronized with those windows;
5. `J × B` transfers momentum directly to the full atmospheric stream;
6. segmented cells distribute and commutate the interaction without requiring the entire multi-tesla magnetic field to travel.

This stays close to the original CRTFE concept while correcting a key modeling issue: the large static HTS bias field and the amplitude of a traveling magnetic field cannot automatically be treated as the same `B` in the old V5 `B²` relation.

### Goal-aligned reduced-order model

```text
F = D σ_on E_drive B_static V
σ_eff = D σ_on
P_J = F² / (σ_eff B_static² V)
```

Segmentation can improve timing, commutation, localization and energy recovery, but does not by itself remove the average `D σ_on` requirement.

For the current 650 kg target with `A = 4.8 m²`, `L = 0.5 m`, `V = 2.4 m³`:

```text
hover thrust ≈ 6.38 kN
ideal hover induced velocity ≈ 23.3 m/s
ideal fluid-power floor ≈ 148.5 kW
```

If the active-gas Joule/slip allowance is provisionally limited to 50 kW, the reduced-order effective-conductivity requirement is approximately:

| Static field | Required effective conductivity |
|---:|---:|
| 3 T | ~37.6 S/m |
| 5 T | ~13.6 S/m |
| 8 T | ~5.3 S/m |

These are screening values, not demonstrated results.

## New plasma-source figure of merit

Peak conductivity alone is no longer the optimization target.

For each plasma pulse define:

```text
K_sigma = integral[σ(t) dt]
ε_p = deposited plasma-source energy density per pulse
R_p = ε_p / K_sigma
```

Lower `R_p` is better: it measures how much energy must be paid for useful conductivity-time.

For periodic pulsing:

```text
P_plasma+Joule
  = F²/(B² V σ_eff)
  + V σ_eff R_p
```

and the reduced-order optimized minimum is:

```text
P_extra,min = (2F/B) sqrt(R_p)
```

The project therefore asks a more useful question than “can air reach 60–150 S/m?”:

> **How much force-producing conductivity impulse can the source create per joule, and can that impulse be synchronized with a strong static field and transferred to neutral air?**

Reproducible screening model: [`tools/goal_aligned_synchronous_lorentz.py`](tools/goal_aligned_synchronous_lorentz.py).

## Pulsed conductivity remains a core mechanism

High instantaneous conductivity can still be valuable even if it is short-lived, provided pulse energy and repetition rate close.

For the provisional 50 kW Joule-loss target:

- at **5 T**, `σ_eff ≈ 13.6 S/m`;
- at **8 T**, `σ_eff ≈ 5.3 S/m`.

If an on-state reaches hundreds of S/m for several microseconds, the required cadence moves into the low-kHz range. If useful conductivity survives only tens of nanoseconds, required cadence moves into the hundreds-of-kHz or MHz range.

That makes **conductivity impulse + pulse energy + commutation** the key subsystem problem.

## Branch control — do not drift from the vehicle goal

### Primary

**Full-stream segmented synchronous Lorentz duct** — static high field, synchronized conductivity/current, full atmospheric mass flow.

### Retained comparison

**V5 traveling-field induction MHD** — retained as a reference branch, but its field decomposition and full system efficiency require correction.

### Supporting subsystem research

Carrier-memory chemistry, negative-ion/metastable pre-ionization, capacitive/electrodeless current coupling, resonant reactive-energy recovery, Hall/tensor conductivity and high-field magnet topology are retained only if they improve the primary branch.

### Screening branches, not project replacements

Small high-speed plasma-driver/ejector concepts, bulk O2 chemical conditioning, and neutral paramagnetic-air acceleration are documented as boundary studies. They do **not** replace CRTFE's atmospheric electromagnetic propulsion objective.

## V0.3 / OSU status

The previously prepared V0.3 P3 broad plasma-optimization campaign is **on hold** while P4 theoretical reengineering identifies the smallest experiment that tests a genuinely CRTFE-specific unknown.

Existing P3 documents are retained as research history and may supply diagnostics later, but they no longer define the immediate program direction.

## V4 / V5 interpretation

### V4 — discrete filament failure model

V4 exposed the `P/F = E/B` burden of high-sustaining-field filament propulsion. Filamentary/streamer behavior cannot be averaged into an optimistic bulk conductivity and inserted into V5.

### V5 — traveling-field comparison model

V5 showed a conditional reduced-order low-slip operating region. P4 now treats it as a **comparison model**, not the only route, because its simplified `B²` relation did not distinguish static bias field from the actual traveling-field component strongly enough.

See [V4–V5 Revised Interpretation](docs/V4-V5-REVISED.md).

## Target vehicle — V5 packaging reference

The long-range vehicle target remains documented in [`docs/TARGET-VEHICLE-V5.md`](docs/TARGET-VEHICLE-V5.md):

- crew: 2 side-by-side
- design gross mass: 650 kg
- length: 6.20 m
- span: 5.40 m
- wing reference area: ~11 m²
- four active lift modules
- total active lift area: ~4.80 m²
- no-moving-parts atmospheric electromagnetic propulsion target

The vehicle remains a research target, not demonstrated flight hardware.

## Active theoretical artifacts

- [P4 Project Goal Lock](docs/PROJECT-GOAL-LOCK-P4.md)
- [Pulsed Lorentz Simulation P1](docs/PULSED-LORENTZ-SIMULATION-P1.md)
- [Carrier-Memory Simulation P2](docs/CARRIER-MEMORY-SIMULATION-P2.md)
- [Oxygen-Memory Energy Sanity Check](docs/OXYGEN-MEMORY-ENERGY-SANITY-CHECK.md)
- [Neutral Paramagnetic Air Branch Screen](docs/NEUTRAL-PARAMAGNETIC-AIR-BRANCH-SCREEN.md)
- [V-2 Hybrid MHD Baseline](docs/V2-HYBRID-MHD-BASELINE.md)
- [V-2 G2 Electromagnetic Validation](docs/V2-G2-ELECTROMAGNETIC-VALIDATION.md)

## Current program conclusion

> **CRTFE remains an aircraft-scale atmospheric electromagnetic propulsion project. P4 is narrowing the design to the full-stream electromagnetic mechanism that maximizes momentum transferred per joule and per kilogram of installed field system. Side branches are retained only when they improve that mechanism.**

The next theoretical deliverable is a coupled segmented-cell model that propagates `σ(t)`, current, `J×B` impulse, neutral momentum, thermal deposition, surface/sheath charge and circuit-energy recovery through the full target mass flow before another laboratory pitch is made.