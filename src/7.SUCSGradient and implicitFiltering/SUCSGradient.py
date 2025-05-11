# Optimization for Engineers - Dr.Johannes Hild
# scaled unit central simplex gradient

# Purpose: Approximates gradient of f on a scaled unit central simplex

# Input Definition:
# f: objective class with methods .objective()
# x: column vector in R ** n(domain point)
# h: simplex edge length
# verbose: bool, if set to true, verbose information is displayed

# Output Definition:
# grad_f_h: simplex gradient
# stenFail: 0 by default, but 1 if stencil failure shows up

# Required files:
# < none >

# Test cases:
# myObjective = multidimensionalObjective()
# x = np.array([[1.02614],[0],[0],[0],[0],[0],[0],[0]], dtype=float)
# h = 1.0e-6
# myGradient = SUCSGradient(myObjective, x, h)
# should return
# myGradient close to [[0],[0],[0],[0],[0],[0],[0],[0]]


import numpy as np


def matrnr():
    # set your matriculation number here
    matrnr = 23339080
    return matrnr


def SUCSGradient(f, x: np.array, h: float, verbose=0):

    if verbose: # print information
        print('Start SUCSGradient...') # print start

    grad_f_h = x.copy() # initialize gradient vector

    # print('grad_f_h.shape =', grad_f_h.shape) 

    # INCOMPLETE CODE STARTS

    for i in range(x.shape[0]): # iterate over all dimensions of x
        ej = np.zeros(x.shape) # initialize unit vector
        ej[i,0] = 1 # set unit vector in i-th direction

        xjs = x + h * ej # set the the simplex 
        xjr = x - h * ej # set the reflected vertices 

        fjs = f.objective(xjs).item() # get function values at the simplex 
        fjr = f.objective(xjr).item() # get function values at the reflected vertices 

        grad_f_h[i] = (fjs - fjr) / (2 * h) # compute the gradient in j-th direction

    # INCOMPLETE CODE ENDS

    if verbose: # print information
        print('SUCSGradient terminated with gradient =', grad_f_h) # print termination

    return grad_f_h


def SUCSStencilFailure(f, x: np.array, h: float, verbose=0):

    if verbose: # print information
        print('Check for SUCSStencilFailure...') # print start of check

    stenFail = 1 # initialize stencil failure with true

    # INCOMPLETE CODE STARTS, DO NOT FORGET TO WRITE A COMMENT FOR EACH LINE YOU WRITE

    for i in range(x.shape[0]): # iterate over all dimensions of x
        ej = np.zeros(x.shape) # initialize unit vector
        ej[i] = 1 # set unit vector in j-th direction

        xjs = x + h * ej # set the the simplex
        xjr = x - h * ej # set the reflected vertices

        fjs = f.objective(xjs) # get function values at the simplex
        fjr = f.objective(xjr) # get function values at the reflected vertices

        if f.objective(x) > np.min([fjs, fjr]): # check if function value at x is less than the minimum of the simplex values
            stenFail = 0 # set stencil failure to false if the condition is satisfied
            break # break the loop if condition is satisfied

    # INCOMPLETE CODE ENDS
    
    if verbose: # print information
        print('SUCSStencilFailure check returns ', stenFail) # print termination

    return stenFail
