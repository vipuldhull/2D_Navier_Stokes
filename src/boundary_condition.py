def apply_velocity_bc(u, v, u_lid):
    # Left and right walls
    u[:, 0] = 0.0
    u[:, -1] = 0.0
    v[:, 0] = 0.0
    v[:, -1] = 0.0

    # Bottom wall
    u[0, :] = 0.0
    v[0, :] = 0.0

    # Top wall
    u[-1, :] = u_lid
    v[-1, :] = 0.0

    return u, v


def apply_pressure_bc(p):
    # dp/dx = 0 on left and right
    p[:, 0] = p[:, 1]
    p[:, -1] = p[:, -2]

    # dp/dy = 0 at bottom
    p[0, :] = p[1, :]

    # p = 0 at top (reference pressure)
    p[-1, :] = 0.0

    return p
