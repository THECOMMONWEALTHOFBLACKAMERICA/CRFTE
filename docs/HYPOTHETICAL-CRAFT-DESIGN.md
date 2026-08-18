# CRTFE Hypothetical Two-Seat Craft — Geometry & Systems Layout

> **Status:** conceptual aircraft packaging study only. The propulsion method is not experimentally validated. This document corrects the earlier oversized render and removes unsupported performance claims.

## Why the aircraft baseline changed

The earlier 450 kg number was a reduced-order propulsion-analysis baseline, not a complete two-person aircraft mass estimate. Once two occupants, controls, avionics, structure, batteries, thermal hardware, environmental-control hardware, landing gear, and propulsion-system mass are included, 450 kg becomes too aggressive for honest packaging.

For the hypothetical two-seat demonstrator, use:

- **Design gross mass:** 650 kg
- **Crew:** 2
- **Length:** 6.2 m
- **Wingspan:** 5.4 m
- **Overall height:** 1.8 m
- **Wing reference area:** ~11 m²
- **Four active lift/propulsion zones:** ~1.2 m² each
- **Total active lift area:** ~4.8 m²

These values are a packaging baseline, not certification dimensions.

## Aerodynamic sanity check

At 650 kg:

```text
Weight = 650 × 9.81 = 6,376.5 N
Wing loading = 6,376.5 / 11 ≈ 580 N/m² ≈ 59 kg/m²
```

Using sea-level density 1.225 kg/m³ and an illustrative CLmax = 1.5:

```text
Vstall ≈ sqrt(2W / (rho S CLmax)) ≈ 25.1 m/s ≈ 49 kt
```

This is only an initial sizing check; real stall speed depends on actual airfoil, planform, Reynolds number, flap/high-lift system, and CFD/flight test.

## Hover / propulsion re-check for the 650 kg craft

Four modules means:

```text
Required hover thrust/module = 6,376.5 / 4 ≈ 1,594 N
```

If the old 0.60 m²/module area were retained, the ideal actuator velocity rises to ~33.3 m/s and the ideal induced power rises to ~53 kW/module before plasma, magnet, inverter, cooling, and other losses. That leaves essentially no room under the old 60 kW/module working cap.

Therefore the aircraft packaging study doubles the active area to approximately **1.20 m²/module**.

With A = 1.20 m²/module:

```text
Ideal actuator velocity ≈ 23.5 m/s
Ideal induced power ≈ 37.5 kW/module
```

At the prior conditional V5 point, sigma = 150 S/m and B = 1.8 T:

```text
Required slip ≈ 5.47 m/s
Ohmic/slip power ≈ 8.71 kW/module
Assumed auxiliary allowance = 5 kW/module
Modeled total ≈ 51.2 kW/module
```

Four modules would therefore be approximately 205 kW total in this simplified conditional hover model.

**Important:** this is a new 650 kg / 1.2 m²-per-module packaging calculation. It is not the same simulation case as the original 450 kg / 0.6 m²-per-module V5 sweep. Full V5 modeling would need to be rerun if V0.3 succeeds.

## Fuselage / cockpit packaging

### Crew station

Use two side-by-side seats rather than tandem for the first layout.

Recommended internal cockpit envelope:

- **Internal width:** 1.36–1.42 m
- **Seated cabin length:** ~2.2 m
- **Usable seated height:** ~1.20–1.25 m
- **External centerbody width:** ~1.55–1.65 m after structure/sidewalls

This allows two approximately 0.55–0.60 m-wide occupant envelopes plus center clearance, side structure, harnesses, and controls.

### Controls

Reserve the forward cockpit for:

- dual side-stick or center-stick flight controls
- dual rudder/brake pedals or electronically integrated yaw control
- primary flight display
- propulsion/energy display
- emergency stop / propulsion isolation
- communications/navigation panel
- environmental-control panel
- manual backup controls where applicable

Keep high-voltage propulsion buses physically segregated from crew-level control wiring.

## Longitudinal packaging

A practical first 6.2 m centerbody split is:

