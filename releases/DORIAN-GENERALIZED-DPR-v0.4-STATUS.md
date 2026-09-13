# Generalized Dorian Phase Relation v0.4 — repository status

**Date:** 2026-09-13  
**Status:** referee-ready working extension; not yet a separately published DOI release.  
**Published baseline:** Dorian Phase Relation v3.0.0 sinusoidal-continuum theorem, reserved Zenodo DOI 10.5281/zenodo.22731518.

## Current generalized result

The post-v3 generalized framework now contains:

- an exact multi-harmonic transition-kernel derivation from the constitutive matrix;
- exact carrier / Schur / first-return identification;
- a positive-spectrum theorem with active-harmonic ceiling
  `H_* floor(n/2)`;
- an exact signed zero-sum criterion for odd-order onset;
- a Perron-weighted `ell^1` convergence proof and phase-uniform remainder equality for nonnegative co-phased spectra;
- a spectral-envelope inequality for arbitrary intrinsic Fourier phases;
- phase-origin covariance with non-unique maximizers;
- a full integer relation-lattice holonomy criterion.

## Independent adversarial review

The first adversarial audit returned **B — needs specific repairs**. Those repairs were implemented and re-audited.

The re-audit reproduced all three executable suites and returned:

**A — theorem-ready**

No counterexample was found inside the stated hypotheses.

This is an external adversarial audit of a working mathematical extension, not journal peer review.

## Reproducibility

Local frozen audit package SHA-256:

`e3cffc1a2be90f3a7b5100148728afe121fd7a0e59885c6619c32c6c5bc72517`

The repository stores the text theorem and executable audit scripts separately so the generalized result can be reviewed without changing the published v3 lineage.

## Scope boundary

The generalized theorem does not by itself cover loss, constitutive dispersion, nonlocality, finite staggered ladders, near-luminal multiband physics, or hardware.
