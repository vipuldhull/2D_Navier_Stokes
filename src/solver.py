import numpy as np
from boundary_condition import apply_velocity_bc, apply_pressure_bc


def build_up_b(rho, dt, dx, dy, u, v):
    b = np.zeros_like(u)

    b[1:-1, 1:-1] = rho * (
        (1.0 / dt) * (
            (u[1:-1, 2:] - u[1:-1, 0:-2]) / (2.0 * dx) +
            (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2.0 * dy)
        )
        - ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2.0 * dx))**2
        - 2.0 * (
            (u[2:, 1:-1] - u[0:-2, 1:-1]) / (2.0 * dy) *
            (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2.0 * dx)
        )
        - ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2.0 * dy))**2
    )

    return b


def pressure_poisson(p, dx, dy, b, nit):
    pn = np.empty_like(p)

    for _ in range(nit):
        pn[:] = p[:]

        p[1:-1, 1:-1] = (
            ((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 +
             (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
            (2.0 * (dx**2 + dy**2))
            - dx**2 * dy**2 / (2.0 * (dx**2 + dy**2)) * b[1:-1, 1:-1]
        )

        p = apply_pressure_bc(p)

    return p


def cavity_flow(nx, ny, nt, nit, u, v, dt, dx, dy, p, rho, nu, u_lid):
    un = np.empty_like(u)
    vn = np.empty_like(v)

    for n in range(nt):
        un[:] = u[:]
        vn[:] = v[:]

        b = build_up_b(rho, dt, dx, dy, u, v)
        p = pressure_poisson(p, dx, dy, b, nit)

        u[1:-1, 1:-1] = (
            un[1:-1, 1:-1]
            - un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, 0:-2])
            - vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[0:-2, 1:-1])
            - dt / (2.0 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2])
            + nu * (
                dt / dx**2 * (un[1:-1, 2:] - 2.0 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                dt / dy**2 * (un[2:, 1:-1] - 2.0 * un[1:-1, 1:-1] + un[0:-2, 1:-1])
            )
        )

        v[1:-1, 1:-1] = (
            vn[1:-1, 1:-1]
            - un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2])
            - vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1])
            - dt / (2.0 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1])
            + nu * (
                dt / dx**2 * (vn[1:-1, 2:] - 2.0 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                dt / dy**2 * (vn[2:, 1:-1] - 2.0 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])
            )
        )

        u, v = apply_velocity_bc(u, v, u_lid)

    return u, v, p
