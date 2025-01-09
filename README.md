# Optimization Methods Implementation

## Overview
This repository contains a collection of projects and implementations related to optimization methods, focusing on Finite Element Method (FEM), optimization simulation, and multibody analysis. These projects were developed as part of the "Optimization for Engineers" course by Dr. Johannes Hild.

## Key Features
- **Finite Element Method (FEM) Simulations**: Implementations of FEM for solving complex engineering problems.
- **Optimization Algorithms**: Various optimization techniques including Newton Descent, BFGS Descent, and Levenberg-Marquardt Descent.
- **Multibody Analysis**: Simulations and analyses of multibody systems.
- **Line Search Methods**: Effective line search methods like Wolfe-Powell and projected backtracking search.
- **Test Problems**: A variety of test problems to validate the implementations.

## Projects
### LAB00: Setup and Initial Implementations
- **Files**: `modelObjective.py`, `incompleteCholesky.py`, `LLTSolver.py`, `Check00.py`
- **Description**: Initial setup and basic implementations for Cholesky decomposition and linear system solving.

### LAB01: Preconditioned Conjugate Gradient Solver and Newton Descent
- **Files**: `PrecCGSolver.py`, `NewtonDescent.py`, `bananaValleyObjective.py`, `quadraticObjective.py`, `Check01.py`
- **Description**: Implementation of a highly effective linear system solver and a descent method with local q-quadratic convergence rate.

### LAB02: Wolfe-Powell Search and BFGS Descent
- **Files**: `WolfePowellSearch.py`, `BFGSDescent.py`, `simpleValleyObjective.py`, `noHessianObjective.py`, `multidimensionalObjective.py`, `Check02.py`
- **Description**: Implementation of a line search method and a descent method with global q-superlinear convergence rate.

### LAB03: Projected Methods
- **Files**: `projectedBacktrackingSearch.py`, `projectedInexactNewtonCG.py`, `projectionInBox.py`, `projectedHessApprox.py`, `boxObjective.py`, `Check03.py`
- **Description**: Implementation of line search and descent methods for box constraints.

### LAB04: Levenberg-Marquardt Descent
- **Files**: `leastSquaresModel.py`, `levenbergMarquardtDescent.py`, `Check04.py`
- **Description**: Implementation of a descent method for least squares objectives.

### LAB05: Augmented Lagrangian Methods
- **Files**: `augmentedLagrangianObjective.py`, `augmentedLagrangianDescent.py`, `Check05.py`
- **Description**: Implementation of descent methods for equality constraints and box constraints.

## Getting Started
### Prerequisites
- Python 3.x
- NumPy

### Installation
Clone the repository:
```sh
git clone https://github.com/yourusername/optimization_methods_implementation.git
cd optimization_methods_implementation
```

### Running the Tests
- Tests contains CheckX.py file to verify the correctness of the implementations. Run these files to ensure everything is working correctly:
```sh
python test/CheckX.py
```

### Contributing
Contributions are welcome! Please read the contributing guidelines for more details.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements
Special thanks to Dr. Johannes Hild for providing the course materials and guidance.
