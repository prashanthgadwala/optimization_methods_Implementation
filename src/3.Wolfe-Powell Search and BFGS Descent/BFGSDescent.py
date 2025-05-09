# Optimization for Engineers - Dr.Johannes Hild
# global BFGS descent

# Purpose: Find xmin to satisfy norm(gradf(xmin))<=eps
# Iteration: x_k = x_k + t_k * d_k
# d_k is the BFGS direction. If a descent direction check fails, d_k is set to steepest descent and the inverse BFGS matrix is reset.
# t_k results from Wolfe-Powell

# Input Definition:
# f: objective class with methods .objective() and .gradient()
# x0: column vector in R ** n(domain point)
# eps: tolerance for termination. Default value: 1.0e-3
# verbose: bool, if set to true, verbose information is displayed

# Output Definition:
# xmin: column vector in R ** n(domain point)

# Required files:
# t = WolfePowellSearch(f, x, d) from WolfePowellSearch.py

# Test cases:
# myObjective = noHessianObjective()
# x0 = np.array([[-0.01], [0.01]])
# xmin = BFGSDescent(myObjective, x0, 1.0e-6, 1)
# should return
# xmin close to [[0.26],[-0.21]] with the inverse BFGS matrix being close to [[0.0078, 0.0005], [0.0005, 0.0080]]


import numpy as np
import WolfePowellSearch as WP



def BFGSDescent(f, x0: np.array, eps=1.0e-3, verbose=0):
    if eps <= 0:
        raise TypeError('range of eps is wrong!')

    if verbose:
        print('Start BFGSDescent...')

    countIter = 0
    x = x0
    n = x0.shape[0]
    E = np.eye(n)
    B = E
    # INCOMPLETE CODE STARTS
    
    while np.linalg.norm(f.gradient(x)) > eps:
        countIter += 1
        gradx = f.gradient(x)
        d = -B @ gradx

        # Step 3b: Check if d is a descent direction
        if d.T @ gradx >= 0:
            d = -gradx
            B = E
            if verbose:
                print("Descent direction check failed. Resetting B to identity matrix.")

        # Step 3c: Wolfe-Powell line search
        t = WP.WolfePowellSearch(f, x, d, 1.0e-3, 1.0e-2, verbose)

        # Step 3d: Compute ∆gk and ∆xk
        s = t * d
        x_new = x + s
        y = f.gradient(x_new) - gradx

        # Step 3e: Update x
        x = x_new

        # Step 3f: Check curvature condition and update B
        if y.T @ s <= 0:
            B = E
            if verbose:
                print("Curvature condition failed. Resetting B to identity matrix.")
        else:
            rho = 1 / (y.T @ s)
            B = (E - rho * s @ y.T) @ B @ (E - rho * y @ s.T) + rho * s @ s.T

    # INCOMPLETE CODE ENDS
    if verbose:
        gradx = f.gradient(x)
        print('BFGSDescent terminated after ', countIter, ' steps with norm of gradient =', np.linalg.norm(gradx), 'and the inverse BFGS matrix is')
        print(B)

    return x
