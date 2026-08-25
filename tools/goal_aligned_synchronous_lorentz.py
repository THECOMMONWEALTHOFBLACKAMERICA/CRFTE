"""CRTFE goal-aligned synchronous Lorentz screening model.

Purpose
-------
Keep the analysis tied to the original CRTFE objective: large-area,
no-moving-parts atmospheric electromagnetic propulsion using full-stream
air, controlled conductivity/current, and strong magnetic field.

This is a reduced-order mathematical screening tool, not a validated
plasma/MHD solver and not evidence of propulsion performance.
"""

from math import sqrt

# Target vehicle baseline
MASS_KG = 650.0
G = 9.81
RHO = 1.225
ACTIVE_AREA_M2 = 4.8
INTERACTION_LENGTH_M = 0.5
ACTIVE_VOLUME_M3 = ACTIVE_AREA_M2 * INTERACTION_LENGTH_M
THRUST_N = MASS_KG * G

# Ideal hover momentum-theory floor
V_INDUCED_M_S = sqrt(THRUST_N / (2.0 * RHO * ACTIVE_AREA_M2))
P_IDEAL_W = THRUST_N * V_INDUCED_M_S


def required_effective_sigma(B_T: float, joule_budget_W: float) -> float:
    """Effective conductivity D*sigma_on needed for a Joule-loss budget."""
    return THRUST_N**2 / (joule_budget_W * B_T**2 * ACTIVE_VOLUME_M3)


def operating_point(B_T: float, sigma_on_S_m: float, duty: float):
    """Return reduced-order force-density/current/electric-field/Joule terms.

    Model:
      F = D sigma_on E B V
      sigma_eff = D sigma_on
      P_J = F^2 / (sigma_eff B^2 V)

    Segmentation/commutation can make the plasma locally pulsed without a
    traveling multi-tesla magnetic field, but it does not evade the average
    D*sigma requirement.
    """
    sigma_eff = duty * sigma_on_S_m
    force_density = THRUST_N / ACTIVE_VOLUME_M3
    current_density_peak = force_density / (duty * B_T)
    electric_field_peak = current_density_peak / sigma_on_S_m
    joule_W = THRUST_N**2 / (sigma_eff * B_T**2 * ACTIVE_VOLUME_M3)
    return {
        "B_T": B_T,
        "sigma_on_S_m": sigma_on_S_m,
        "duty": duty,
        "sigma_eff_S_m": sigma_eff,
        "J_peak_A_m2": current_density_peak,
        "E_peak_V_m": electric_field_peak,
        "P_J_kW": joule_W / 1000.0,
        "P_ideal_plus_J_kW": (P_IDEAL_W + joule_W) / 1000.0,
    }


def repetition_rate_hz(sigma_eff: float, sigma_peak: float, conductive_window_s: float) -> float:
    """Pulse rate required if each pulse provides sigma_peak for a window."""
    duty = sigma_eff / sigma_peak
    if duty > 1.0:
        return float("nan")
    return duty / conductive_window_s


def plasma_energy_metric_limit(B_T: float, extra_power_budget_W: float) -> float:
    """Maximum R = epsilon_pulse / integral(sigma dt) for an optimized pulsed source.

    Let K_sigma = integral sigma(t) dt per pulse and epsilon_p be deposited
    plasma-source energy per unit volume per pulse. Define

        R = epsilon_p / K_sigma       [equivalent to (V/m)^2]

    For periodic pulsing, eliminating repetition frequency gives

        P_extra = F^2/(B^2 V sigma_eff) + V sigma_eff R

    The optimized minimum is

        P_extra,min = 2 F/B * sqrt(R)

    Therefore this function returns the largest R compatible with the chosen
    extra-power allowance. Lower R is better.
    """
    return (extra_power_budget_W * B_T / (2.0 * THRUST_N)) ** 2


if __name__ == "__main__":
    print("CRTFE goal-aligned synchronous Lorentz screening")
    print(f"Hover thrust: {THRUST_N/1000:.3f} kN")
    print(f"Ideal hover induced velocity: {V_INDUCED_M_S:.2f} m/s")
    print(f"Ideal hover fluid-power floor: {P_IDEAL_W/1000:.1f} kW")
    print()

    joule_budget = 50_000.0
    for B in (3.0, 5.0, 8.0):
        seff = required_effective_sigma(B, joule_budget)
        print(f"B={B:>4.1f} T -> sigma_eff={seff:>7.2f} S/m for 50 kW Joule loss")

    print("\nRepresentative full-stream points")
    for B, sigma_on, duty in (
        (5.0, 50.0, 0.50),
        (5.0, 500.0, 0.0271065),
        (8.0, 50.0, 0.106),
        (8.0, 500.0, 0.0105885),
    ):
        print(operating_point(B, sigma_on, duty))

    print("\nPulse cadence needed to reproduce the 50 kW-Joule-loss sigma_eff")
    for B in (5.0, 8.0):
        seff = required_effective_sigma(B, joule_budget)
        for sigma_peak in (100.0, 500.0, 800.0):
            for window_us in (0.05, 0.5, 5.0, 50.0):
                f = repetition_rate_hz(seff, sigma_peak, window_us * 1e-6)
                if f == f:
                    print(
                        f"B={B:.0f} T, sigma_peak={sigma_peak:.0f} S/m, "
                        f"window={window_us:g} us -> {f/1000:.2f} kHz"
                    )

    print("\nPlasma-source energy metric limits")
    for B in (3.0, 5.0, 8.0):
        rmax = plasma_energy_metric_limit(B, 80_000.0)
        print(
            f"B={B:.0f} T -> R=epsilon_p/K_sigma must be <= {rmax:.1f} (V/m)^2 "
            "for <=80 kW optimized plasma+Joule overhead"
        )
