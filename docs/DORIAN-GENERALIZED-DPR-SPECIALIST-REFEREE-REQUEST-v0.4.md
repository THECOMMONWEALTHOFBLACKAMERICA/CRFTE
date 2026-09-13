# Specialist referee request — Generalized DPR v0.4

This package has completed one B→A adversarial repair cycle.

Please do not assume the A verdict is correct. Independently review the theorem.

## Reproduce

Run the three audit scripts in `analysis/`:

- `dorian_generalized_dpr_audit_v01.py`
- `dorian_generalized_dpr_audit_adversarial_v02.py`
- `dorian_generalized_dpr_audit_repairs_v03.py`

## Primary manuscript

`docs/DORIAN-GENERALIZED-DPR-WORKING-THEOREM-v0.4.md`

## Required mathematical checks

- explicit kernel derivation from the constitutive matrix;
- continuum/carrier/Schur/first-return identification;
- Perron-weighted ell1 convergence and complement invertibility;
- sharp active-harmonic ceiling;
- positive-spectrum worst-phase equality;
- arbitrary-phase spectral-envelope inequality;
- phase-origin covariance with non-unique maximizers;
- full relation-lattice holonomy criterion;
- odd-order signed-zero-sum onset theorem.

Try to produce an in-hypothesis counterexample.

Classify the package as:
A. theorem-ready
B. needs specific repairs
C. major proof gap
D. false
