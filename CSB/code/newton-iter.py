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
	return x*math.cosh(75/x) - x - 15
	
def dfun1(x):
	return math.cosh(75/x)-75/x*math.sinh(75/x) - 1
	
sol, n = iter(fun1, dfun1, 100, 1E-12)

print('Approximation is %8.7E' % sol)

print('Number of interations used is %d' % n)
