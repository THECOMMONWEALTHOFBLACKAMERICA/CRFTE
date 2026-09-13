# Dorian Phase Relation v3 - Phase-Uniform Validity Maps

These numerical tables are supplementary to the all-orders theorem.

Because the theorem proves that the maximum absolute truncation remainder occurs at the in-phase condition \\(\\delta=0\\), the in-phase thresholds below are conservative **phase-uniform validity boundaries** for every relative phase on the stated regular subluminal branch.

## Equal-depth map

`data/Dorian_validity_thresholds_v3.csv` records the pole

\\[
u_{\\rm pole}=\\frac{1}{1+m}
\\]

and the \\(O(2)\\), \\(O(4)\\), and \\(O(6)\\) threshold velocities for 0.1%, 1%, 5%, and 10% relative error. The crossing-status field is explicit; every reported equal-depth threshold crosses before the pole.

## Unequal-depth map

`data/Dorian_unequal_depth_validity_thresholds_v3.csv` extends the same calculation to

\\[
a,b\\in\\{0.05,0.10,0.15,0.20,0.30\\},
\\]

using the phase-uniform pole

\\[
u_{\\rm pole}(a,b)=\\frac{1}{\\sqrt{(1+a)(1+b)}}.
\\]

The table is symmetric under \\(a\\leftrightarrow b\\) to numerical precision.

These files quantify the theorem's approximation envelope; they do not enlarge its scope beyond the stated local sinusoidal continuum model.
