import numpy as np

# Domain
Lx = 1.0
Ly = 1.0

# Grid
nx = 41
ny = 41
dx = Lx / (nx - 1)
dy = Ly / (ny - 1)

# Physical properties
rho = 1.0
nu = 0.1

# Time stepping
dt = 0.001
nt = 500

# Pressure solver
nit = 50

# Lid-driven cavity
u_lid = 1.0

# Coordinates
x = np.linspace(0.0, Lx, nx)
y = np.linspace(0.0, Ly, ny)
