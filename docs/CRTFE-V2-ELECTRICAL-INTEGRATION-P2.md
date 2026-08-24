# CRTFE V-2 Electrical Integration and Wiring Baseline

> Controlled revision: P2 - 2026-08-24  
> Requirement maturity: `DRAFT`  
> Status: concept-level ground-research electrical architecture. Not a fabrication release, energized-work authorization, flight drawing, or approval to construct a high-voltage source.

## 1. Controlled purpose

This revision adds connection architecture for four separate research configurations:

1. the V0.3 moving-air conductivity screening rig
2. the G2B plasma-off polyphase stator validation article
3. the G2D combined HTS-bias/stator ground article
4. the V5 target-vehicle energy sled and ARC interface boundary

The drawings show functional separation, protective functions, measurement points, connector families and harness zones. They deliberately do **not** release bus voltage, conductor ampacity, overcurrent-device ratings, contactor ratings, coil turns, coil current, HTS dump resistance, creepage/clearance, insulation system or energized test limits. Those values require selected hardware, a fault-current study, thermal analysis, EMC analysis and approval by the responsible electrical engineer and host laboratory.

## 2. Non-negotiable safety rules

- High-voltage plasma hardware is a professionally enclosed laboratory subsystem operated under the host facility's procedure.
- The safety chain is hardwired and independent of ARC, T.A.R., the DAQ computer and ordinary software.
- Opening a guarded energized compartment must remove the relevant hazardous-energy enable through a safety-rated architecture selected by the qualified integrator.
- Emergency stop, guard interlocks and protective trips are de-energize-to-trip and require deliberate manual reset.
- No automatic restart is permitted after loss and return of control power.
- Lockout/tagout, absence-of-voltage verification, discharge verification and stored-energy controls are required before access.
- Signal, control, stator-power, HTS-current and propulsion-HV harnesses use separate routing zones and controlled crossings.
- Protective bonding and cable-shield termination are not interchangeable. Each requires its own controlled drawing and inspection.
- A conductive shield, frame or seam near the traveling field must be analyzed and tested for eddy-current heating and shorted-turn behavior.

## 3. Drawing set

| Sheet | Drawing | Purpose |
|---|---|---|
| E-001 | Index, legend and architecture boundary | Defines symbols, configuration boundaries and unreleased values |
| E-101 | V0.3 system interconnect | Separates blower, enclosed plasma subsystem, instruments, DAQ and hardwired safety |
| E-102 | V0.3 hardwired safety chain | Shows dual-channel concept, manual reset and monitored contactor feedback |
| E-201 | G2B stator validation one-line | Shows isolated polyphase source, current/voltage measurement and segmented stator |
| E-301 | G2D HTS/stator integration | Keeps HTS supply/quench protection independent from the traveling-wave source |
| E-401 | V5 energy-sled single-line | Shows functional order of service disconnect, fuse, contactors, precharge, IMD and branch isolation |
| E-501 | ARC power/data/safety boundary | Prevents ARC from becoming a direct actuator or protective-trip path |
| E-601 | Harness zones and interface schedule | Controls routing, labeling, connector classes and release evidence |

## 4. Cable-class schedule

| Class | Service | P2 planning rule | Released size/status |
|---|---|---|---|
| C0 | Protective earth/bonding | Green/yellow where applicable; dedicated studs; no signal-current return | `TBD` by fault study and applicable code |
| C1 | 24 VDC safety/control | Twisted stranded copper; separately fused branches; de-energize-to-trip | 18 AWG bench candidate only; engineer verifies length, fuse and environment |
| C2 | Analog sensors/bridge/voltage sense | Shielded twisted pair; shield termination per instrument plan | 22-24 AWG bench candidate only |
| C3 | Thermocouples | Correct thermocouple-alloy extension wire; no copper substitution | 24 AWG bench candidate only |
| C4 | Digital data/time | Fiber preferred across noisy/high-energy boundaries; copper only in controlled zone | Connector/media by network and EMC design |
| C5 | Polyphase stator power | Symmetric phase routing; measured current per phase; minimize loop area | `TBD` after frequency, RMS/peak current, skin/proximity and thermal analysis |
| C6 | HTS magnet DC/current leads | Vendor-qualified current leads and cryogenic feedthroughs | `TBD` by magnet/cryogenic design |
| C7 | Propulsion/battery HV | Orange identification where applicable; touch-safe keyed interfaces; HVIL | `TBD` after bus, fault-current, ampacity, insulation and environmental studies |
| C8 | Pyro/service-disconnect firing or squib circuits | Physically segregated, guarded and separately controlled | Not released in P2 |

