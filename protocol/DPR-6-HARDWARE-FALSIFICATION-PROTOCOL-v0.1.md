# DPR-6 PRE-REGISTERED BENCH FALSIFICATION PROTOCOL

**Project:** Dorian Phase Relation (DPR) Hardware Demonstrator  
**Device:** DPR-6 Six-Cell Time-Modulated Analog Transmission-Line Demonstrator  
**Protocol Version:** 0.1  
**Status:** PRE-REGISTERED BEFORE MODULATED HARDWARE TESTING  
**Investigator:** Dorian Martin-Smith  
**Date Frozen:** 2026-09-13  
**Repository / Archive Location:** THECOMMONWEALTHOFBLACKAMERICA/CRFTE  
**SHA-256 of Frozen Protocol:** recorded in the companion `.sha256` file.

---

## 1. Purpose

The purpose of this experiment is to test whether a physical time-modulated electronic analogue of the stated CRTFE-HCM continuum model exhibits the phase-dependent coupling predicted by the Dorian Phase Relation.

The experiment is designed as a falsification test rather than a demonstration.

The leading-order DPR prediction is

\[
\boxed{
\tilde\xi_D(\delta)
=
\frac{m_em_m}{2}
\frac{u}{1-u^2}
\cos\delta
}
\]

where

\[
u=\frac{\Omega}{Kc_m}.
\]

Here \(m_e\) is the electric-channel modulation depth, \(m_m\) is the magnetic-channel modulation depth, \(\Omega\) is temporal modulation angular frequency, \(K\) is spatial modulation wavenumber, \(c_m\) is measured unmodulated ladder wave velocity, and \(\delta\) is relative modulation phase.

No experimental result will be interpreted before the predictions, candidate models, controls, and failure criteria below are frozen.

---

## 2. Experimental claim being tested

Primary hypothesis:

> A physical two-channel time-modulated transmission-line analogue will exhibit a signed nonreciprocal response whose leading dependence on relative modulation phase is proportional to \(\cos\delta\).

This experiment does **not** test whether electromagnetism can move air, produce propulsion, or establish DPR as a universal law of physics.

A successful result would support:

> The Dorian Phase Relation has been experimentally observed in a physical time-modulated electronic analogue of the stated continuum model.

---

## 3. Device architecture

The test article will contain six spatial cells.

\[
C_n(t)=C_0[1+m_e\cos(\kappa n-\Omega t)]
\]

\[
L_n(t)=L_0[1+m_m\cos(\kappa n-\Omega t+\delta)]
\]

with

\[
\boxed{\kappa=\frac{2\pi}{6}=60^\circ}
\]

per cell.

Thus

\[
\phi_{E,n}=60^\circ n,
\qquad
\phi_{M,n}=60^\circ n+\delta.
\]

The electronic implementation may use voltage-controlled transconductance elements or equivalent analog circuitry, but the programmed state equations must preserve two independently controlled traveling modulation channels.

---

## 4. Mandatory Stage 0: measure the unmodulated device first

No DPR phase sweep will be interpreted until the unmodulated ladder has been characterized.

Set

\[
m_e=m_m=0.
\]

Measure the unmodulated transmission response over the intended carrier-frequency range.

The effective propagation velocity \(c_m\) will be obtained using either time-of-flight or calibrated phase-versus-frequency propagation measurements. The actual method must be recorded before proceeding.

Measured value:

\[
\boxed{c_m=\_\_\_\_\_\_\_\_\_\_}
\]

Measured uncertainty:

\[
\boxed{\sigma_{c_m}=\_\_\_\_\_\_\_\_\_\_}
\]

Then calculate

\[
\boxed{u=\frac{\Omega}{Kc_m}}.
\]

No assumed or simulated value of \(c_m\) may replace the measured value in the primary analysis.

---

## 5. Pre-registered regularity boundary

For each experimental condition, the DPR continuum theorem requires

\[
\boxed{
0<u<
\frac{1}{\sqrt{(1+m_e)(1+m_m)}}
}.
\]

Every primary DPR data point must satisfy this condition using measured \(c_m\).

Any point outside this branch will be labeled **OUTSIDE PRE-REGISTERED DPR TEST DOMAIN** and will not be counted as evidence for or against the primary theorem.

Initial target operating range:

\[
0.05\le u\le0.40.
\]

Initial modulation depths:

\[
0.05\le m_e\le0.10,
\qquad
0.05\le m_m\le0.10.
\]

---

## 6. Primary observable

For each operating condition, transmission will be measured in both directions.

\[
\boxed{
\phi_{\rm NR}
=
\arg\left(\frac{S_{21}}{S_{12}}\right)
}
\]

The exact calibration factor mapping \(\phi_{\rm NR}\) to \(\tilde\xi\) is device-dependent.

Therefore the primary hardware test does **not** assume

\[
\phi_{\rm NR}=\tilde\xi.
\]

It tests whether the **signed nonreciprocal response** follows the phase symmetry and velocity dependence predicted by DPR.

---

## 7. Primary phase prediction

