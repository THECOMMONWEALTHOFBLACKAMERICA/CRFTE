"""CRTFE P4B bipolar static-pole inductive-loop screening model.

Goal
----
Stay inside the original CRTFE architecture: full-stream atmospheric air,
no rotating propulsor, pulsed conductivity, induced plasma current, strong
stationary magnetic field, and direct JxB momentum transfer.

The P4B topology uses a closed plasma current loop spanning two adjacent
static magnetic poles of opposite sign. Current reverses in the return leg
and B reverses with it, so both transverse legs contribute axial force in
the same direction.

This is a reduced-order RL/force/energy screening model, not a validated
plasma-MHD solver and not evidence of flight feasibility.
"""

from math import exp, pi

MU0 = 4*pi*1e-7
MASS_KG = 650.0
G = 9.81
N_MODULES = 4
THRUST_TOTAL_N = MASS_KG*G
THRUST_MODULE_N = THRUST_TOTAL_N/N_MODULES

# Representative module geometry
LEG_LENGTH_M = 1.0       # transverse current-leg length
MODULE_HEIGHT_M = 1.2
POLE_LENGTH_M = 0.25     # each +B/-B zone axial extent
LINKED_DRIVE_AREA_M2 = 0.10

# Pulse baseline
F_HZ = 3000.0
TP_S = 5e-6
RECOVERY = 0.98


def geometry_R_L(sigma_S_m, pole_length_m=POLE_LENGTH_M,
                 height_m=MODULE_HEIGHT_M, leg_length_m=LEG_LENGTH_M,
                 k_R=1.2, k_L=1.5):
    """Estimate plasma-loop resistance and geometric inductance.

    Resistance model: two broad transverse plasma legs, each with current
    cross section ~ height*pole_length, plus a connector penalty k_R.

    Inductance model: broad paired-sheet loop scale L~mu0*d*l/w, with k_L
    absorbing end/closure/fringe contributions. This is deliberately a
    screening estimate; detailed 3D EM is required before hardware design.
    """
    R = k_R * 2.0*leg_length_m/(sigma_S_m*height_m*pole_length_m)
    L = k_L * MU0*pole_length_m*leg_length_m/height_m
    return R, L


def current_impulse_required(B_T, f_hz=F_HZ, leg_length_m=LEG_LENGTH_M):
    """Integral I dt required per pulse per module.

    Both transverse legs add force because J and B reverse together:
        F_avg = 2 B l f integral(I dt)
    """
    return THRUST_MODULE_N/(2.0*B_T*leg_length_m*f_hz)


def solve_constant_voltage_pulse(B_T, sigma_S_m,
                                 pole_length_m=POLE_LENGTH_M,
                                 tp_s=TP_S, f_hz=F_HZ,
                                 recovery=RECOVERY,
                                 linked_area_m2=LINKED_DRIVE_AREA_M2,
                                 k_R=1.2, k_L=1.5):
    R, L = geometry_R_L(sigma_S_m, pole_length_m=pole_length_m,
                        k_R=k_R, k_L=k_L)
    tau = L/R
    target = current_impulse_required(B_T, f_hz=f_hz)

    # RL response for a constant induced loop voltage V during 0<t<tp:
    # I(t)=V/R*(1-exp(-t/tau))
    # integral I dt = V/R*[tp-tau(1-exp(-tp/tau))]
    a = tp_s - tau*(1.0-exp(-tp_s/tau))
    V = target*R/a
    I_end = V/R*(1.0-exp(-tp_s/tau))

    # Analytic integral of I^2 from 0 to tp
    x = tp_s/tau
    int_i2 = (V/R)**2 * (
        tp_s - 2.0*tau*(1.0-exp(-x))
        + 0.5*tau*(1.0-exp(-2.0*x))
    )
    E_joule_module = R*int_i2
    E_mag_end_module = 0.5*L*I_end**2

    # Whole-aircraft repeated losses
    P_joule_total = E_joule_module*f_hz*N_MODULES
    P_unrecovered_mag = (1.0-recovery)*E_mag_end_module*f_hz*N_MODULES

    flux_swing = V*tp_s
    drive_field_swing = flux_swing/linked_area_m2

    return {
        "B_static_T": B_T,
        "sigma_on_S_m": sigma_S_m,
        "R_loop_mohm": 1e3*R,
        "L_loop_uH": 1e6*L,
        "L_over_R_us": 1e6*tau,
        "required_current_impulse_A_s": target,
        "drive_voltage_V": V,
        "I_end_kA": I_end/1e3,
        "drive_flux_mWb": 1e3*flux_swing,
        "equiv_drive_field_mT": 1e3*drive_field_swing,
        "joule_power_kW": P_joule_total/1e3,
        "unrecovered_magnetic_power_kW": P_unrecovered_mag/1e3,
        "EM_overhead_kW": (P_joule_total+P_unrecovered_mag)/1e3,
    }


if __name__ == "__main__":
    print("CRTFE P4B bipolar static-pole inductive-loop screen")
    print(f"Target thrust: {THRUST_TOTAL_N/1000:.3f} kN total")
    print(f"Pulse: {F_HZ/1000:.1f} kHz, {TP_S*1e6:.1f} us")
    print(f"Assumed magnetic-energy recovery: {RECOVERY*100:.0f}%")
    print()
    for B in (5.0, 8.0):
        for sigma in (100.0, 300.0, 800.0, 1500.0):
            r = solve_constant_voltage_pulse(B, sigma)
            print(r)
