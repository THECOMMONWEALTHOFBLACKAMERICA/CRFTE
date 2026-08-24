# CRTFE V-2 G2 Electromagnetic Verification and Validation

> Revision P1 — 2026-08-24  
> Status: preliminary validation plan. Acceptance limits remain provisional until the uncertainty and design-sensitivity analyses are approved.

## Purpose

G2 prevents the project from treating an ideal uniform magnetic field or commanded coil current as proof of the installed electromagnetic system. It validates the model in stages before plasma loading and before any propulsion conclusion.

The full Ampere-Maxwell relation is:

```text
curl(B) = mu0 J + mu0 epsilon0 dE/dt
```

In a current-free, quasi-static air region where the displacement term is shown negligible, `curl(B) ~= 0`. The first physical test is therefore called a **plasma-off background-field test**. It is a vacuum test only if the chamber is actually evacuated.

## Required prediction outputs

- vector magnetic field `Bx, By, Bz` and `|B|`
- field phase and commanded direction across frequency
- coil currents and terminal voltages
- complex impedance matrix `Z_ij(f) = R_ij + jX_ij`
- mutual inductance, real/reactive/apparent power and power factor
- harmonics and thermal loss
- induced currents and loss in duct, cryostat, supports, shield, seams and fasteners
- HTS AC loss, temperature margin, stored energy and quench-relevant quantities
- plasma-loaded current, body-force direction, reaction force and Joule heating after G1 passes

## Staged gate

### G2A — numerical verification

Required evidence:

1. mesh-convergence study on all release quantities
2. energy-conservation residual within the numerical error budget
3. small and documented `div(B)` residual
4. correct conductor, insulator, air/plasma and magnetic material assignments
5. no artificial conduction through insulating regions
6. correct winding-circuit boundaries, phase sequence and mutual coupling
7. reproducible solver inputs, versions and result hashes

### G2B — bare-coil validation

Test the segmented stator without the plasma and without installed passive vehicle hardware.

Minimum map:

- five axial stations
- `5 x 5` cross-section grid at each station
- 125 vector-field locations total
- additional points at winding ends, seams and predicted extrema
- amplitude and phase sweep across the proposed operating-frequency band

Measure the complete coil impedance matrix, real/reactive/apparent power, power factor, harmonics, temperature rise and repeatability.

### G2C — installed passive hardware

Repeat the G2B matrix with the real duct, cryostat, supports, protective shield, seams and representative fasteners installed. Quantify field distortion, eddy-current loss, heating and any shorted-turn behavior.

### G2D — combined HTS and stator, plasma off

Map the combined static bias and traveling field. Measure HTS temperature margin, AC loss, field-volume homogeneity, stored energy and protection response. Do not proceed on unexplained heating or loss of critical-current margin.

### G2E — plasma-loaded validation

Run only after the G1 conductivity gate passes. Compare loaded impedance, vector fields, power and commanded force direction with the coupled model. Use blank, polarity reversal and phase-sequence reversal controls.

## Acceptance rule

Final limits must be registered before testing and derived from:

1. calibrated measurement uncertainty
2. repeatability and environmental variation
3. the sensitivity of thrust, loss, HTS margin and safety outcomes to each discrepancy
4. the combined uncertainty budget for the downstream G3-G6 tests

Preliminary objectives, not released acceptance criteria:

| Quantity | Provisional objective |
|---|---:|
| Field-amplitude RMS error | `<= 5%` |
| Maximum local field error | `<= 10%` |
| Field-phase error | `<= 5 degrees` |
| Real-power error | `<= 10%` |

## Controlled pass statement

> **G2 Pass Evidence:** A mesh-converged finite-coil and circuit model shall predict the measured vector magnetic-field distribution, phase response, complex coil-impedance matrix, real power, reactive power and passive-structure losses across a pre-registered spatial and frequency test matrix. Validation shall progress through bare-coil, installed-hardware, combined HTS/stator and plasma-loaded configurations. Acceptance limits shall be established before testing from measurement uncertainty and design sensitivity; preliminary objectives are no more than 5% field RMS error, 10% maximum local error, 5 degrees field-phase error and 10% real-power error.

Methodology precedent from other electromagnetic systems supports model-to-measurement correlation, but does not validate CRTFE propulsion performance.

