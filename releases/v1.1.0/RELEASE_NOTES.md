# CRTFE-HCM v1.1.0 release notes

**Release scope:** reproducibility and independent clean-room review package for the Dorian Phase Relation carrier-transferability result and the current near-luminal mathematical branch.

**Author:** Dorian Charles Martin-Smith  
**ORCID:** 0009-0008-9926-6840  
**Related prior Zenodo record:** 10.5281/zenodo.22681634

The authoritative source snapshot for this release is the commit referenced by the `v1.1.0` Git tag. Do not substitute an earlier pre-release commit for the tagged release.

## What is frozen

- exact canonical 48-C/48-L topology;
- fixed-K modulation convention (`Kd=pi/6`, with sign reversal for negative `u`);
- `H=15` carrier-transferability solver;
- training/held-out split and acceptance thresholds;
- complete complex sideband output for the reproduced reference run;
- expected carrier-transferability scores and model-selection result;
- the failed fixed-`f_m`, varying-`K` control path documented as known-invalid;
- pinned Python/package versions used for the reproduction workflow;
- a two-page clean-room reproduction brief;
- one-command reproduction and verification workflow.

## Reference verdict

The frozen Stage 1A carrier-level held-out transferability criteria pass. The release does **not** claim completed reduced-effective-model prediction of every held-out Floquet sideband.

## Evidence boundary

This is a numerical/theoretical release. It does not claim experimental hardware validation, measured isolation, insertion loss, efficiency, gain, stability, or other RF hardware performance.

## DOI linkage

This release is prepared for deposit as Zenodo version 1.1.0. The new version-specific DOI must be recorded only after Zenodo actually mints it; until then, `10.5281/zenodo.22681634` remains the related prior record, not the DOI of this software/reproducibility release.
