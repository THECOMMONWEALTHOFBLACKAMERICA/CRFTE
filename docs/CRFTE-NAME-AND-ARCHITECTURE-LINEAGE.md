# CRFTE Name and Architecture Lineage

**Status:** canonical naming and architecture record  
**Date:** 2026-08-25

## Canonical naming rule

`CRFTE` is retained as the program identifier and repository name.

The initials originated from **Counter-Rotating Field Thrust Engine**, which describes the earliest propulsion concept explored by the project.

That phrase is now historical. It must not be used as a literal description of the current P4 propulsion mechanism.

## Why the meaning changed

The program was intentionally allowed to evolve when reduced-order modeling exposed weaknesses in earlier counter-rotating / traveling-field assumptions.

The current primary mechanism no longer requires counter-rotating multi-tesla propulsion fields. Instead it separates the propulsion magnetic field from the current-generation mechanism and asks whether a controlled conductive atmospheric stream can receive useful momentum through direct Lorentz body force.

Current physical core:

```text
flowing atmospheric air
        +
controlled transient conductivity
        +
transverse current J
        +
predominantly stationary magnetic field B
        ↓
J × B body force
        ↓
neutral-air momentum transfer
```

## Program hierarchy

### CRFTE

The overall research program and historical lineage.

### P4 — Atmospheric Electromagnetic Propulsion architecture

The current vehicle-scale theoretical architecture. It uses a large atmospheric-air mass flow, controlled plasma conductivity, current drive, and a predominantly static magnetic field.

P4A, P4B and P4C are current-drive refinements within this architecture.

### P4D

The high-repetition-rate plasma-conditioning research branch investigating whether attachment and recombination losses can be reduced enough to make P4 energetically useful.

### P4E

The current grant-scale proof-of-physics experiment. P4E is **not the finished vehicle engine**. It tests the plasma/MHD question that must pass before P4 vehicle scaling is justified.

## Historical branches

Earlier counter-rotating-field, traveling-field and V5 induction-MHD records remain in the repository for traceability and comparison.

They are not current design requirements unless a later quantitative model demonstrates a superior force, power, mass, stability or control result.

Historical filenames are not renamed when doing so would damage research traceability. A filename containing `CRTFE`, `counter-rotating`, or `traveling-field` therefore does not imply that the mechanism remains current.

## Required wording in current documents

Preferred:

> **CRFTE Atmospheric Electromagnetic Propulsion Research Program**

For the current mechanism:

> **P4 Atmospheric Electromagnetic Propulsion architecture**

For the immediate experiment:

> **P4E grant-scale atmospheric plasma/MHD proof-of-physics experiment**

Historical wording may say:

> **CRFTE originated as the Counter-Rotating Field Thrust Engine concept.**

Avoid wording that states or implies:

- the current engine requires counter-rotating magnetic fields;
- P4E is already a complete propulsion engine;
- the 300–500 mph vehicle target is demonstrated performance;
- successful Lorentz-force laboratory data automatically establishes aircraft feasibility.

## Scientific interpretation

The architecture change is not treated as abandonment of the project goal. The goal remains direct electromagnetic momentum transfer into a large atmospheric-air mass flow without conventional rotors, propellers, turbines or mechanical compressors.

What changed is the proposed mechanism for reaching that goal.

That distinction is deliberate: **the program identity remains stable while the mechanism is allowed to change when modeling or experiments require it.**
