# -*- coding: utf-8 -*-

# Newton's method

import math

def iter(f,df,xinit,tol):
	xold = xinit + 1.0
	xnew = xinit
	k = 0
	while abs(xnew - xold) > tol:
		k = k+1
		xold = xnew
		xnew = xold - f(xold) / df(xold)
	return xnew, k
		
	
def fun1(x):
	return x**2-10.0
	
def dfun1(x):
	return 2.0*x
	

	
sol, n = iter(fun1, dfun1, 1, 1E-9)


	
print('Approximation is %8.7E' % sol)

print('Number of interations used is %d' % n)
