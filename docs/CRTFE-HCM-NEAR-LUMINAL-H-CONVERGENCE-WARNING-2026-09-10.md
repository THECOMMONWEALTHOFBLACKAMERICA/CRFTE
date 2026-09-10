# CRTFE-HCM — Near-Luminal H-Convergence Warning

**Author:** Dorian Martin-Smith  
**Date:** 10 September 2026  
**Status:** Numerical warning / unresolved characterization.

A follow-on attempt was made to classify the near-luminal CRTFE-HCM region after the finite-ladder energy gate closed.

The existing transfer-matrix branch tracker was swept across approximately `u = 0.50 ... 0.95` while the retained Floquet harmonic order `H` was increased.

The apparent attenuation/gap onset did **not** converge to a stable interval. Representative behavior changed materially with `H`, including cases where the apparent onset moved from roughly `u ~ 0.92` at low order to much lower `u` at higher order, while branch identity and attenuation magnitude also changed substantially.

Therefore the present calculation does not support a claim of a converged directional stopband, nonreciprocal bandgap, mode coalescence, or unidirectional branch near the luminal regime.

The appropriate conclusion is:

\[
\boxed{\text{The current transfer-matrix branch tracker is not sufficient to classify the near-luminal multiband region.}}
\]

Possible causes include branch-tracking ambiguity and numerical conditioning of high-order transfer-matrix products. A better-conditioned generalized eigenvalue or finite-scattering formulation is required.

This warning does not alter the bounded low/moderate-`u` effective-medium results around the intended V1 regime. It prevents those results from being extrapolated into the unresolved near-luminal region.
