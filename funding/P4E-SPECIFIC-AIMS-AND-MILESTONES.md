# CRTFE P4E — Specific Aims and Milestones

## Objective

Determine whether vibrationally conditioned, high-repetition-rate atmospheric plasma can increase the useful conductivity-time integral enough to produce controlled, polarity-reversible MHD momentum transfer at laboratory scale.

The work deliberately stops short of aircraft hardware. Its purpose is to establish or falsify the plasma/MHD mechanism that the larger CRTFE architecture requires.

## Aim 1 — Quantify the RF vibrational-conditioning gain

Operate a controlled dry-air flow cell with 40-100 kHz nanosecond ionization pulses, first without and then with a sub-breakdown RF waveform.

Measure:

- time-resolved electron density or validated surrogate;
- plasma impedance / effective conductivity;
- pulse energy and average conditioning power;
- optical emission and spatial uniformity;
- gas rotational/translational temperature;
- attachment/recombination decay behavior;
- flow speed and residence time.

### Milestone 1A

Demonstrate repeatable high-PRF diffuse/non-arc operation over a bounded operating map.

### Milestone 1B

Show either:

```text
RF-on integral[sigma(t) dt] / RF-off integral[sigma(t) dt] >= 10
```

at matched ns-pulse energy, or establish a measured upper bound below that target.

### Milestone 1C

Maintain bulk gas-temperature rise below 150 K at the selected operating point.

## Aim 2 — Demonstrate and identify Lorentz-force momentum transfer

Place the characterized cell in a 1.5-2.0 T transverse static magnetic field. Apply a separately controlled sustainer/current drive after the ionization pulse.

Execute the sign matrix:

```text
+B,+J
+B,-J
-B,+J
-B,-J
```

plus:

```text
B=0
J=0
plasma=off
RF=off
flow=off / installed-hardware baseline where safe
```

Measure force/pressure/velocity response synchronously with current, voltage, plasma state, and gas temperature.

### Milestone 2A

Resolve a conditioned force signal of at least 3 mN above calibrated background.

### Milestone 2B

Force direction must follow `J x B` under independent B and J reversals.

### Milestone 2C

Measured force must agree with the independently reconstructed electromagnetic body-force integral within approximately ±30% after measurement uncertainty is propagated.

## Aim 3 — Determine whether the gain is energetically meaningful

Compute for every validated operating point:

```text
K_sigma = integral[sigma(t) dt]
I_EM = integral[F_EM(t) dt]
E_ns = nanosecond-pulser deposited energy
E_RF = RF-conditioning energy
E_J = sustainer/current Joule energy
```

and compare:

```text
conductivity impulse / conditioning joule
Lorentz impulse / total electrical joule
```

### Milestone 3A

RF-conditioned operation improves Lorentz impulse per conditioning joule by at least 5x relative to ns-pulse-only operation.

### Milestone 3B

Identify whether attachment, recombination, spatial nonuniformity, or source energy is the dominant remaining limiter.

## Optional Aim 4 — Translate to electrodeless CRTFE current drive

Only after Aims 1-3 pass, replace the laboratory sustainer with the P4B/P4C induced-current topology:

- closed low-inductance plasma loop;
- adjacent opposite-polarity static magnetic poles;
- externally induced current;
- clamp/reset synchronized to plasma decay.

Success is not required for the initial grant to be scientifically productive.

## Simulation-defined experimental target

The P4E reduced-order model uses the following central screen:

```text
active volume: 50 cm^3
B: 2 T
current-drive field: 5 kV/m
PRF: 50 kHz
pulse-added carrier density: 3e12 cm^-3/pulse
```

Predicted outcomes:

```text
unconditioned model:      ~0.16 mN
moderate RF-conditioned:  ~7.6 mN
strong RF-conditioned:   ~13.1 mN
```

The experiment therefore seeks an order-of-magnitude RF-on/RF-off contrast, not an aircraft-scale thrust demonstration.

## Six-month technical sequence

### Month 1

- apparatus integration and safety review;
- plasma-off airflow baseline;
- pulse-energy calibration;
- RF field / impedance calibration;
- force-balance calibration.

### Months 2-3

- PRF / pulse-energy / RF-amplitude operating map;
- conductivity and decay-time measurements;
- spatial-uniformity and gas-temperature measurements;
- select one or more bounded P4E operating points.

### Months 4-5

- static-field MHD measurements;
- full B/J polarity-reversal matrix;
- force/pressure/velocity correlation;
- thermal and ionic-wind controls.

### Month 6

- energy ledger;
- uncertainty propagation;
- go/no-go decision for electrodeless current drive;
- manuscript / technical report / follow-on proposal.

## Decision rule

P4E is successful if the project can answer, quantitatively and with controls:

> Does vibrationally conditioned high-PRF plasma create a substantially larger, energy-efficient conductivity-time integral that translates into polarity-reversible `J x B` momentum transfer in moving atmospheric air?

A negative answer is a valid project outcome and should stop or redirect vehicle-scale CRTFE work before expensive hardware development.
