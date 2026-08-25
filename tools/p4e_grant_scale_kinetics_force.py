"""CRTFE P4E grant-scale reduced-order plasma/MHD screen.

Purpose
-------
Find a laboratory-scale experiment that can prove or falsify the key CRTFE
mechanism before any vehicle-scale claim is made.

The model represents repetitive ns-pulse ionization in flowing air with
between-pulse electron losses from:

    dn_e/dt = -beta*n_e^2 - n_e/tau_attach

Each ns pulse adds Delta_n electrons/ions.  RF vibrational conditioning is
represented parametrically by a longer effective attachment time and a lower
effective electron-ion recombination coefficient, bounded by published
atmospheric-air vibrational-nonequilibrium literature.

The model then maps mean electron density into transverse conductivity and
reduced-order Lorentz force:

    sigma = e*n_e*mu_e/(1 + (mu_e B)^2)
    F = sigma*E_drive*B*V
    P_J = sigma*E_drive^2*V

This is not a Boltzmann/chemical-kinetics solver and is not evidence of
propulsion performance.  It defines a falsifiable laboratory operating window.
"""

from math import exp

E_CHARGE = 1.602176634e-19


def periodic_electron_density(
    delta_n_cm3,
    repetition_hz,
    beta_cm3_s,
    tau_attach_us,
    cycles=3000,
    steps_per_period=120,
):
    """Return steady periodic mean/min/max electron density in cm^-3."""
    period = 1.0 / repetition_hz
    dt = period / steps_per_period
    tau_attach = tau_attach_us * 1e-6
    n = 0.0
    samples = []

    def loss(nn):
        return -(beta_cm3_s * nn * nn + nn / tau_attach)

    for cycle in range(cycles):
        n += delta_n_cm3
        for _ in range(steps_per_period):
            k1 = loss(n)
            n_mid = max(0.0, n + 0.5 * dt * k1)
            k2 = loss(n_mid)
            n = max(0.0, n + dt * k2)
            if cycle >= cycles - 200:
                samples.append(n)

    mean = sum(samples) / len(samples)
    return mean, min(samples), max(samples)


def lab_point(
    delta_n_cm3=3e12,
    repetition_hz=50_000.0,
    beta_cm3_s=3e-8,
    tau_attach_us=100.0,
    mobility_m2_Vs=0.05,
    B_T=2.0,
    E_drive_V_m=5000.0,
    active_volume_cm3=50.0,
    ion_pair_energy_eV=75.0,
):
    mean, nmin, nmax = periodic_electron_density(
        delta_n_cm3,
        repetition_hz,
        beta_cm3_s,
        tau_attach_us,
    )

    n_m3 = mean * 1e6
    hall_factor = 1.0 / (1.0 + (mobility_m2_Vs * B_T) ** 2)
    sigma = E_CHARGE * n_m3 * mobility_m2_Vs * hall_factor
    volume_m3 = active_volume_cm3 * 1e-6

    force_N = sigma * E_drive_V_m * B_T * volume_m3
    joule_W = sigma * E_drive_V_m**2 * volume_m3

    pairs_per_pulse = delta_n_cm3 * 1e6 * volume_m3
    ionization_lower_bound_W = (
        pairs_per_pulse * ion_pair_energy_eV * E_CHARGE * repetition_hz
    )

    return {
        "n_mean_cm3": mean,
        "n_min_cm3": nmin,
        "n_max_cm3": nmax,
        "sigma_S_m": sigma,
        "force_mN": force_N * 1e3,
        "joule_W": joule_W,
        "ionization_lower_bound_W": ionization_lower_bound_W,
    }


if __name__ == "__main__":
    cases = [
        ("unconditioned", 50_000, 1e-7, 0.15, 3e12),
        ("attachment suppressed", 50_000, 1e-7, 100.0, 3e12),
        ("moderate RF conditioned", 50_000, 3e-8, 100.0, 3e12),
        ("strong RF conditioned", 50_000, 1e-8, 100.0, 3e12),
        ("high-PRF conditioned", 100_000, 1e-8, 100.0, 1e12),
    ]

    print("CRTFE P4E grant-scale 50 cm^3 screen")
    print("B=2 T, E_drive=5 kV/m, mobility=0.05 m^2/V/s")
    for name, f, beta, taua, dn in cases:
        r = lab_point(
            delta_n_cm3=dn,
            repetition_hz=f,
            beta_cm3_s=beta,
            tau_attach_us=taua,
        )
        print(
            f"{name:26s}  ne={r['n_mean_cm3']:.2e} cm^-3  "
            f"sigma={r['sigma_S_m']:.4f} S/m  "
            f"F={r['force_mN']:.2f} mN  "
            f"PJ={r['joule_W']:.1f} W  "
            f"Pion,lb={r['ionization_lower_bound_W']:.1f} W"
        )
