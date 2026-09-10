# CRTFE-HCM v1.1.0 Release Manifest

**Git tag:** `v1.1.0`  
**Tagged source commit:** `149ce17ffbdcda00243a17583e4837c0ee0098e9`  
**GitHub release:** `https://github.com/THECOMMONWEALTHOFBLACKAMERICA/CRFTE/releases/tag/v1.1.0`  
**Archive filename:** `CRTFE-HCM-v1.1.0-reproducibility-release.zip`  
**Release-asset SHA-256:** `3721dc604f12a3ac5818a0c39c031a0d2439cb6083bde604158a475a00a8d86b`  
**Archive size:** `1,142,236 bytes`  
**Clean-room PDF SHA-256:** `574f5c743d6a95a17964a7eefc1a60a98778bca4367edc88c1d617bd08e0be1e`  
**Related prior DOI:** `10.5281/zenodo.22681634`  
**New version DOI:** pending Zenodo mint; do not preassign.

## Archive contract

The tagged release archive contains:

- version/source/citation metadata;
- the exact canonical `N`-C / `N`-L topology, including the 48-C/48-L reference topology with the final inductor feeding the right termination;
- the frozen Python/package environment;
- fixed-`K` transferability protocol and exact held-out split;
- harmonic-balance, reproduction, and verification code;
- complete complex `h=-15..15` sideband output from the reproduced reference run;
- expected held-out/model-selection/control/convergence outputs;
- the invalid fixed-`f_m`, varying-`K` path documented as a negative-control failure mode;
- transferability and near-luminal technical notes available at the tagged source snapshot;
- the clean-room reproduction brief in Markdown and exactly two-page PDF form;
- `reproduce.sh` for one-command reproduction;
- `MANIFEST_SHA256.txt` covering the archive contents;
- `FULL_REPRODUCTION_VERIFICATION.txt` from the release-build rerun.

## Frozen reference environment

- Python `3.13.5`
- NumPy `2.3.5`
- SciPy `1.17.0`
- pandas `2.2.3`
- Matplotlib `3.10.8`

## Reproduction and release verification

GitHub Actions run `34480316545` installed the frozen environment, reconstructed the predeclared fixed-`K` split, verified its SHA-256 as `1abef1d3586e937fd57049719cd3f29cd8495bb80ab4d66eff64beb343e24123`, reran the complete frozen condition set, passed the six headline Stage 1A acceptance gates, built the deterministic archive, and published the `v1.1.0` release.

The six headline gates are: median non-null relative error <=5%; p95 <=10%; worst <=20%; median absolute carrier-phase error <=`2e-4 rad`; p95 carrier-phase error <=`5e-4 rad`; and `u/(1-u^2)` must have the lowest held-out SSE among the tested velocity laws under identical treatment.

## Evidence boundary

This is a numerical/theoretical reproducibility release. A PASS means the frozen fixed-`K` carrier-level transferability result reproduces. It does not claim experimental hardware validation, measured isolation, insertion loss, efficiency, gain, stability, or completed full-sideband reduced-effective-model transferability.
