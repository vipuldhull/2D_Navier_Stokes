import numpy as np

from config import nx, ny, nt, nit, dx, dy, dt, rho, nu, u_lid, x, y
from solver import cavity_flow
from postprocess import plot_results, plot_streamlines


def main():
    u = np.zeros((ny, nx))
    v = np.zeros((ny, nx))
    p = np.zeros((ny, nx))

    u, v, p = cavity_flow(
        nx=nx,
        ny=ny,
        nt=nt,
        nit=nit,
        u=u,
        v=v,
        dt=dt,
        dx=dx,
        dy=dy,
        p=p,
        rho=rho,
        nu=nu,
        u_lid=u_lid,
    )

    plot_results(x, y, u, v, p, save_path="results/cavity_pressure_velocity.png")
    plot_streamlines(x, y, u, v, save_path="results/cavity_streamlines.png")


if __name__ == "__main__":
    main()