At fixed \(u,m_e,m_m\), the pre-registered fit is

\[
\boxed{
\phi_{\rm NR}(\delta)=A\cos\delta+B
}.
\]

\(A\) is the measured DPR-correlated amplitude and \(B\) is a phase-independent experimental offset.

No additional phase harmonics will be introduced into the **primary weak-order fit** after seeing the data.

Predictions:

- \(\delta=0^\circ\): positive extremum, \(\phi_{\rm NR}-B>0\).
- \(\delta=90^\circ\): leading-order null, \(\phi_{\rm NR}\approx B\).
- \(\delta=180^\circ\): sign-reversed extremum, \(\phi_{\rm NR}-B<0\).
- \(\delta=270^\circ\): second leading-order null, \(\phi_{\rm NR}\approx B\).
- \(\delta=360^\circ\): return to the positive extremum.

---

## 8. Phase sweep

The primary sweep will use

\[
\delta=0^\circ,30^\circ,60^\circ,\ldots,330^\circ.
\]

A \(360^\circ\) repeat may be recorded as a closure check.

Measurement order should be randomized or alternated when practical to reduce drift. Original acquisition order must be retained in raw data.

---

## 9. Experimental noise floor

Real hardware is not expected to produce exactly zero response in controls.

Before the full two-channel run, obtain repeated measurements from:

1. unmodulated ladder;
2. electric-channel-only modulation;
3. magnetic-channel-only modulation.

Define pooled control standard deviation

\[
\boxed{\sigma_{\rm ctrl}}
\]

and detection threshold

\[
\boxed{T_{\rm noise}=5\sigma_{\rm ctrl}}.
\]

Experimental words **zero**, **null**, and **vanishes** mean statistically indistinguishable from this measured control floor, not mathematically equal to zero.

---

## 10. Mandatory calibration/control sequence

### Control A — unmodulated ladder

\[
m_e=0,\qquad m_m=0.
\]

Purpose: establish reciprocal baseline, propagation velocity, insertion loss, static phase offset, and noise.

Expected DPR-correlated response: below \(T_{\rm noise}\).

### Control B — electric channel only

\[
m_e>0,\qquad m_m=0.
\]

Purpose: measure residual one-channel response and parasitic nonreciprocity.

Expected DPR cross-coupling: below \(T_{\rm noise}\) after baseline correction.

### Control C — magnetic channel only

\[
m_e=0,\qquad m_m>0.
\]

Expected DPR cross-coupling: below \(T_{\rm noise}\) after baseline correction.

### Control D — static modulation

\[
\Omega=0.
\]

Prediction: no traveling-modulation DPR nonreciprocity above the control floor.

### Control E — reverse modulation direction

\[
K\rightarrow-K.
\]

Prediction: signed DPR-correlated response reverses direction.

### Control F — phase reversal

\[
\delta\rightarrow\delta+\pi.
\]

Prediction:

\[
\boxed{
\phi_{\rm NR}(\delta+\pi)-B
\approx
-[\phi_{\rm NR}(\delta)-B]
}.
\]

### Control G — probe-amplitude linearity

Repeat selected measurements at multiple probe amplitudes.

Primary DPR analysis requires operation in a regime where measured response is linear in probe amplitude within uncertainty.

### Control H — termination swap

Repeat selected operating points with changed/swapped port termination conditions.

A response that disappears or reverses solely because of a termination change will be flagged as a possible boundary artifact rather than bulk DPR evidence.

---

## 11. Velocity-law experiment

After the phase sweep establishes a measurable signed response, repeat at multiple values of \(u\).

At minimum, target approximately

\[
u=0.05,\;0.10,\;0.20,\;0.30,\;0.40
\]

where technically achievable and inside the measured regularity branch.

For each \(u\), retrieve the best-fit cosine amplitude \(A(u)\).

DPR candidate:

\[
\boxed{
A(u)=C\frac{u}{1-u^2}
}.
\]

Pre-registered competing models:

\[
M_1(u)=C_1u,
\]

\[
M_2(u)=C_2\frac{u}{1-u},
\]

\[
M_3(u)=C_3\frac{u}{1-u^2},
\]

\[
M_4(u)=C_4u^2.
\]

\(M_3\) is the DPR model.

No additional functional form will be declared a primary competitor after viewing the data.

---

## 12. Velocity-model selection criterion

Each candidate receives one amplitude coefficient fitted using the same dataset.

Primary ranking will use held-out or cross-validated squared prediction error. AIC or equivalent may be reported secondarily.

For the experiment to support the DPR velocity law,

\[
\boxed{
M_3=\frac{u}{1-u^2}
}
\]

must have the lowest pre-registered prediction error among \(M_1\)–\(M_4\).

Raw residuals for every model must be retained.

---

## 13. Primary phase-law success criteria

The primary DPR phase test is supportive only if **all** of the following occur.

### Criterion 1 — detectable two-channel response

At least one of the \(0^\circ\) or \(180^\circ\) responses satisfies

\[
|\phi_{\rm NR}-B|>5\sigma_{\rm ctrl}.
\]

