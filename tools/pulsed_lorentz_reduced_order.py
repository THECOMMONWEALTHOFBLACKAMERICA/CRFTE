"""CRTFE pulsed Lorentz / synchronous conductivity reduced-order model.

This is a research screening model, not CFD, PIC, plasma chemistry, or a flight prediction.
It compares three limiting cases:

1. Continuous conductivity supplied as a given material property.
2. One-pass ionization: each parcel is ionized once and remains conductive through the interaction length.
3. Recreated-pulse lower bound: the conductive population must be recreated on a characteristic decay time.

The purpose is to identify which parameter combinations are worth higher-fidelity modeling.
"""

from math import sqrt

# Target vehicle / actuator baseline
MASS_KG = 650.0
G = 9.81
RHO_AIR = 1.225
AREA_M2 = 4.8
INTERACTION_LENGTH_M = 0.5
VOLUME_M3 = AREA_M2 * INTERACTION_LENGTH_M

# Plasma screening assumptions
# Electron mobility is an illustrative atmospheric-air order-of-magnitude value.
# It must ultimately be replaced by E/N-dependent swarm data.
ELECTRON_MOBILITY_M2_VS = 0.05
# 34 eV is used as an illustrative lower-bound mean energy cost per electron-ion pair in air.
# It is a user-adjustable screening assumption, not a claim of achieved efficiency.
W_PAIR_EV = 34.0

THRUST_N = MASS_KG * G
INDUCED_VELOCITY_M_S = sqrt(THRUST_N / (2.0 * RHO_AIR * AREA_M2))
IDEAL_FLUID_POWER_W = THRUST_N * INDUCED_VELOCITY_M_S
VOLUME_FLOW_M3_S = AREA_M2 * INDUCED_VELOCITY_M_S
RESIDENCE_TIME_S = INTERACTION_LENGTH_M / INDUCED_VELOCITY_M_S


def conductivity_for_slip_loss(B_T: float, slip_loss_W: float) -> float:
    """Required bulk conductivity for a specified Joule/slip loss.

    From P_slip = F^2/(sigma B^2 V).
    """
    return THRUST_N**2 / (slip_loss_W * B_T**2 * VOLUME_M3)


def one_pass_ionization_power_W(sigma_S_m: float, w_pair_eV: float = W_PAIR_EV,
                                mobility: float = ELECTRON_MOBILITY_M2_VS) -> float:
    """Optimistic lower-bound power if each gas parcel is ionized once.

    sigma ~= e n_e mu_e and energy density ~= n_e W_pair imply
    U_ion ~= sigma * W_pair[eV] / mu_e in J/m^3.
    """
    ionization_energy_density_J_m3 = sigma_S_m * w_pair_eV / mobility
    return ionization_energy_density_J_m3 * VOLUME_FLOW_M3_S


def recreated_population_min_power_W(B_T: float, decay_time_s: float,
                                      effective_creation_energy_eV: float = W_PAIR_EV,
                                      mobility: float = ELECTRON_MOBILITY_M2_VS) -> float:
    """Best-case extra power for pulsed/recreated conductivity.

    Model:
        F = D sigma E_slip B V
        P_J = F^2/(D sigma B^2 V)
        P_create = D V U_create/tau

    with U_create ~= sigma*W_eff/mu.

    Optimizing over conductive duty cycle D cancels sigma and V:
        E_slip,opt = sqrt(W_eff/(mu tau))
        P_extra,min = 2 F E_slip,opt / B

    This is intentionally optimistic: it excludes driver, plasma chemistry,
    electrode/dielectric, magnet, cryogenic, switching, thermal and aerodynamic losses.
    """
    e_slip_opt_V_m = sqrt(effective_creation_energy_eV / (mobility * decay_time_s))
    return 2.0 * THRUST_N * e_slip_opt_V_m / B_T


def required_decay_time_for_extra_budget(B_T: float, extra_power_W: float,
                                         effective_creation_energy_eV: float = W_PAIR_EV,
                                         mobility: float = ELECTRON_MOBILITY_M2_VS) -> float:
    """Characteristic carrier lifetime required by the optimistic recreated-pulse bound."""
    term = extra_power_W * B_T / (2.0 * THRUST_N)
    return effective_creation_energy_eV / (mobility * term**2)


def print_screening_table():
    print("CRTFE pulsed-Lorentz reduced-order screening")
    print(f"Target thrust: {THRUST_N/1000:.3f} kN")
    print(f"Ideal actuator-disk velocity: {INDUCED_VELOCITY_M_S:.3f} m/s")
    print(f"Ideal fluid power floor: {IDEAL_FLUID_POWER_W/1000:.1f} kW")
    print(f"Interaction residence time: {RESIDENCE_TIME_S*1000:.2f} ms")
    print()

    slip_budget_W = 50_000.0
    print("One-pass optimistic screening (50 kW slip/Joule allowance):")
    print("B[T]  sigma[S/m]  P_ion_once[kW]  total_floor[kW]")
    for B in [3, 5, 8, 12, 20]:
        sigma = conductivity_for_slip_loss(B, slip_budget_W)
        p_ion = one_pass_ionization_power_W(sigma)
        total = IDEAL_FLUID_POWER_W + slip_budget_W + p_ion
        print(f"{B:>4.1f}  {sigma:>10.3f}  {p_ion/1000:>14.1f}  {total/1000:>14.1f}")

    print()
    print("Recreated-pulse lower bound using 50 ns carrier decay:")
    print("B[T]  fresh-air-extra[kW]  0.45eV-reactivation[kW]")
    for B in [5, 8, 12, 20]:
        fresh = recreated_population_min_power_W(B, 50e-9, 34.0)
        react = recreated_population_min_power_W(B, 50e-9, 0.45)
        print(f"{B:>4.1f}  {fresh/1000:>19.1f}  {react/1000:>23.1f}")

    print()
    print("Carrier lifetime required to fit an 80 kW non-fluid allowance:")
    print("B[T]  tau@34eV[s]  tau@4eV[s]  tau@0.45eV[s]")
    for B in [5, 8, 12, 20]:
        t34 = required_decay_time_for_extra_budget(B, 80_000, 34.0)
        t4 = required_decay_time_for_extra_budget(B, 80_000, 4.0)
        t045 = required_decay_time_for_extra_budget(B, 80_000, 0.45)
        print(f"{B:>4.1f}  {t34:>11.4g}  {t4:>10.4g}  {t045:>13.4g}")


if __name__ == "__main__":
    print_screening_table()
