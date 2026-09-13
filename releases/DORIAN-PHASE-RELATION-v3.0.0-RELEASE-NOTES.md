# Dorian Phase Relation v3.0.0 — Release notes

**Date:** 12 September 2026  
**Author:** Dorian Martin-Smith

## Major result

This release advances the Dorian Phase Relation from the weak-order phase law to an **all-orders phase-uniform truncation theorem for the stated local sinusoidal continuum model**.

### Added

- Exact laboratory-frame matrix representation.
- Fourier-space carrier/complement Schur-complement derivation.
- Positive first-return representation.
- Explicit eta grading: two external O(eta) vertices plus 2N-2 interior vertices at order 2N.
- All-orders vanishing of odd total modulation orders.
- Exact phase-harmonic ceiling r_max=N at total order 2N.
- Nonnegative phase-harmonic coefficients on the regular subluminal branch.
- Phase-uniform truncation theorem: the maximum absolute remainder of every finite even-order approximation occurs at delta=0.
- Exact unequal-depth in-phase solution.
- Explicit O(8)/O(10) formulas and an exact sparse sign audit through O(20).
- Discrete quadratic-susceptibility tomography and two-parameter continuum-limit refinement.

## Scope

The theorem applies to the local sinusoidal continuum model only. It does not establish the same result for arbitrary waveforms, finite staggered ladders, lossy/dispersive devices, near-luminal multiband regimes, or hardware.

## Zenodo lineage

Earlier public mathematical note: DOI **10.5281/zenodo.22681634**.

Recommended release tag: \`dorian-phase-relation-v3.0.0\`.


## Final pre-publication referee closure

The final manuscript makes three proof obligations explicit:

- \(T_{\mathsf Q}=\mathsf Q T\mathsf Q\), so intermediate carrier revisits are projected out and the Schur-complement expansion is genuinely first-return.
- \(\rho(T_{\rm abs})<1\) implies convergence of the complement Neumann series and therefore invertibility of \(I-T_{\mathsf Q}\) and \(\mathcal L_{\mathsf Q\mathsf Q}\) throughout the stated branch.
- The exact unequal-depth in-phase coefficient is included explicitly in the manuscript, matching the abstract.

The branch inequality is independent of relative phase \(\delta\), making the meaning of **phase-uniform** explicit.


## Consolidated verification summary

The final theorem manuscript now groups four independent/structurally distinct checks in one place:

- exact recovery of the earlier O(2) Dorian relation from the shortest first-return paths;
- exact recovery of the independently derived general unequal-depth O(4) term;
- exact sparse sign audit through O(20), with zero wrong-sign monomial coefficients at every audited order;
- numerical `a <-> b` symmetry of the unequal-depth validity map.

The unequal-depth validity caption also states explicitly that `worst_case_phase_deg = 0.0` is imposed by the theorem, not discovered by an empirical phase scan.

See also: [publication QA markup](../docs/DORIAN-PHASE-RELATION-PUBLICATION-QA-v3.md).
