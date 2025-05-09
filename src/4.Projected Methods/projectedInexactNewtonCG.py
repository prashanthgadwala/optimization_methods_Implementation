# Optimization for Engineers - Dr.Johannes Hild
# projected inexact Newton descent

# Purpose: Find xmin to satisfy norm(xmin - P(xmin - gradf(xmin)))<=eps
# Iteration: x_k = P(x_k + t_k * d_k)
# d_k starts as a steepest descent step and then CG steps are used to improve the descent direction until negative curvature is detected or a full Newton step is made.
# t_k results from projected backtracking

# Input Definition:
# f: objective class with methods .objective() and .gradient()
# P: box projection class with method .project() and .activeIndexSet()
# x0: column vector in R ** n(domain point)
# eps: tolerance for termination. Default value: 1.0e-3
# verbose: bool, if set to true, verbose information is displayed

# Output Definition:
# xmin: column vector in R ** n(domain point)

# Required files:
# dH = projectedHessApprox(f, P, x, d) from projectedHessApprox.py
# t = projectedBacktrackingSearch(f, P, x, d) from projectedBacktrackingSearch.py

# Test cases:
# p = np.array([[1], [1]])
# myObjective = simpleValleyObjective(p)
# a = np.array([[1], [1]])
# b = np.array([[2], [2]])
# myBox = projectionInBox(a, b)
# x0 = np.array([[2], [2]], dtype=float)
# eps = 1.0e-3
# xmin = projectedInexactNewtonCG(myObjective, myBox, x0, eps, 1)
# should return xmin close to [[1],[1]]

import numpy as np
import projectedBacktrackingSearch as PB
import projectedHessApprox as PHA


def projectedInexactNewtonCG(f, P, x0: np.array, eps=1.0e-3, verbose=0):

    if eps <= 0:
        raise TypeError('range of eps is wrong!')

    if verbose:
        print('Start projectedInexactNewtonCG...')

    countIter = 0
    xp = P.project(x0)
    # INCOMPLETE CODE STARTS

    # Step 2: Initialize ηk
    gradx = f.gradient(xp)
    stationarity = np.linalg.norm(xp - P.project(xp - gradx))
    eta_k = min(0.5, stationarity) * stationarity

    while stationarity > eps:
        countIter += 1

        # Step 3a: Initialize CG variables
        xj = xp
        rj = gradx
        dj = -rj

        while np.linalg.norm(rj) > eta_k:
            # Step 3b.i: Approximate dA ← ∇²Ωf(xk)dj
            dA = PHA.projectedHessApprox(f, P, xp, dj)

            # Step 3b.ii: Compute ρj
            rho_j = dj.T @ dA

            # Step 3b.iii: Check curvature condition
            if rho_j <= eps * np.linalg.norm(dj) ** 2:
                break

            # Step 3b.iv: Compute step size tj
            t_j = (rj.T @ rj) / rho_j
            xj = xj + t_j * dj

            # Step 3b.v: Update residual rj
            r_old = rj
            rj = r_old + t_j * dA

            # Step 3b.vi: Update βj and dj
            beta_j = (rj.T @ rj) / (r_old.T @ r_old)
            dj = -rj + beta_j * dj

        # Step 3c: Compute dk
        if not np.allclose(xj, xp):
            dk = xj - xp
        else:
            dk = -gradx

        # Step 3d: Perform projected backtracking line search
        t_k = PB.projectedBacktrackingSearch(f, P, xp, dk)

        # Step 3e: Update xk and ηk
        xp = P.project(xp + t_k * dk)
        gradx = f.gradient(xp)
        stationarity = np.linalg.norm(xp - P.project(xp - gradx))
        eta_k = min(0.5, stationarity) * stationarity
        
    # INCOMPLETE CODE ENDS
    if verbose:
        gradx = f.gradient(xp)
        stationarity = np.linalg.norm(xp - P.project(xp - gradx))
        print('projectedInexactNewtonCG terminated after ', countIter, ' steps with stationarity =', np.linalg.norm(stationarity))

    return xp

