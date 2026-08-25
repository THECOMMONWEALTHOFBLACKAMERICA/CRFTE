"""CRTFE multispecies conductivity-impulse bound.

Bounding model for the time-integrated conductivity contributed by free electrons
and longer-lived positive/negative ions after one atmospheric plasma event.

This is not a chemistry solver. Species mobilities/lifetimes are exposed as inputs
and must be replaced with regime-specific measurements before design use.
"""

from dataclasses import dataclass
from math import sqrt

F_N = 650.0 * 9.81


@dataclass
class Species:
    name: str
    mobility_m2_Vs: float
    lifetime_s: float
    relative_initial_density: float = 1.0

    @property
    def mobility_lifetime(self) -> float:
        return self.relative_initial_density * self.mobility_m2_Vs * self.lifetime_s


def integrated_transport(species):
    """Return sum(mu_s * tau_s * relative density)."""
    return sum(s.mobility_lifetime for s in species)


def lower_bound_extra_power(force_N, B_T, activation_energy_eV, transport_integral):
    """Generalized lower bound using integrated carrier transport.

    Electron-only result uses transport_integral = mu_e * tau_e.
    Multispecies tail replaces that with sum_s relative_density_s * mu_s * tau_s.

    Assumes all listed species descend from the same created charge event and their
    current contributions add. It excludes detailed reaction branching, ambipolar
    fields, Hall/tensor effects, wall loss, spatial nonuniformity, and source losses.
    """
    return (2.0 * force_N / B_T) * sqrt(activation_energy_eV / transport_integral)


def run():
    # Literature-inspired bounding values; not a dry-air chemistry claim.
    electron = Species("e-", 0.055, 50e-9)

    # Atmospheric ion mobilities are O(1e-4 m^2/V/s). The values below are
    # representative placeholders informed by published air mobility data.
    o2_plus = Species("O2+", 2.5e-4, 28e-6)
    no_plus = Species("NO+", 3.5e-4, 117e-6)
    o2_minus = Species("O2-", 2.4e-4, 17e-6)
    o3_minus = Species("O3-", 2.4e-4, 23e-6)

    cases = {
        "electron_only": [electron],
        "e + O2+ + O2-": [electron, o2_plus, o2_minus],
        "e + NO+ + O3-": [electron, no_plus, o3_minus],
    }

    print("CRTFE multispecies time-integrated conductivity bound\n")
    for name, sp in cases.items():
        integ = integrated_transport(sp)
        print(f"{name}: sum(mu*tau) = {integ:.3e} m^2/V")
        for B in [5.0, 8.0, 12.0, 20.0]:
            p34 = lower_bound_extra_power(F_N, B, 34.0, integ)
            p045 = lower_bound_extra_power(F_N, B, 0.45, integ)
            print(
                f"  B={B:4.1f} T -> fresh-pair lower bound {p34/1e6:8.2f} MW; "
                f"0.45-eV reactivation bound {p045/1e6:8.2f} MW"
            )
        print()


if __name__ == "__main__":
    run()
