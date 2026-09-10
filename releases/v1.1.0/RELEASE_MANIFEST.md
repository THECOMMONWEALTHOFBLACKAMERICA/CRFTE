# CRTFE-HCM v1.1.0 Release Manifest

**Source commit:** `776a58b4218aeabf477d4e4b62b32aa898c1e68d`  
**Archive filename:** `CRTFE-HCM-v1.1.0-reproducibility-release.zip`  
**Archive SHA-256:** `eb466d27eb02f8ec89f881b407b33ded88a5bf745bf287dc7ee468b5581f7def`  
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
- `MANIFEST_SHA256.txt` covering every file in the archive;
- `FULL_REPRODUCTION_VERIFICATION.txt` recording the completed 176-condition solver rerun and verifier results.

## Frozen reference environment

- Python `3.13.5`
- NumPy `2.3.5`
- SciPy `1.17.0`
- pandas `2.2.3`
- Matplotlib `3.10.8`

## One-command contract

`./reproduce.sh` creates a virtual environment, installs the pinned direct dependencies, reruns the fixed-K carrier-transferability calculation, writes `reproduced/`, and evaluates the frozen acceptance criteria. `./reproduce.sh --verify-reference` checks the shipped reference score/model-selection files without rerunning the solver.

The complete numerical solver path was also rerun end-to-end over all **176 conditions** using the frozen package versions already present in the execution environment. All six acceptance gates passed and all headline reproduced values matched the reference values within the verifier tolerances. The sandbox itself had no outbound package-network access, so the initial `pip install` download step was not part of that execution; this limitation is recorded rather than hidden.

## Evidence boundary

This is a numerical/theoretical reproducibility release. It does not claim experimental hardware validation, isolation, insertion loss, efficiency, gain, or completed full-sideband reduced-effective-model transferability.
