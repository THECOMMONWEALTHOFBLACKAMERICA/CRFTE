# CRTFE-HCM v1.1.0 Release Manifest

**Source commit:** `776a58b4218aeabf477d4e4b62b32aa898c1e68d`  
**Archive filename:** `CRTFE-HCM-v1.1.0-reproducibility-release.zip`  
**Archive SHA-256:** `7529d5a844d0e56de42e1c46778d6c8022892a812f3a88acd61c9f9726f309b7`  
**Related prior DOI:** `10.5281/zenodo.22681634`  
**New version DOI:** pending Zenodo mint; do not preassign.

## Archive contract

The archive contains:

- `VERSION`, `SOURCE_COMMIT`, `CITATION.cff`, `ZENODO_METADATA_v1.1.0.json`;
- `topology/topology.json` and `topology/TOPOLOGY.md`;
- `environment/requirements-lock.txt` and `environment/runtime.json`;
- `protocol/transferability_protocol_fixedK.json` and `protocol/heldout_split_fixedK.json`;
- harmonic-balance, reproduction, verification, and near-luminal Python code;
- `data/raw/full_sidebands_fixedK.csv.gz`, the complete complex `h=-15..15` reference sideband data;
- condition summary and expected held-out/model-selection/control/convergence tables;
- the invalid fixed-`f_m`, varying-`K` implementation and failed scores as a negative-control record;
- transferability and near-luminal technical notes;
- `CLEAN_ROOM_REPRODUCTION_BRIEF.md` plus an exactly two-page PDF brief;
- `reproduce.sh` and `EXPECTED_OUTPUTS.json`;
- `MANIFEST_SHA256.txt` covering every file in the archive.

## Frozen reference environment

- Python `3.13.5`
- NumPy `2.3.5`
- SciPy `1.17.0`
- pandas `2.2.3`
- Matplotlib `3.10.8`

## One-command contract

`./reproduce.sh` creates a virtual environment, installs the pinned direct dependencies, reruns the fixed-K carrier-transferability calculation, writes `reproduced/`, and evaluates the frozen acceptance criteria. `./reproduce.sh --verify-reference` checks the shipped reference score/model-selection files without rerunning the solver.

## Reference self-check

The packaged reference verifier returns PASS for all six headline checks: median, p95, and worst relative error; median and p95 phase error; and the requirement that `u/(1-u^2)` have the lowest held-out SSE among the tested velocity laws.

## Evidence boundary

This is a numerical/theoretical reproducibility release. It does not claim experimental hardware validation, isolation, insertion loss, efficiency, gain, or completed full-sideband reduced-effective-model transferability.