Candidate small-wire gauges apply only to a non-flight bench harness after the responsible engineer confirms branch protection, voltage drop, temperature, bundle derating, flexing and connector compatibility. They are not aircraft wire-size releases.

## 5. Interface identifiers

| ID | Interface | Required features |
|---|---|---|
| J-V03-CTRL | V0.3 control-box bulkhead | Keyed low-voltage connector; control and status only |
| J-V03-DAQ | V0.3 instrumentation bulkhead | Shielded sensor pairs; no hazardous-energy conductors |
| J-V03-HV | Enclosed plasma-subsystem interface | Laboratory-owned, touch-safe, interlocked; pinout not released |
| J-G2-PH | G2 stator phase interface | Three phase conductors plus protective bonding as designed; phase ID A/B/C |
| J-G2-SENSE | G2 voltage/current/temperature sense | Finger-safe measurement interface selected by laboratory |
| J-HTS-DC | HTS supply/current-lead interface | Vendor/engineer controlled; no P2 pinout |
| J-HTS-QD | Quench detector/dump interface | Independent protective circuit; ARC read-only status only |
| J-SLED-HV | Energy-sled propulsion-HV interface | Touch-safe, keyed, HVIL, blind-mate candidate; rating `TBD` |
| J-SLED-LV | Energy-sled essential low-voltage interface | BMS/IMD/status and independent shutdown request |
| J-ARC-A/B | ARC redundant data/power interfaces | Isolated supplies and segregated network paths; no direct actuator pins |

## 6. Assembly order

### Phase A - drawings and parts control

1. Freeze the configuration ID and test-plan revision.
2. Create a wire list with `from`, `to`, signal/service, cable class, connector/pin, length, shield rule and inspection status.
3. Select actual components and capture manufacturer datasheets.
4. Complete fault-current, ampacity, insulation, creepage/clearance, stored-energy and EMC analyses before releasing hazardous-energy wiring.
5. Have the host laboratory approve the safety architecture and energized-work boundary.

### Phase B - mechanical and de-energized installation

6. Install DIN rail, terminals, protective-earth bar and labeled cable-entry plates in the control enclosure.
7. Install hardwired safety components before ordinary control or DAQ hardware.
8. Install separate harness routes for C0/C1, C2/C3/C4 and C5/C6/C7 services.
9. Terminate protective bonding first. Record stud preparation, hardware stack, torque and measured resistance.
10. Build low-voltage harnesses to a controlled cut list. Use qualified crimp tooling and record tool/terminal compatibility.
11. Label both ends of every conductor and every connector. Labels must match the wire list and schematic.
12. Install shield terminations exactly as the EMC plan requires; do not improvise pigtails or ground both ends without analysis.
13. Install hazardous-energy harnesses only after their engineering release and under the qualified facility's procedure.

### Phase C - inspection and de-energized verification

14. Perform point-to-point continuity against the released netlist.
15. Verify no unintended continuity between power, control, sensor, shield and chassis circuits.
16. Verify protective-bond continuity with an approved low-resistance method.
17. Verify connector keying, polarization, strain relief, bend radius, chafe protection, service loops and clamp spacing.
18. Verify E-stop and guard-interlock logic using a low-energy test supply before any hazardous source is connected.
19. Verify manual reset and no automatic restart after control-power cycling.
20. Record all results, instruments, calibration status, operator, date and configuration.

