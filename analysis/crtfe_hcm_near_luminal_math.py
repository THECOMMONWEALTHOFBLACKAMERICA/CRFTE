import numpy as np
from scipy.linalg import eig


def constitutive_convolution(depth, phase, H):
    S = 2 * H + 1
    M = np.eye(S, dtype=complex)
    for i in range(S):
        if i - 1 >= 0:
            M[i, i - 1] += 0.5 * depth * np.exp(1j * phase)
        if i + 1 < S:
            M[i, i + 1] += 0.5 * depth * np.exp(-1j * phase)
    return M


def equal_depth_pole_bounds(m, delta):
    c = abs(np.cos(delta / 2))
    s2 = 1 - c * c
    pmax = (1 + m * c) ** 2
    if c >= m:
        pmin = (1 - m * c) ** 2
    else:
        pmin = (1 - m * m) * s2
    return 1 / np.sqrt(pmax), 1 / np.sqrt(pmin)


def k_spectrum(omega, Omega, K, me, mm, delta, H):
    hs = np.arange(-H, H + 1)
    eps = constitutive_convolution(me, 0, H)
    mu = constitutive_convolution(mm, delta, H)
    W = np.diag(omega + hs * Omega)
    NK = np.diag(hs * K)
    A = np.block([
        [-NK, W @ mu],
        [W @ eps, -NK],
    ])
    vals, vecs = eig(A)
    return vals, vecs


def omega_spectrum(k, Omega, K, me, mm, delta, H):
    hs = np.arange(-H, H + 1)
    S = len(hs)
    eps = constitutive_convolution(me, 0, H)
    mu = constitutive_convolution(mm, delta, H)
    Q = np.diag(k + hs * K)
    NOm = np.diag(hs * Omega)
    Z = np.zeros((S, S), dtype=complex)
    A = np.block([
        [Q, -NOm @ mu],
        [-NOm @ eps, Q],
    ])
    B = np.block([
        [Z, mu],
        [eps, Z],
    ])
    vals, vecs = eig(A, B)
    return vals, vecs


if __name__ == '__main__':
    m = 0.10
    for deg in (0, 60, 90, 120, 150, 170, 180):
        lo, hi = equal_depth_pole_bounds(m, np.deg2rad(deg))
        print(f'delta={deg:3d} deg : u in [{lo:.9f}, {hi:.9f}]')
