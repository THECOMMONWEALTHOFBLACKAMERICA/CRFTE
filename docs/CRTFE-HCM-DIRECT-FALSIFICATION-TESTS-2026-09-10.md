# CRTFE-HCM — Direct Falsification Tests After Adversarial Review

**Date:** 10 September 2026  
**Status:** Numerical only. No hardware claim.

## Why this test was run

An adversarial review correctly identified that the previously reported direct energy-balance closure is an algebraic identity of the time-varying L/C ladder model and therefore functions as a simulator/unit-consistency test rather than as an independent falsification of the CRTFE-HCM phase relation.

Two tests that can actually fail the phase relation were therefore run:

1. direct terminated-device nonreciprocity versus relative phase, using independently excited left and right ports; and
2. functional-form selection for the modulation-velocity dependence over the bounded subluminal regime.

## Test 1 — Direct terminated-device S21 versus S12 phase sweep

A 48-cell finite ladder was driven from the left and right in separate simulations with identical physical modulation. The carrier-frequency transmission coefficients S21 and S12 were extracted after periodic settling.

Parameters:

- N = 48
- M = 4
- L0 = 625 nH
- C0 = 250 pF
- m_e = m_m = 0.10
- f_m = 3 MHz
- f_0 = 150 kHz
- u = 0.45
- 50-ohm source/load
- physical midpoint reference for the inductor modulation phase

For a 9-point phase sweep over 0 to 360 degrees, the centered signed carrier phase difference

    arg(S21 / S12)

fits a cosine with:

- amplitude A = 0.003167520 rad
- fitted phase delta0 = -179.9615 degrees
- RMS residual = 9.935e-7 rad
- relative RMS residual = 3.14e-4 = 0.0314%

The complex quantity S21 - S12 also fits a sinusoidal first harmonic with approximately 0.0315% relative RMS residual.

A 180-degree fitted phase is equivalent here to the expected sign convention for the extracted nonreciprocal phase. With physical midpoint referencing, the previously identified 15-degree geometric offset is not present as an unexplained phase error.

A refined cardinal-point check gives:

- delta = 0 deg: arg(S21/S12) = -0.00311572 rad
- delta = 90 deg: arg(S21/S12) = +5.24396e-5 rad
- delta = 180 deg: arg(S21/S12) = +0.00321933 rad
- delta = 270 deg: arg(S21/S12) = +5.67876e-5 rad

Thus the direct finite-device nonreciprocal phase reverses sign between 0 and 180 degrees and falls near the small finite-frequency/background level around 90 and 270 degrees.

This is a direct terminated-device reciprocity test rather than a restatement of the bulk k-retrieval.

## Test 2 — Functional-form selection for u dependence

The discrete Floquet bulk model was evaluated over

    u = 0.05 to 0.70

with

- f0/fm = 0.02
- N = 192
- H = 4
- m_e = m_m = 0.10

At every u, the delta dependence was separately fit to extract the phase-law amplitude A(u).

Four candidate velocity dependences were then fit with one overall scale parameter:

1. u
2. u/(1-u)
3. u/(1-u^2)
4. u/(1-u^2)^(3/2)

Results:

| Candidate | Best-fit scale | SSE | RMSE | AIC | Max pointwise relative error |
|---|---:|---:|---:|---:|---:|
| u/(1-u^2) | 0.005033 | 2.145e-9 | 1.238e-5 | -314.39 | 0.595% |
| u/(1-u) | 0.003145 | 7.937e-7 | 2.381e-4 | -231.60 | 34.0% |
| u/(1-u^2)^(3/2) | 0.003929 | 1.140e-6 | 2.854e-4 | -226.52 | 21.4% |
| u | 0.007629 | 5.827e-6 | 6.452e-4 | -203.69 | 52.1% |

The selected prefactor 0.005033 is close to the analytic weak-order coefficient

    m_e m_m / 2 = 0.005.

If that analytic coefficient is fixed rather than fitted, the Dorian prediction

    A(u) = 0.005 * u/(1-u^2)

has a mean absolute relative error of approximately 0.287% and a worst pointwise relative error of approximately 1.14% over u = 0.05 to 0.70.

The nearest competing functional form has an SSE roughly 370 times larger than u/(1-u^2).

## Current conclusion

These two tests directly target the CRTFE-HCM weak-order phase relation rather than the simulator's internal energy identity.

Within the tested bounded subluminal regime, the model survives both:

- a terminated-device signed nonreciprocity phase sweep; and
- explicit functional-form competition for the u dependence.

The result remains numerical. It does not validate hardware behavior, real material loss, fabrication tolerance, or the unresolved near-luminal multiband regime.

The direct energy-balance closure should remain in the record only as a simulator consistency/unit test, not as a physics falsification gate.