### Criterion 2 — sign reversal

\[
[\phi_{\rm NR}(0^\circ)-B]
[\phi_{\rm NR}(180^\circ)-B]
<0.
\]

Both must individually exceed the control threshold if a strong sign-reversal claim is made.

### Criterion 3 — quadrature suppression

Define

\[
P=
\frac{
|\phi_{\rm NR}(0^\circ)-B|
+
|\phi_{\rm NR}(180^\circ)-B|
}{2}.
\]

Require

\[
\boxed{
\max(
|\phi_{\rm NR}(90^\circ)-B|,
|\phi_{\rm NR}(270^\circ)-B|
)
<
\max(T_{\rm noise},0.20P)
}.
\]

### Criterion 4 — cosine is the primary phase model

The pre-registered \(A\cos\delta+B\) model must describe the leading phase dependence without a systematic sign error or displacement of extrema incompatible with measurement uncertainty.

### Criterion 5 — one-channel controls remain small

Electric-only and magnetic-only responses must each remain substantially below the full two-channel DPR signal.

---

## 14. Stronger DPR support criteria

Classify the result as **strong DPR-consistent hardware evidence** only if the primary criteria pass and:

1. reversing \(K\) reverses the signed response;
2. \(\delta+\pi\) produces the predicted sign reversal;
3. response remains in the small-signal linear regime;
4. the result survives termination changes/de-embedding;
5. measurements on a different day reproduce the phase pattern;
6. the velocity experiment favors \(u/(1-u^2)\) over all pre-registered alternatives.

---

## 15. Pre-registered falsification conditions

The weak-order hardware hypothesis is **not supported** if a statistically resolved experiment inside the stated operating regime shows any of the following:

1. no measurable two-channel response above the calibrated noise floor;
2. \(0^\circ\) and \(180^\circ\) responses have the same sign;
3. significant extrema consistently occur near predicted quadrature nulls instead of near \(0^\circ/180^\circ\);
4. reversing modulation direction fails to reverse the signed response where the reversal should be resolvable;
5. one-channel modulation produces a response comparable to the supposed two-channel DPR signal;
6. the phase response cannot be distinguished from board asymmetry or static reciprocal behavior;
7. a competing pre-registered velocity model consistently predicts held-out measurements better than \(u/(1-u^2)\).

A failed hardware test does not automatically disprove the mathematical DPR theorem. It may instead falsify the proposition that the constructed circuit adequately realizes the assumptions of the DPR continuum model.

---

## 16. Higher-order effects

The primary experiment tests the weak-order cosine law.

Higher-order deviations may be investigated only after the primary analysis is frozen and completed.

Such deviations may include additional harmonics predicted by the generalized DPR framework.

They will be labeled **secondary/post-primary analysis** and must not be used retrospectively to rescue a failed weak-order test.

---

## 17. Raw-data policy

Retain:

- raw scope traces or sampled waveforms;
- forward and reverse measurements;
- actual modulation phases and frequencies;
- carrier frequency;
- measured \(c_m\) and \(u\);
- component settings;
- supply voltages;
- temperature if available;
- control-run measurements;
- acquisition timestamps;
- original acquisition order;
- calibration files;
- all analysis scripts.

No raw point may be deleted because it disagrees with the DPR prediction.

Any excluded point must remain in the archive with a written exclusion reason.

---

## 18. Analysis integrity

After data acquisition begins, the primary analysis may not:

- change predicted null locations;
- replace \(\cos\delta\) with a different phase law because it fits better;
- change the velocity-law candidate set;
- silently remove unfavorable operating points;
- redefine the experimental noise floor;
- change sign convention after viewing results.

Corrections of genuine instrumentation or coding errors are allowed but must be documented with version history.

---

## 19. Replication

A successful initial run is an observation in one apparatus.

Next evidentiary stages:

1. same device repeated on different days;
2. second independently assembled DPR-6 board;
3. independent laboratory/investigator replication;
4. materially different physical implementation.

Only after independent physical replication should stronger language about a broadly established physical phase law be considered.

---

## 20. Pre-registered claim language

If only the first board passes, permitted wording:

> “The Dorian Phase Relation was experimentally observed in a physical time-modulated electronic analogue of the stated continuum model.”

Not permitted:

> “DPR has been proven to be a universal law of physics.”

If independent replications pass, language may be strengthened to describe DPR as an experimentally replicated phase law within the demonstrated class of physical systems.

---

## 21. Freeze declaration

By committing and cryptographically hashing this document before the first full two-channel modulated phase sweep, the investigator declares that:

- predicted phase dependence was specified before observing the result;
- candidate velocity laws were specified in advance;
- control sequence was specified in advance;
- principal success/failure criteria were specified in advance;
- post-hoc exploratory analyses will be labeled as such.

**Investigator:** Dorian Martin-Smith  
**Date frozen:** 2026-09-13  
**Protocol SHA-256:** recorded in `protocol/DPR-6-HARDWARE-FALSIFICATION-PROTOCOL-v0.1.sha256`
