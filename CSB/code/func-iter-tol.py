import math

def iter(f, xinit, tol):
	xold = 0
	xnew = 1
	xtemp = xinit
	n = 0

	while abs(xold - xnew) > tol:
		n += 1
		xold = xtemp
		xnew = f(xold)
		xtemp = xnew

	return xnew, n

def fun7(x):
    return (x+15)/(math.cosh(75/x))

def fun8(x):
    return x*math.cosh(75/x)-15

tol = 1E-12
xinit = 100

nul, it = iter(fun8, xinit, tol)

print(f"Nulpunkt fundet ved x = {nul:0.7E} efter {it} iterationer.")
