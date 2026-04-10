# 2D Lid-Driven Cavity Flow Solver

This project solves the incompressible 2D Navier–Stokes equations for a lid-driven cavity using Python and finite differences.

## Features
- 2D incompressible flow
- Pressure-Poisson formulation
- Finite-difference discretization
- Velocity and pressure visualization

## Governing Equations
The solver uses the incompressible continuity and momentum equations in 2D.

## Numerical Method
- Uniform Cartesian grid
- Explicit time stepping
- Pressure Poisson correction
- No-slip boundary conditions
- Moving lid at the top wall

## How to Run
```bash
pip install -r requirements.txt
cd src
python main.py
