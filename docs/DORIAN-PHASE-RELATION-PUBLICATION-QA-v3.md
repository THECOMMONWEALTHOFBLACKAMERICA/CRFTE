# Dorian Phase Relation v3.0.0 - Publication QA markup

This note records OCR/text-extraction artifacts reported during final review and distinguishes them from the actual publication source. No mathematical erratum is required for these items because the Markdown source and rendered PDF use the correct expressions.

| Reported extraction artifact | Correct publication expression | Status |
|---|---|---|
| Schur complement shown with `delta` instead of `S`, with reordered factors | `S = L_00 - L_0Q L_QQ^{-1} L_Q0` | Source/PDF already correct; OCR artifact |
| `delta^{-1}` / `delta_11` for the Schur complement | `S^{-1}` / `S_11` | Source/PDF already correct; OCR artifact |
| Repeated transformed-Schur-complement symbol | `S~_11 = S_11 = Q` | Source/PDF already correct in meaning; extraction artifact |
| Complement-to-carrier block shown as `L~_00` | `L~_Q0 = -eta D_Q T_Q0` | Source/PDF already correct; OCR artifact |
| `u_xi^(2)` and `u_xi^(4)` | `u * xi_tilde^(2)` and `u * xi_tilde^(4)` | Source/PDF already correct; OCR artifact |
| Scope list extracted with repeated numeral 1 | Standard Markdown bullet list | Source/PDF already correct; extraction/list artifact |
| Corrupted boundary-factor expression | `ell^T T_+ = ell^T T_- = (0,beta a/2)` | Source/PDF already correct; OCR artifact |
| Final boxed branch inequality reported with a missing closing brace | `0 < u < 1/sqrt((1+a)(1+b))` in a complete box | Source/PDF already correct; OCR artifact |

## Final content changes after review

1. Added one consolidated verification subsection covering the O(2), O(4), O(20), and `a <-> b` checks.
2. Clarified that `worst_case_phase_deg = 0.0` in the unequal-depth CSV is a theorem prediction, not an empirical phase scan.
3. Retained the explicit complement-block invertibility implication from the positive majorant.
