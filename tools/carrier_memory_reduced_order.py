"""CRTFE carrier-memory reduced-order model.

This script is intentionally a bounding model, not a plasma-chemistry solver.
It evaluates how carrier storage lifetime, pulse repetition, reactivation energy,
free-electron conducting lifetime, and static magnetic field affect the lower-bound
extra electrical power required by the pulsed Lorentz-entrainment branch.

Evidence-sensitive assumptions are exposed as parameters rather than hidden.
"""

from math import exp, sqrt

MASS_KG = 650.0
G = 9.81
FORCE_N = MASS_KG * G
MU_E = 0.055  # m^2/(V s), illustrative atmospheric-order electron mobility
P_FLUID_IDEAL_W = 148_500.0  # current 650 kg / 4.8 m^2 hover lower bound


def reuse_count(store_lifetime_s: float, repetition_hz: float) -> float:
    """Maximum idealized activations per stored carrier.

    Assumes perfect reattachment/recovery after each activation and exponential
    loss of the stored carrier population between pulses. Real values will be lower.
    """
    period = 1.0 / repetition_hz
    survival = exp(-period / store_lifetime_s)
    return 1.0 / (1.0 - survival)


def effective_activation_energy_eV(
    ion_pair_creation_eV: float,
    reactivation_eV: float,
    activations_per_carrier: float,
) -> float:
    """Amortized energy cost per useful activation, in eV/electron."""
    return reactivation_eV + ion_pair_creation_eV / activations_per_carrier


def min_extra_power_W(
    force_N: float,
    B_T: float,
    mobility_m2_Vs: float,
    conducting_lifetime_s: float,
    activation_energy_eV: float,
) -> float:
    """Optimized lower-bound Joule + carrier activation power.

    Derived from:
        F = D sigma E B V
        P_J = F^2/(D sigma B^2 V)
        P_activation = D sigma V W/(mu tau)

    where W is expressed in electron-volts per elementary charge (numerically volts).
    Optimizing over duty cycle gives:
        P_extra,min = (2 F / B) sqrt(W/(mu tau))

    This excludes magnet/cryogenic, dielectric, inverter, thermal-management,
    aerodynamic installation, and nonideal plasma-chemistry losses.
    """
    return (2.0 * force_N / B_T) * sqrt(
        activation_energy_eV / (mobility_m2_Vs * conducting_lifetime_s)
    )


def maxwell_pressure_Pa(B_T: float) -> float:
    mu0 = 4.0e-7 * 3.141592653589793
    return B_T * B_T / (2.0 * mu0)


def run():
    print("CRTFE carrier-memory lower-bound sweep")
    print(f"Hover force: {FORCE_N:.0f} N")
    print(f"Ideal fluid power floor: {P_FLUID_IDEAL_W/1000:.1f} kW\n")

    store_cases_us = [20.0, 117.0, 300.0]
    repetition_cases_kHz = [10.0, 20.0, 100.0, 1000.0]
    creation_eV = 34.0
    detachment_eV = 0.45

    print("Idealized carrier reuse (perfect recovery assumption)")
    for tau_us in store_cases_us:
        for f_kHz in repetition_cases_kHz:
            nreuse = reuse_count(tau_us * 1e-6, f_kHz * 1e3)
            weff = effective_activation_energy_eV(creation_eV, detachment_eV, nreuse)
            p = min_extra_power_W(FORCE_N, 8.0, MU_E, 50e-9, weff)
            print(
                f"store={tau_us:6.1f} us  f={f_kHz:7.1f} kHz  "
                f"reuse={nreuse:8.2f}  W_eff={weff:6.3f} eV  "
                f"P_extra@8T,50ns={p/1e6:8.2f} MW"
            )

    print("\nChemical-memory / conducting-lifetime sweep")
    B_cases = [5.0, 8.0, 12.0, 20.0]
    tau_cases = [50e-9, 10e-6, 100e-6, 300e-6, 1e-3, 3e-3]
    for B in B_cases:
        print(f"\nB={B:g} T  Maxwell pressure={maxwell_pressure_Pa(B)/1e6:.1f} MPa")
        for tau in tau_cases:
            p = min_extra_power_W(FORCE_N, B, MU_E, tau, detachment_eV)
            print(
                f"  tau_eff={tau*1e6:9.2f} us -> "
                f"P_extra={p/1000:9.1f} kW, "
                f"P_floor+extra={(p+P_FLUID_IDEAL_W)/1000:9.1f} kW"
            )


if __name__ == "__main__":
    run()
