# CRTFE-HCM Clean-Room Reproduction Brief - v1.1.0

**Author:** Dorian Charles Martin-Smith | **ORCID:** 0009-0008-9926-6840  
**Related DOI:** 10.5281/zenodo.22681634  
**Scope:** independent numerical reproduction of the Dorian Phase Relation carrier-level transferability result. Numerical/theoretical only.

## 1. Exact topology

Canonical device: exactly **48 shunt capacitors and 48 series inductors**. Nodes are `V[0]..V[47]`. Each `C_n(t)` connects node `n` to ground. `L_0` connects node 0 to node 1; ...; `L_46` connects node 46 to node 47; **`L_47` connects node 47 to the right termination**. Left incidence uses a Thevenin source through `ZL`; reverse incidence uses the corresponding right-side source through `ZR`. Canonical values: `C0=250 pF`, `L0=625 nH`, `m_e=m_m=0.10`, `ZL=ZR=50 ohm`. Transferability lengths use the same per-cell topology: always `N` capacitors and `N` inductors.

A 48-C/47-L ladder with the load attached directly to the last capacitor is a different topology and is not an acceptable reproduction.

## 2. Modulation and sign conventions

Use `y(t)=sum_h y_h exp(+i(omega0+h*Omega)t)`, `h=-H..H`; reference `H=15`.

`C_n(t)=C0[1+m_e cos(kappa*n - Omega*t)]`

`L_n(t)=L0[1+m_m cos(kappa*(n+1/2) - Omega*t + delta)]`

The half-cell magnetic offset is physical. Accepted velocity scaling holds **`kappa=Kd=+pi/6` fixed** for positive `u`; use `-pi/6` for traveling-modulation reversal. Change `f_m` to set `u`, not `K`: `f_m=|u|*(pi/6)/(2*pi*sqrt(L0*C0))`; `f0=r*f_m`.

Port currents point into the device. Voltage waves are `a=(v+Zi)/2`, `b=(v-Zi)/2`. For unequal terminations use `S21=(b_R/a_L)*sqrt(ZL/ZR)` and `S12=(b_L/a_R)*sqrt(ZR/ZL)`. Preserve signed phase. Primary observable: `phi_nr=arg(S21/S12)` and `xi_hat=-phi_nr/[2*N*omega0*sqrt(L0*C0)]`.

## 3. Required observables

For **both left and right carrier incidence**, record complete complex Floquet scattering for every retained `h`: output port, real/imaginary S, magnitude, phase, and physical sideband frequency. Report carrier `S21^(0)`, `S12^(0)`, `arg(S21/S12)`, and retrieved `xi_hat`. Do not validate from carrier magnitude alone. Retain the full converged sideband vectors even though v1.1.0 claims only carrier-level transferability.

## 4. Mandatory null/symmetry controls

1. Static: `m_e=m_m=0` -> carrier reciprocity to numerical tolerance and no modulation sidebands.
2. Electric-only: `m_m=0` -> leading `m_e*m_m` cross-term vanishes; only the known small finite-frequency residual may remain.
3. Magnetic-only: `m_e=0` -> same requirement.
4. Phase reversal: `delta -> delta+pi` -> leading directional term reverses sign.
5. Quadrature null: `delta=90 deg,270 deg` -> leading `cos(delta)` term vanishes.
6. Modulation reversal: `kappa -> -kappa` -> directional response reverses sign.
7. Load swap: exchange `ZL,ZR` -> boundary response transforms while the retrieved bulk carrier term remains approximately invariant after proper normalization/de-embedding.
8. Harmonic convergence: increase `H`; carrier terms of appreciable magnitude must change by `<1e-4` relatively, weak sidebands by `<1e-7` absolutely, and `arg(S21/S12)` must be stable.

## 5. Acceptance criteria

Freeze the supplied training/held-out split before scoring. Primary model: `xi=0.005*u/(1-u^2)*cos(delta)+D*r^2`; only `D` is fit on training for the analytic-coefficient test.

Held-out PASS requires: median non-null relative error <=5%; 95th percentile <=10%; worst <=20%; median absolute carrier-phase error <=`2e-4 rad`; 95th percentile <=`5e-4 rad`; and `u/(1-u^2)` must have the lowest held-out SSE against `u`, `u/(1-u)`, and `u/(1-u^2)^(3/2)` under identical treatment.

Reference v1.1.0 outcome: 96 held-out conditions; median relative error ~2.624%; p95 ~6.806%; worst ~10.384%; median phase error ~`8.67e-6 rad`; p95 phase error ~`4.72e-4 rad`. The one-time-fit global coefficient is ~`0.0051064` versus analytic `0.005`. These are expected outputs, not thresholds to tune toward.

## 6. Known failure modes

**Invalid fixed-f_m / varying-K path:** holding `f_m` fixed while varying `K` to change `u` changes `Kd` and therefore the discrete spatial modulation geometry. At `u=0.05` the failed implementation reached about `270 deg/cell`; it failed held-out scoring and is intentionally retained as a negative control. The accepted path holds `Kd=pi/6` fixed and varies `f_m`.

Also reject: 48-C/47-L topology substitution; dropping the inductor half-cell phase; erasing propagation sign; unequal-load S comparison without power normalization; per-condition refitting; insufficient `H` near high `u`; treating direct energy closure as independent validation; treating Floquet pseudounity as proof of passivity/stability/nonreciprocity; extrapolating the weak Dorian relation through the near-luminal singular layer; or claiming hardware isolation/gain/efficiency from numerical data.

## 7. One-command reproduction

From the unpacked v1.1.0 archive run `./reproduce.sh`. It creates a local virtual environment, installs the pinned dependencies, reruns the frozen fixed-K transferability set, writes `reproduced/`, and executes the acceptance verifier. `./reproduce.sh --verify-reference` checks only the shipped reference outputs.

**Verdict boundary:** a PASS means the fixed-K **carrier-level** held-out transferability criteria reproduce. It does not mean full-sideband reduced-effective-model validation or experimental RF hardware validation.