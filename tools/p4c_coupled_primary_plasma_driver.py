"""CRTFE P4C coupled primary/plasma-loop driver screen.

Goal lock: full-stream atmospheric electromagnetic propulsion using
pulsed conductivity, a stationary high-B HTS pole pair, and direct JxB
momentum transfer. This script only screens the pulsed transformer drive.

The model is a fixed-mutual-inductance transformer equivalent:

  L1 di1/dt + M di2/dt + R1 i1 = Vc
  M di1/dt + L2 di2/dt + R2(t) i2 = 0
  C dVc/dt = -i1

R2(t) may grow exponentially to represent conductivity decay.
The solver uses RK4 so no external Python packages are required.
"""

from math import sqrt, exp

# Vehicle / module anchor
MASS_KG = 650.0
G = 9.81
MODULES = 4
B0_T = 8.0
ACTIVE_LEG_M = 1.0
PULSE_RATE_HZ = 3000.0
TOTAL_THRUST_N = MASS_KG * G
MODULE_THRUST_N = TOTAL_THRUST_N / MODULES
TARGET_CURRENT_IMPULSE_AS = MODULE_THRUST_N / (2.0 * B0_T * ACTIVE_LEG_M * PULSE_RATE_HZ)


def rk4_step(fun, t, y, dt):
    k1 = fun(t, y)
    y2 = [a + 0.5 * dt * b for a, b in zip(y, k1)]
    k2 = fun(t + 0.5 * dt, y2)
    y3 = [a + 0.5 * dt * b for a, b in zip(y, k2)]
    k3 = fun(t + 0.5 * dt, y3)
    y4 = [a + dt * b for a, b in zip(y, k3)]
    k4 = fun(t + dt, y4)
    return [a + dt * (b1 + 2*b2 + 2*b3 + b4) / 6.0
            for a, b1, b2, b3, b4 in zip(y, k1, k2, k3, k4)]


def simulate(V0, pulse_s=5e-6, C=20e-6, L1=1e-6, L2=0.39e-6,
             k=0.8, R1=0.003, R2_0=0.010, sigma_decay_s=None,
             steps=1200):
    M = k * sqrt(L1 * L2)
    det = L1 * L2 - M * M
    dt = pulse_s / steps

    # state = i1, i2, capacitor voltage, primary R loss, plasma R loss
    y = [0.0, 0.0, V0, 0.0, 0.0]
    t = 0.0
    impulse_signed = 0.0
    prev_i2 = 0.0
    peak_i1 = 0.0
    peak_i2 = 0.0
    sign_reversal = False

    def rhs(tt, yy):
        i1, i2, vc, _, _ = yy
        R2 = R2_0 if sigma_decay_s is None else R2_0 * exp(tt / sigma_decay_s)
        b1 = vc - R1 * i1
        b2 = -R2 * i2
        di1 = (b1 * L2 - b2 * M) / det
        di2 = (b2 * L1 - b1 * M) / det
        dvc = -i1 / C
        return [di1, di2, dvc, R1*i1*i1, R2*i2*i2]

    for _ in range(steps):
        y_new = rk4_step(rhs, t, y, dt)
        i2_new = y_new[1]
        impulse_signed += -0.5 * (prev_i2 + i2_new) * dt
        if prev_i2 < 0.0 and i2_new > 0.0:
            sign_reversal = True
        prev_i2 = i2_new
        y = y_new
        t += dt
        peak_i1 = max(peak_i1, abs(y[0]))
        peak_i2 = max(peak_i2, abs(y[1]))

    i1, i2, vc, e_r1, e_r2 = y
    Wmag = 0.5*L1*i1*i1 + 0.5*L2*i2*i2 + M*i1*i2
    return {
        "impulse_As": impulse_signed,
        "peak_i1_A": peak_i1,
        "peak_i2_A": peak_i2,
        "vc_end_V": vc,
        "primary_loss_J": e_r1,
        "plasma_loss_J": e_r2,
        "magnetic_energy_end_J": Wmag,
        "initial_cap_energy_J": 0.5*C*V0*V0,
        "sign_reversal": sign_reversal,
        "M_H": M,
    }


def required_voltage(**kwargs):
    base = simulate(1.0, **kwargs)
    if base["impulse_As"] <= 0:
        raise ValueError("No forward current impulse in this pulse window")
    V0 = TARGET_CURRENT_IMPULSE_AS / base["impulse_As"]
    result = simulate(V0, **kwargs)
    result["V0_V"] = V0
    return result


def average_em_power_kW(result, recovery=0.98):
    unrecovered = (result["primary_loss_J"] + result["plasma_loss_J"]
                   + (1.0-recovery)*result["magnetic_energy_end_J"])
    return unrecovered * PULSE_RATE_HZ * MODULES / 1000.0


if __name__ == "__main__":
    print("CRTFE P4C coupled primary/plasma-loop driver")
    print(f"Target current impulse/module/pulse: {TARGET_CURRENT_IMPULSE_AS:.5f} A*s")
    print("\nCoupling sweep: C=20 uF, L1=1 uH, L2=0.39 uH, R2=10 mOhm, 5 us")
    for k in (0.6, 0.7, 0.8, 0.9):
        r = required_voltage(k=k)
        print(
            f"k={k:.1f}: V0={r['V0_V']:.0f} V, "
            f"I1pk={r['peak_i1_A']/1000:.1f} kA, "
            f"I2pk={r['peak_i2_A']/1000:.1f} kA, "
            f"Ecap={r['initial_cap_energy_J']:.1f} J, "
            f"P_EM(98%)={average_em_power_kW(r):.1f} kW"
        )

    print("\nConductivity-decay / pulse-window sweep: k=0.8, tau_sigma=5 us")
    for pulse_us in (3.0, 4.0, 5.0, 6.0, 7.0, 7.5):
        r = required_voltage(pulse_s=pulse_us*1e-6, sigma_decay_s=5e-6)
        print(
            f"tp={pulse_us:>3.1f} us: V0={r['V0_V']:.0f} V, "
            f"I1pk={r['peak_i1_A']/1000:.1f} kA, "
            f"I2pk={r['peak_i2_A']/1000:.1f} kA, "
            f"P_EM(98%)={average_em_power_kW(r):.1f} kW, "
            f"reverse={r['sign_reversal']}"
        )
