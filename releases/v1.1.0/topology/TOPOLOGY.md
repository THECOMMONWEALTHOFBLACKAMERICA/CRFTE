# Exact canonical topology

`Vs_L -- ZL -- [node 0: C0(t) to ground] -- L0(t) -- [node 1: C1(t) to ground] -- ... -- [node N-1: C_(N-1)(t) to ground] -- L_(N-1)(t) -- ZR -- Vs_R`

For the canonical V1 device, `N=48`: exactly **48 shunt capacitors and 48 series inductors**. The last series inductor feeds the right termination. This differs from a 48-C/47-L ladder with the load attached directly to the last capacitor.

Accepted transferability tests also use N=96, 144, and 192 while preserving the same per-cell topology and fixed spatial modulation phase `kappa = pi/6` (or `-pi/6` for modulation reversal).
