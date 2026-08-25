"""CRTFE segmented synchronous Lorentz pulse-budget model.

Goal-aligned reduced-order model for the primary P4 branch.

A plasma pulse creates an on-state conductivity that decays exponentially.
The propulsion electric field is applied only during a chosen useful window.
The model calculates:
  - time-averaged conductivity available to JxB force
  - electric field required for target thrust
  - Joule power
  - maximum allowable plasma-source energy per unit volume per pulse
    for a selected total overhead budget

This is a screening model, not a validated plasma chemistry or MHD solver.
"""

from math import exp, sqrt

MASS_KG = 650.0
G = 9.81
RHO = 1.225
AREA_M2 = 4.8
LENGTH_M = 0.5
VOLUME_M3 = AREA_M2 * LENGTH_M
THRUST_N = MASS_KG * G
INDUCED_V_M_S = sqrt(THRUST_N / (2 * RHO * AREA_M2))
IDEAL_FLUID_POWER_W = THRUST_N * INDUCED_V_M_S


def driven_sigma_eff(
    sigma_peak_S_m: float,
    tau_s: float,
    repetition_hz: float,
    drive_window_s: float,
) -> float:
    """Average conductivity available while drive is applied.

    Assumes each pulse produces an on-state approximately

        sigma(t) = sigma_peak * exp(-t/tau)

    and the propulsion field is gated on from t=0 to drive_window.
    Pulses are treated as independent; overlap/saturation is not modeled.
    """
    period_s = 1.0 / repetition_hz
    w = min(drive_window_s, period_s)
    k_sigma = sigma_peak_S_m * tau_s * (1.0 - exp(-w / tau_s))
    return repetition_hz * k_sigma


def operating_point(
    B_T: float,
    sigma_peak_S_m: float,
    tau_s: float,
    repetition_hz: float,
    drive_window_s: float,
    extra_power_budget_W: float,
):
    sigma_eff = driven_sigma_eff(
        sigma_peak_S_m, tau_s, repetition_hz, drive_window_s
    )
    if sigma_eff <= 0:
        raise ValueError("sigma_eff must be positive")

    E_drive_V_m = THRUST_N / (B_T * VOLUME_M3 * sigma_eff)
    J_avg_A_m2 = sigma_eff * E_drive_V_m
    P_joule_W = THRUST_N**2 / (B_T**2 * VOLUME_M3 * sigma_eff)

    remaining_W = extra_power_budget_W - P_joule_W
    if remaining_W > 0:
        epsilon_pulse_max_J_m3 = remaining_W / (VOLUME_M3 * repetition_hz)
        pulse_energy_whole_volume_J = epsilon_pulse_max_J_m3 * VOLUME_M3
    else:
        epsilon_pulse_max_J_m3 = None
        pulse_energy_whole_volume_J = None

    return {
        "B_T": B_T,
        "sigma_peak_S_m": sigma_peak_S_m,
        "tau_us": tau_s * 1e6,
        "repetition_kHz": repetition_hz / 1e3,
        "drive_window_us": drive_window_s * 1e6,
        "sigma_eff_S_m": sigma_eff,
        "E_drive_V_m": E_drive_V_m,
        "J_avg_A_m2": J_avg_A_m2,
        "P_joule_kW": P_joule_W / 1e3,
        "P_ideal_plus_joule_kW": (IDEAL_FLUID_POWER_W + P_joule_W) / 1e3,
        "epsilon_pulse_max_J_m3": epsilon_pulse_max_J_m3,
        "pulse_energy_whole_volume_max_J": pulse_energy_whole_volume_J,
    }


if __name__ == "__main__":
    print("CRTFE segmented synchronous Lorentz pulse-budget model")
    print(f"Target thrust: {THRUST_N/1000:.3f} kN")
    print(f"Ideal fluid-power floor: {IDEAL_FLUID_POWER_W/1000:.1f} kW")
    print()

    # 80 kW allowance for plasma-source + gas-current Joule overhead.
    extra_budget = 80_000.0

    cases = [
        # B, sigma_peak, tau, rep rate, drive window
        (5.0, 500.0, 5e-6, 8_000.0, 5e-6),
        (5.0, 800.0, 5e-6, 8_000.0, 5e-6),
        (8.0, 500.0, 5e-6, 5_000.0, 5e-6),
        (8.0, 800.0, 5e-6, 3_000.0, 5e-6),
    ]

    for case in cases:
        result = operating_point(*case, extra_power_budget_W=extra_budget)
        print(result)

    print("\nInterpretation")
    print(
        "A candidate pulse regime closes the reduced-order overhead budget only if "
        "the real plasma source deposits no more than the reported epsilon_pulse limit "
        "while producing the assumed conductivity waveform over the useful volume."
    )
