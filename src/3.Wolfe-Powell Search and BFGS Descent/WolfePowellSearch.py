# Optimization for Engineers - Dr.Johannes Hild
# Wolfe-Powell line search

# Purpose: Find t to satisfy f(x+t*d)<=f(x) + t*sigma*gradf(x).T@d and gradf(x+t*d).T@d >= rho*gradf(x).T@d

# Input Definition:
# f: objective class with methods .objective() and .gradient()
# x: column vector in R ** n(domain point)
# d: column vector in R ** n(search direction)
# sigma: value in (0, 1 / 2), marks quality of decrease. Default value: 1.0e-3
# rho: value in (sigma, 1), marks quality of steepness. Default value: 1.0e-2
# verbose: bool, if set to true, verbose information is displayed

# Output Definition:
# t: t is set, such that t satisfies both Wolfe - Powell conditions

# Required files:
# < none >

# Test cases:
# p = np.array([[0], [1]])
# myObjective = simpleValleyObjective(p)
# x = np.array([[-1.01], [1]])
# d = np.array([[1], [1]])
# sigma = 1.0e-3
# rho = 1.0e-2
# t = WolfePowellSearch(myObjective, x, d, sigma, rho, 1)
# should return t=1

# p = np.array([[0], [1]])
# myObjective = simpleValleyObjective(p)
# x = np.array([[-1.2], [1]])
# d = np.array([[0.1], [1]])
# sigma = 1.0e-3
# rho = 1.0e-2
# t = WolfePowellSearch(myObjective, x, d, sigma, rho, 1)
# should return t=16

# p = np.array([[0], [1]])
# myObjective = simpleValleyObjective(p)
# x = np.array([[-0.2], [1]])
# d = np.array([[1], [1]])
# sigma = 1.0e-3
# rho = 1.0e-2
# t = WolfePowellSearch(myObjective, x, d, sigma, rho, 1)
# should return t=0.25

import numpy as np


def WolfePowellSearch(f, x: np.array, d: np.array, sigma=1.0e-3, rho=1.0e-2, verbose=0):
    fx = f.objective(x)
    gradx = f.gradient(x)
    descent = gradx.T @ d

    if descent >= 0:
        raise TypeError('descent direction check failed!')

    if sigma <= 0 or sigma >= 0.5:
        raise TypeError('range of sigma is wrong!')

    if rho <= sigma or rho >= 1:
        raise TypeError('range of rho is wrong!')

    if verbose:
        print('Start WolfePowellSearch...')

    def WP1(ft, s):
        isWP1 = ft <= fx + s*sigma*descent
        return isWP1

    def WP2(gradft: np.array):
        isWP2 = gradft.T @ d >= rho*descent
        return isWP2

    t = 1
    # INCOMPLETE CODE STARTS

    def w1(t): # function to check Wolfe condition 1
        return f.objective(x + t * d) <= fx + t * sigma * descent # check Wolfe condition 1
    def w2(t): # function to check Wolfe condition 2
        return f.gradient(x + t * d).T @ d >= rho * descent # check Wolfe condition 2
    
    if not w1(t): # if Wolfe condition 1 is not satisfied backtracking
        t = 0.5 * t # reduce step size
        while not w1(t): # while Wolfe condition 1 is still not satisfied
            t = 0.5 * t # again reduce step size 
        t_ = t # store t minus as new step size
        tp = 2 * t  # set t plus as double of t
    
    elif w2(t): # if Wolfe condition 2 is satisfied 
        return t # return t as step size

    else: # if Wolfe condition 1 is satisfied and Wolfe condition 2 is not satisfied fronttracking
        t = 2 * t # increase step size
        while w1(t): # while Wolfe condition 1 is satisfied
            t = 2 * t # increase step size
        t_ = t * 0.5 # store t minus as new step size 
        tp = t # set t plus as t

    t = t_ # set t as t minus

    while not w2(t): # while Wolfe condition 2 is not satisfied
        t = 0.5 * (t_ + tp) # set t as average of t minus and t plus
        if w1(t): # if Wolfe condition 1 is satisfied
            t_ = t # set t minus as t
        else: # if Wolfe condition 1 is not satisfied
            tp = t # set t plus as t

    # INCOMPLETE CODE ENDS

    if verbose:
        xt = x + t * d
        fxt = f.objective(xt)
        gradxt = f.gradient(xt)
        print('WolfePowellSearch terminated with t=', t)
        print('Wolfe-Powell: ', fxt, '<=', fx+t*sigma*descent, ' and ', gradxt.T @ d, '>=', rho*descent)

    return t
