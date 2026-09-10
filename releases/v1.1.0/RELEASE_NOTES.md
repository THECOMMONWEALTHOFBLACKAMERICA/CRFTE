# CRTFE-HCM v1.1.0 release notes

**Release scope:** reproducibility and independent-clean-room review package for the Dorian Phase Relation and the current near-luminal mathematical branch.

**Source repository head:** `776a58b4218aeabf477d4e4b62b32aa898c1e68d`

## What is frozen

- exact canonical 48-C/48-L topology;
- fixed-K modulation convention (`Kd=pi/6`, with sign reversal for negative `u`);
- `H=15` carrier-transferability solver;
- training/held-out split and acceptance thresholds;
- complete complex sideband output for the reference run;
- current expected carrier-transferability scores and model-selection result;
- the failed fixed-`f_m`, varying-`K` implementation retained as a known-invalid control path;
- Python/package versions used to generate the reference outputs.

## Evidence boundary

This release supports a **numerical/theoretical** Stage 1A carrier-level transferability result. It does not claim experimental hardware validation or a completed reduced effective-medium prediction of every held-out Floquet sideband.

## DOI linkage

The related Zenodo record is `10.5281/zenodo.22681634`. This archive is prepared for deposit as version 1.1.0; the new version-specific DOI must be inserted after Zenodo mints it.
