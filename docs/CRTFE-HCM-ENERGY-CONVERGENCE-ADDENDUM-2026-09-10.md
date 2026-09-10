# CRTFE-HCM — Energy-Gate Numerical Convergence Addendum

**Author:** Dorian Martin-Smith  
**Date:** 10 September 2026  
**Status:** Public numerical validation addendum; theoretical/numerical only.

## Question

The original finite-ladder energy-gate report showed that

\[
P_{\rm in}+P_{\rm pump}-P_{\rm out}-\frac{dU}{dt}\rightarrow 0
\]

under tighter numerical settings, but its short convergence table changed both integration resolution and settling duration between runs.

That table therefore did not isolate which numerical variable controlled the reported improvement.

This addendum separates the variables.

The physical model is unchanged:

- `N = 48`
- `M = 4`
- `L0 = 625 nH`
- `C0 = 250 pF`
- `m_e = m_m = 0.10`
- `f_m = 3 MHz`
- `f_0 = 150 kHz`
- `delta = 0`
- 50-ohm source and load

## 1. Averaging/quadrature convergence at fixed dynamics

The ODE solution was held at 80 maximum integration steps per pump period and 10 carrier-period settling intervals. Only the number of samples used to evaluate the final one-carrier-period power integrals was changed.

| Evaluation samples | Relative closure residual |
|---:|---:|
| 501 | `-4.17e-9` |
| 1,001 | `-9.79e-10` |
| 2,001 | `-2.42e-10` |
| 4,001 | `-6.02e-11` |
| 8,001 | `-1.50e-11` |
| 16,001 | `-3.70e-12` |
| 32,001 | `-8.75e-13` |

Each doubling of the evaluation sample count reduces the residual by approximately a factor of four. This is the expected second-order convergence of trapezoidal quadrature for the smooth periodic signals being integrated.

Therefore the residual in the previously reported long-settled energy balance was dominated by numerical averaging error, not by an unaccounted physical power term.

## 2. ODE integration-resolution convergence at fixed settling

Settling was fixed at 10 carrier periods and the final power integration was fixed at 16,001 evaluation samples. Only the maximum ODE step size was changed through the number of allowed points per modulation period.

| Points per pump period | Relative closure residual |
|---:|---:|
| 10 | `-2.75e-8` |
| 15 | `-3.38e-10` |
| 20 | `+4.15e-10` |
| 30 | `+3.42e-10` |
| 40 | `+2.34e-11` |
| 60 | `-3.11e-12` |
| 80 | `-3.70e-12` |
| 120 | `-3.71e-12` |

The result is effectively converged by approximately 60 points per pump period under these tolerances. Beyond that point the residual reaches the floor imposed by the fixed evaluation quadrature.

## 3. Settling convergence measured independently

Settling should not be inferred from the energy-closure residual itself.

The conservation identity is valid during transients as well as at steady state. Settling is instead required for the later Floquet sideband/scattering extraction, which assumes a periodic steady response.

Accordingly, settling was tested with a separate diagnostic:

\[
\epsilon_{\rm periodic}
=
\frac{\|y(t+T_0)-y(t)\|}
{\max(\|y(t+T_0)\|,\|y(t)\|)}.
\]

At fixed 80-points-per-pump integration resolution:

| Settling periods | Relative state-periodicity error |
|---:|---:|
| 1 | `6.75e-3` |
| 2 | `4.87e-3` |
| 4 | `2.85e-3` |
| 6 | `1.89e-3` |
| 8 | `1.15e-3` |
| 10 | `7.11e-4` |
| 12 | `5.07e-4` |
| 14 | `3.05e-4` |
| 16 | `1.88e-4` |
| 18 | `1.35e-4` |
| 20 | `8.2e-5` |

The periodicity error decreases monotonically with settling duration.

This separates two numerical requirements that were previously mixed together:

\[
\boxed{\text{quadrature / ODE resolution controls energy-closure accuracy}}
\]

while

\[
\boxed{\text{settling duration controls steady-periodic Floquet extraction}}
\]

to the accuracy relevant here.

## Conclusion

The earlier resolution/settling confound is resolved.

The direct energy-closure result does not depend on extra settling to make the conservation law hold. At fixed settling, the power-balance residual converges with both ODE resolution and evaluation quadrature. At fixed numerical resolution, the state independently approaches a periodic steady response as settling duration is increased.

For the tested V1 numerical ladder, no unresolved energy term appears when these variables are separated.

This addendum does not change the existing experimental boundary: no hardware isolation, insertion-loss, efficiency, or gain result has been demonstrated.
