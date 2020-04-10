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
	return 4*x**3-x**2-12*x+3
	
def dfun1(x):
	return 4*3*x**2-2*x-12

sol, n = iter(fun1, dfun1, 0, 1E-9)

	
print('Approximation is %8.7E' % sol)

print('Number of interations used is %d' % n)
