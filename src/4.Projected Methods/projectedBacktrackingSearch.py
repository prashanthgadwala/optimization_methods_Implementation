# Optimization for Engineers - Dr.Johannes Hild
# projected backtracking line search

# Purpose: Find t to satisfy f(x+t*d)< f(x) - sigma/t*norm(x-P(x - t*gradient))**2

# Input Definition:
# f: objective class with methods .objective() and .gradient() and .hessian()
# P: box projection class with method .project()
# x: column vector in R**n (domain point)
# d: column vector in R**n (search direction)
# sigma: value in (0,1), marks quality of decrease. Default value: 1.0e-4.
# verbose: bool, if set to true, verbose information is displayed

# Output Definition:
# t: t is set to the biggest 2**m, such that 2**m satisfies the projected sufficient decrease condition

# Required files:
# <none>

# Test cases:
# p = np.array([[0], [1]])
# myObjective = simpleValleyObjective(p)
# a = np.array([[-2], [1]])
# b = np.array([[2], [2]])
# eps = 1.0e-6
# myBox = projectionInBox(a, b, eps)
# x = np.array([[1], [1]])
# d = np.array([[-1.99], [0]])
# sigma = 0.5
# t = projectedBacktrackingSearch(myObjective, myBox, x, d, sigma, 1)
# should return t = 0.5

import numpy as np


def projectedBacktrackingSearch(f, P, x: np.array, d: np.array, sigma=1.0e-4, verbose=0):
    xp = P.project(x)
    gradx = f.gradient(xp)
    decrease = gradx.T @ d

    if decrease >= 0:
        raise TypeError('descent direction check failed!')

    if sigma <= 0 or sigma >= 1:
        raise TypeError('range of sigma is wrong!')

    if verbose:
        print('Start projectedBacktrackingSearch...')

    beta = 0.5
    t = 1
    # INCOMPLETE CODE STARTS
    
    if np.array_equal(P.project(x + d), x): # check if x+td is inside the feasible set
        raise TypeError('xk is stationary point!') # raise error for stationary point

    def w1(t): # Wolfe-Powell condition 1
        return (f.objective(P.project(x + t * d)) <= f.objective(x) + sigma * f.gradient(x).T @ (P.project(x + t * d) - x)) and (f.gradient(x).T @ (P.project(x + t * d) - x) < 0 ) # check for sufficient decrease
    
    def w2(t): # Wolfe-Powell condition 2
        return (not np.array_equal(x + t * d, P.project(x + t * d))) or (f.gradient(P.project(x + t * d)).T @ d >= rho * f.gradient(x).T @ d) # check if x+td is inside the feasible set
    
    if not w1(t):  # while Wolfe-Powell condition 1 is not satisfied
        t = 0.5 * t # halve t
        while not w1(t): # while Wolfe-Powell condition 1 is not satisfied
            t = 0.5 * t # halve t again
        tminus = t # store t for Wolfe-Powell condition 2 check
        tplus = 2 * t # store t for Wolfe-Powell condition 2 check

    elif w2(t): # if Wolfe-Powell condition 2 is satisfied
        return t # return t if Wolfe-Powell condition 2 is satisfied
    
    else:   # if Wolfe-Powell condition 2 is not satisfied
        t = 2 * t # double t 
        while (w1(t) and np.array_equal(P.project(x + t * d), x + t * d)): # while Wolfe-Powell condition 1 is satisfied and x+td is inside the feasible set
            t = 2 * t # double t again
        tminus = t / 2 # store t for Wolfe-Powell condition 2 check
        tplus = t   # store t for Wolfe-Powell condition 2 check
    
    t = tminus # set t to t minus

    while not w2(t): # while Wolfe-Powell condition 2 is not satisfied
        t = 0.5 * (tminus + tplus) # set t to average of t minus and t plus
        if w1(t): # if Wolfe-Powell condition 1 is satisfied
            tminus = t # set t minus to t
        else: # if Wolfe-Powell condition 1 is not satisfied
            tplus = t # set t plus to t

    # INCOMPLETE CODE ENDS

    if verbose:
        print('projectedBacktrackingSearch terminated with t=', t)

    return t
