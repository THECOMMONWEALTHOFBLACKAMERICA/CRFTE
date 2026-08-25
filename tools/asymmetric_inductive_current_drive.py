"""CRTFE P4A asymmetric inductive current-drive screening model.

Goal lock
---------
This model stays inside the primary CRTFE objective: large-area, no-moving-parts
atmospheric propulsion using full-stream air, controlled conductivity/current,
and a strong stationary magnetic field.

The proposed current-drive subarchitecture separates the two magnetic functions:

1. a strong stationary HTS bias field B0 supplies the Lorentz-force field;
2. a much smaller, fast-changing induction field supplies loop EMF to create a
   transverse plasma current without plasma-contact electrodes.

A fast forward flux ramp is applied while the air is conductive. Transformer flux
is reset only after effective conductivity has decayed or the conductive packet has
advected away from the high-B interaction region, suppressing reverse impulse.

This is a reduced-order theoretical screen, not a validated plasma/circuit solver.
"""

from math import exp, pi, sqrt

MASS_KG = 650.0
G = 9.81
ACTIVE_AREA_M2 = 4.8
INTERACTION_LENGTH_M = 0.5
ACTIVE_VOLUME_M3 = ACTIVE_AREA_M2 * INTERACTION_LENGTH_M
THRUST_N = MASS_KG * G
MU0 = 4.0 * pi * 1e-7


def operating_point(
    B0_T: float,
    sigma_on_S_m: float,
    repetition_hz: float,
    pulse_s: float,
    loop_path_m: float = 2.0,
    linked_area_m2: float = 0.10,
):
    """Return the idealized pulse requirements.

    Force model:
        F = B0 * J_avg * V

    With duty D=f*tau:
        J_on = J_avg/D
        E_ind = J_on/sigma_on
        EMF_loop = E_ind * l_loop
        DeltaPhi ~= EMF_loop * tau
        DeltaB_drive ~= DeltaPhi/A_link

    The changing drive flux induces the current; B0 is stationary and provides the
    dominant Lorentz-force field.
    """
    duty = repetition_hz * pulse_s
    if not 0.0 < duty <= 1.0:
        raise ValueError("repetition_hz * pulse_s must be in (0, 1]")

    J_avg = THRUST_N / (B0_T * ACTIVE_VOLUME_M3)
    J_on = J_avg / duty
    E_ind = J_on / sigma_on_S_m
    emf_loop = E_ind * loop_path_m
    delta_phi = emf_loop * pulse_s
    delta_B_drive = delta_phi / linked_area_m2
    sigma_eff = duty * sigma_on_S_m
    P_joule = THRUST_N**2 / (
        B0_T**2 * ACTIVE_VOLUME_M3 * sigma_eff
    )

    return {
        "B0_T": B0_T,
        "sigma_on_S_m": sigma_on_S_m,
        "repetition_kHz": repetition_hz / 1000.0,
        "pulse_us": pulse_s * 1e6,
        "duty": duty,
        "sigma_eff_S_m": sigma_eff,
        "J_avg_A_m2": J_avg,
        "J_on_kA_m2": J_on / 1000.0,
        "E_ind_V_m": E_ind,
        "loop_emf_V": emf_loop,
        "delta_phi_mWb": delta_phi * 1000.0,
        "delta_B_drive_mT": delta_B_drive * 1000.0,
        "P_joule_kW": P_joule / 1000.0,
    }


def reset_reverse_impulse_fraction(
    conductivity_decay_s: float,
    reset_delay_s: float,
    reset_duration_s: float,
) -> float:
    """Approximate reverse-current impulse during flux reset.

    Assume effective conductivity after the useful pulse decays exponentially:
        sigma(t) = sigma0 exp(-t/tau_sigma)

    The reverse reset ramp restores the same flux over reset_duration. Relative to
    a flat forward current pulse, the reverse-current impulse fraction is

        r = exp(-delay/tau_sigma)
            * (tau_sigma/reset_duration)
            * [1-exp(-reset_duration/tau_sigma)]

    This intentionally isolates the commutation timing issue. Real circuits require
    coupled field/circuit/plasma simulation.
    """
    tau = conductivity_decay_s
    tr = reset_duration_s
    td = reset_delay_s
    return exp(-td / tau) * (tau / tr) * (1.0 - exp(-tr / tau))


def skin_depth_m(sigma_S_m: float, frequency_hz: float) -> float:
    """Classical collisional conductor skin-depth sanity check."""
    return sqrt(2.0 / (MU0 * sigma_S_m * 2.0 * pi * frequency_hz))


if __name__ == "__main__":
    print("CRTFE P4A asymmetric inductive current-drive screen")
    print(f"Hover thrust: {THRUST_N/1000:.3f} kN")
    print(f"Active volume: {ACTIVE_VOLUME_M3:.3f} m^3")
    print()

    cases = (
        (8.0, 800.0),
        (8.0, 300.0),
        (5.0, 800.0),
    )
    for B0, sigma in cases:
        result = operating_point(
            B0_T=B0,
            sigma_on_S_m=sigma,
            repetition_hz=3000.0,
            pulse_s=5e-6,
            loop_path_m=2.0,
            linked_area_m2=0.10,
        )
        print(result)
        print(
            f"skin depth @3 kHz: {skin_depth_m(sigma, 3000.0):.3f} m"
        )

    print("\nFlux-reset reverse-impulse screen")
    for tau_us in (0.05, 0.5, 5.0, 20.0, 100.0):
        frac = reset_reverse_impulse_fraction(
            conductivity_decay_s=tau_us * 1e-6,
            reset_delay_s=10e-6,
            reset_duration_s=50e-6,
        )
        print(f"tau_sigma={tau_us:>6g} us -> reverse impulse fraction={frac:.6g}")