```text
0.0–0.7 m   Nose / crash structure / sensors
0.7–2.9 m   Two-seat cockpit and controls
2.9–3.8 m   Avionics + flight-control + environmental-control bay
3.8–5.2 m   Battery / power electronics / thermal-management keel bay
5.2–6.2 m   Aft structure / propulsion distribution / cooling exits
```

The four large active MHD/lift zones are integrated into the broad wing-centerbody and inner-wing lower surfaces rather than packaged as four tiny 0.6 m² pods.

## Environmental control and oxygen

### Terrestrial demonstrator

For a first atmospheric demonstrator, a full spacecraft-style closed-loop oxygen-recycling system is not justified. NASA ECLSS systems include air revitalization, carbon-dioxide removal, water recovery, and oxygen generation by electrolysis; those are valuable for long-duration spacecraft but add substantial mass, plumbing, power, and complexity.

The first aircraft should instead use a **semi-closed cabin environmental-control system**:

- outside-air ventilation when cabin conditions permit
- cabin-air recirculation fan
- particulate / activated-carbon filtration
- CO2 sensor and alarm
- humidity and temperature control
- compact CO2 scrubber as emergency/extended-duration backup
- emergency supplemental oxygen cylinder(s) and masks
- cabin pressure monitoring

FAA 14 CFR 91.211 requires supplemental oxygen based on **cabin pressure altitude**, including crew oxygen above 12,500 ft for prolonged exposure, continuous crew use above 14,000 ft, and oxygen availability for occupants above 15,000 ft. For early test operations, remaining well below these cabin-altitude thresholds avoids the need to make regenerative oxygen generation part of the propulsion demonstrator.

### Later high-altitude version

If a later aircraft is intended for high-altitude pressurized operation, design a dedicated environmental-control/life-support bay approximately 0.10–0.20 m³ initially for:

- pressurization hardware
- redundant oxygen storage
- CO2 scrubbing
- humidity removal
- emergency masks
- cabin pressure and O2/CO2 monitoring

A true regenerative oxygen system (electrolysis plus CO2 reduction/recovery) should be treated as a separate technology program, not assumed to fit inside the first flight demonstrator.

## Preliminary mass budget

This is a packaging allowance, not a validated weight statement:

| Item | Preliminary allowance |
|---|---:|
| Two occupants | 180 kg |
| Airframe / landing gear / cabin structure | 110–130 kg |
| Battery pack | 90–120 kg |
| Propulsion-field hardware + inverters + cryogenic/thermal hardware | 90–130 kg |
| Avionics / flight controls / sensors | 20–30 kg |
| Environmental control + emergency oxygen | 10–20 kg |
| Wiring / plumbing / misc. systems / reserve | 40–60 kg |

This range itself shows why **450 kg should not be presented as a finished two-seat aircraft gross weight**. The 650 kg design point is still aggressive and depends heavily on the eventual propulsion and magnet masses.

## Blueprint dimensions to use going forward

```text
Length:             6.2 m
Wingspan:           5.4 m
Overall height:     1.8 m
Wing area:          ~11 m²
Centerbody width:   ~1.6 m external
Cockpit internal:   ~1.4 m W × 2.2 m L × 1.2 m usable seated H
Crew:               2 side-by-side
Active lift area:   ~4.8 m² total (4 × 1.2 m²)
Design gross mass:  650 kg conceptual
```

## Claims intentionally removed from the old render

Do **not** use the following as design specifications until independently supported:

- Mach 2.5+ top speed
- unlimited range
- >10 g sustained acceleration
- 60,000+ ft service ceiling
- 'very low' radar/thermal/acoustic signature
- gravity or inertia cancellation

The current program goal is much narrower: prove useful atmospheric conductivity in V0.3, then demonstrate controlled MHD force in a stationary rig before aircraft-scale propulsion claims are made.

## Current design philosophy

The craft should be treated as a **blended-wing two-seat technology demonstrator** with generous centerbody volume, four large distributed propulsion interaction zones, battery/thermal mass close to the center of gravity, conventional aerodynamic control surfaces as backup, and an environmental-control system sized for terrestrial flight rather than spacecraft life support.
