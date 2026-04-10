import matplotlib.pyplot as plt
import numpy as np


def plot_results(x, y, u, v, p, save_path=None):
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, p, levels=30)
    plt.colorbar(label="Pressure")
    plt.quiver(X, Y, u, v)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Lid-Driven Cavity: Pressure and Velocity Field")

    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches="tight")

    plt.show()


def plot_streamlines(x, y, u, v, save_path=None):
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(8, 6))
    plt.streamplot(X, Y, u, v, density=1.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Lid-Driven Cavity: Streamlines")

    if save_path:
        plt.savefig(save_path, dpi=200, bbox_inches="tight")

    plt.show()
