# P4A Simulation Correction — Plasma-Loop Inductance

**Date:** 2026-08-25

The initial P4A resistive-only screen estimated a few-millitesla drive-flux requirement from `E=J/sigma` and Faraday's law. That estimate omitted plasma-loop inductance.

The next RL simulation shows that `L dI/dt` dominates the voltage requirement when a multi-kiloampere plasma current must build in only a few microseconds. Therefore the earlier **2–10 mT** figure must not be used as the current P4A engineering estimate.

For the representative 8 T, 3 kHz, 5 us, 800 S/m case, a compact bipolar static-pole plasma loop with approximately `L=0.39 uH` and `R=10 mOhm` requires approximately:

```text
~1.09 kV induced loop voltage
~13 kA end-of-pulse current per module
~54 mT equivalent linked drive-field swing over 0.10 m^2
~35 kW total gas-current Joule loss
~43 kW electromagnetic overhead if 98% of loop magnetic energy is recovered
```

The architecture still avoids a multi-tesla traveling magnetic propulsion field, but its benefit now depends strongly on keeping the plasma loop **sub-microhenry**.

See the superseding detailed simulation:

- `docs/P4B-BIPOLAR-STATIC-POLE-INDUCTIVE-LOOP.md`
- `tools/bipolar_static_pole_inductive_loop.py`

P4A remains a current-drive concept inside the goal-locked CRTFE architecture; this correction changes the quantitative drive-field estimate, not the project goal.
