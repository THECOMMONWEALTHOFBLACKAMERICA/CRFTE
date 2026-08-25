"""CRTFE neutral-paramagnetic air stage screening model.

Explores an alternative to plasma MHD: use the ordinary paramagnetism of O2 in air.
A pulsed magnetic stage can in principle add/remove the magnetic potential energy
of a paramagnetic gas parcel. This script estimates the ideal stage count required
to reach the far-wake velocity of the current hover target.

It is a thermodynamic/magnetic-potential bound, not a coil or flight design.
"""

from math import sqrt

MU0 = 4.0e-7 * 3.141592653589793
CHI_AIR = 3.6e-7      # dimensionless volume susceptibility, room-temp air order
RHO_AIR = 1.225       # kg/m^3
MASS_KG = 650.0
G = 9.81
AREA_M2 = 4.8
INTERACTION_LENGTH_M = 0.5
CHARACTERISTIC_FLOW_M_S = 30.0


def magnetic_specific_energy_J_kg(B_T: float) -> float:
    """Ideal 0->B magnetic potential-energy scale per kg of bulk air."""
    energy_density = CHI_AIR * B_T * B_T / (2.0 * MU0)
    return energy_density / RHO_AIR


def hover_induced_velocity() -> float:
    thrust = MASS_KG * G
    return sqrt(thrust / (2.0 * RHO_AIR * AREA_M2))


def run():
    vi = hover_induced_velocity()
    far_wake = 2.0 * vi
    target_specific_ke = 0.5 * far_wake * far_wake

    print("CRTFE neutral-paramagnetic air stage bound")
    print(f"Hover induced velocity: {vi:.2f} m/s")
    print(f"Far-wake velocity increment scale: {far_wake:.2f} m/s")
    print(f"Target far-wake specific kinetic energy: {target_specific_ke:.1f} J/kg\n")

    for B in [5.2, 8.0, 12.0, 20.0]:
        e = magnetic_specific_energy_J_kg(B)
        stages = target_specific_ke / e
        pitch = INTERACTION_LENGTH_M / stages
        switch_hz = CHARACTERISTIC_FLOW_M_S / pitch
        print(
            f"B={B:4.1f} T  e_stage={e:7.2f} J/kg  "
            f"ideal_stages={stages:7.1f}  pitch={pitch*1000:7.2f} mm  "
            f"characteristic_switch={switch_hz/1000:7.2f} kHz"
        )


if __name__ == "__main__":
    run()
