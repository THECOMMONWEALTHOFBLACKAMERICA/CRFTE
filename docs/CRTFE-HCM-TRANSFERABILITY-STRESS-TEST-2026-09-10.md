# CRTFE-HCM Dorian Phase Relation — Transferability Stress Test

**Date:** 10 September 2026  
**Status:** Numerical only; no hardware-performance claim.

## Verdict

**Stage 1A carrier-law transferability: PASS under the frozen thresholds.**

**Full original full-sideband effective-medium prediction protocol: NOT YET COMPLETE.**

The fixed-K held-out experiment supports transferability of the Dorian Phase Relation at the carrier/constitutive level across changed length, termination, phase, frequency ratio, modulation velocity, and incidence direction. The full Floquet sideband vectors were generated and numerically converged, but a separate reduced effective Floquet model capable of predicting every held-out sideband from frozen constitutive parameters has not yet been specified. Therefore no full-sideband effective-medium PASS is claimed.

## Protocol correction before the final run

The first Stage-1 implementation varied `u` by changing spatial wavenumber `K` while holding `f_m=3 MHz`. At `u=0.05` this drove the discrete modulation to approximately `K d = 4.712 rad/cell`, changing the spatial modulation geometry and leaving the intended fixed-geometry comparison. That run failed its held-out criteria and is retained as an implementation-control record rather than discarded.

Before the corrected held-out run, the protocol was amended and frozen so that:

- `K d = pi/6` is fixed for every length and every `u`;
- `f_m` is varied to set `u`;
- `f_0 = r f_m`;
- all original pass/fail thresholds are unchanged;
- a fresh held-out split was generated with seed `2026091002`.

Protocol amendment SHA-256:

`e4f521388a443c1c33bb687cd9178a7b0efbca31e9117e09abfdc6628c0b7789`

Exact corrected held-out split SHA-256:

`1abef1d3586e937fd57049719cd3f29cd8495bb80ab4d66eff64beb343e24123`

## Harmonic convergence

The sparse harmonic-balance solver retains `h=-15..15` for the held-out experiment.

At the fixed-K high-u convergence point (`u=0.70`, `r=0.03`, `N=192`, `ZL=50 ohm`, `ZR=75 ohm`, `delta=22.5 deg`), increasing `H=14` to `H=15` changed the overlapping full scattering vector by approximately `1.80e-13` in absolute amplitude, with outermost sideband amplitude about `2.51e-12`.

This is below the predeclared weak-sideband absolute tolerance of `1e-7`.

## Held-out prediction — analytic coefficient fixed

The primary model was

`xi = 0.005 * [u/(1-u^2)] * cos(delta) + D r^2`

with `0.005 = m_e m_m / 2` fixed analytically and only the background coefficient `D` retrieved from training.

The training-only fitted background coefficient was:

`D = -0.00426077675024`

Held-out results over 96 device conditions:

- median relative error, non-null: **2.624%**
- 95th-percentile relative error: **6.806%**
- worst non-null relative error: **10.384%**
- median absolute carrier-phase error: **8.668e-06 rad**
- 95th-percentile carrier-phase error: **4.719e-04 rad**
- worst carrier-phase error: **8.898e-04 rad**

The predeclared thresholds were 5% median, 10% 95th percentile, 20% worst non-null relative error, `2e-4 rad` median phase error, and `5e-4 rad` 95th-percentile phase error.

**All predeclared analytic-coefficient thresholds pass.**

The worst absolute phase-error point exceeds `5e-4 rad`, but worst-case phase error was not a predeclared pass/fail threshold and is reported transparently.

## One-time coefficient retrieval

When `C` and `D` are fit once on training and then frozen:

- `C = 0.0051063844052`
- analytical weak-order value = `0.005`
- coefficient difference = **2.128%**

Held-out median relative error is **1.504%** and 95th-percentile relative error is **7.064%**.

## Held-out velocity-law competition

All candidate laws received the same two-parameter treatment on training: one global scale `C` plus one global `D r^2` background.

| Velocity law | Held-out SSE |
|---|---:|
| `u/(1-u^2)` | 9.673966e-07 |
| `u/(1-u)` | 9.905526e-06 |
| `u/(1-u^2)^(3/2)` | 1.836716e-05 |
| `u` | 3.746371e-05 |

The Dorian form `u/(1-u^2)` has the lowest held-out SSE. The nearest competitor has approximately **10.24x** larger held-out SSE.

## Length transferability and de-embedding

Four lengths (`N=48,96,144,192`) were compared at fixed per-cell modulation geometry.

A simple linear length de-embedding,

`phi_nr(N) = bulk_slope * N + boundary_intercept`,

was applied at `u=0.15, 0.40, 0.60` and `delta=0,45,180 deg`.

Across those nine cases, the de-embedded bulk estimate differs from the analytic Dorian value by at most **3.02%**.

## Termination invariance

At `N=192`, `u=0.40`, `r=0.02`, termination pairs included:

`50/50`, `50/25`, `25/50`, `50/75`, `75/50`, `50/100`, and `100/50 ohm`.

Away from the quadrature null, the largest termination-induced range in retrieved `xi` is approximately **0.745%** of the mean signal.

At `delta=90 deg`, the relative ratio is not meaningful because the leading signal is near zero; the absolute `xi` range is retained in the data.

## Symmetry controls

- Static (`m_e=m_m=0`): reciprocity residual is at numerical zero.
- C-only and L-only residuals are each about **0.107%** of the dual-channel `delta=0` signal at the control point.
- `delta -> delta+pi` reverses the leading directional term.
- Traveling-wave reversal `K -> -K` reverses the retrieved coupling with mismatch of approximately **2.431e-11%**.
- Swapping unequal loads produces only a small change in the retrieved bulk carrier term.

## What this does and does not establish

The corrected Stage 1A run is evidence that the **carrier-level effective Dorian phase law transfers across held-out finite-device conditions without per-condition coefficient refitting** in the declared weak/moderate, fixed-geometry numerical regime.

It does **not** establish:

- experimental hardware behavior;
- isolation, insertion loss, efficiency, gain, or RF performance;
- near-luminal multiband behavior;
- a complete reduced effective-medium prediction of every Floquet sideband.

The full sideband arrays were generated specifically so that the next stage can define a reduced Floquet constitutive/scattering model, freeze it on training data, and ask it to predict held-out complex sideband response without refitting.

## Bottom line

**The Dorian Phase Relation survives the corrected held-out carrier-transferability test.**

The earlier failed variable-K run remains part of the record because it exposed an important implementation confound rather than being discarded. The stronger full-sideband predictive test remains open.