### Phase D - staged commissioning

21. Commission the DAQ and sensors with hazardous sources disconnected.
22. Commission the blower and mechanical systems with the plasma subsystem isolated.
23. Run the full V0.3 plasma-OFF baseline at 10, 20 and 30 m/s.
24. Commission the bare G2 stator at the lowest laboratory-approved energy, with field/phase/impedance measurements and no plasma.
25. Repeat G2 with passive structures installed and stop on unexplained heating or field distortion.
26. Integrate HTS bias only after quench protection, stored-energy handling and cryogenic safety reviews are complete.
27. Enable the enclosed plasma subsystem only with qualified personnel, approved procedure, interlocks and independent stop authority.

## 7. Required inspections

| Hold point | Evidence required | Release authority |
|---|---|---|
| HP-E1 | Approved schematic, wire list and selected component datasheets | Responsible electrical engineer |
| HP-E2 | Protective-bond and enclosure inspection | Electrical engineer / facility safety |
| HP-E3 | Point-to-point netlist verification and insulation test plan | Independent checker |
| HP-E4 | E-stop/interlock/manual-reset functional test at low energy | Facility safety representative |
| HP-E5 | DAQ calibration and time synchronization | Test engineer |
| HP-E6 | Plasma-OFF V0.3 and G2 baselines | Test director |
| HP-E7 | HTS quench/dump validation | Magnet/cryogenic responsible engineer |
| HP-E8 | Energized-test readiness review | Host laboratory authority |

## 8. Stop-work conditions

Stop, isolate and investigate on any of the following:

- unexpected continuity or insulation result
- missing/incorrect conductor or connector label
- a guard opening that does not remove hazardous-energy enable
- automatic restart after power restoration
- welded or inconsistent contactor feedback
- loss of protective bond
- uncommanded phase sequence or current imbalance
- unexplained passive-structure heating, field distortion or shorted-turn signature
- HTS temperature-margin loss or quench-protection anomaly
- DAQ time loss, calibration failure or mismatched test configuration
- arc, smoke, odor, coolant leak, abnormal sound or unexpected temperature rise

## 9. ARC/T.A.R. boundary

ARC may receive approved telemetry, retrieve signed project evidence, compare a pinned digital twin with measurements and produce a non-executable research plan. It may submit a typed ground-test intent for independent review.

ARC does not carry hardwired E-stop, guard-interlock, quench-trip, BMS protection, contactor-drive, phase-drive or actuator current. Loss of ARC must not prevent a deterministic controller or hardwired protective circuit from reaching the predefined safe state.

## 10. Sources and workmanship references

- CRTFE project baselines: `V0.3-PROTOTYPE-BUILD-GUIDE.md`, `V2-HYBRID-MHD-BASELINE.md`, `V2-G2-ELECTROMAGNETIC-VALIDATION.md`, `ARC-AKASHIC-VESSEL-INTEGRATION.md`, and the V5 energy-sled preliminary manual.
- OSHA 29 CFR 1910.147, control of hazardous energy: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147
- OSHA 29 CFR 1910.333, electrical work practices: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333
- OSHA 29 CFR 1910.306, interlock precedent for access panels on specific equipment: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.306
- NASA-STD-8739.4, cable and harness workmanship: https://standards.nasa.gov/standard/NASA/NASA-STD-87394
- FAA AC 43.13-1B with Change 1, aircraft inspection/repair practices where applicable and legally permitted: https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/99861
- NFPA 70E overview, electrical safety in the workplace: https://www.nfpa.org/codes-and-standards/nfpa-70e-standard-development/70e

These references inform the safety/workmanship basis. They do not turn this preliminary project package into a code-compliant installation, flight release or certification approval.
