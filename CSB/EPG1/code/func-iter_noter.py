# -*- coding: utf-8 -*-

# fixed point method for zero finding


import numpy as np


def iter(f, xinit, N):
    L1 = [i for i in range(N+1)]
    L2 = [0.0 for i in range(N+1)]
    L2[0] = xinit
    for i in range(N):
        L2[i+1] = f(L2[i])
    return zip(L1, L2)
    

def fun8(x):
    return x*np.cosh(75/x)-15

def fun7(x):
    (x+15)/(np.cosh(75/x))
    
X = iter(fun8,100,1000)

print('Iteration       Værdi')

for i, fi in X:
    print('%5d      %5.8E' % (i, fi))
