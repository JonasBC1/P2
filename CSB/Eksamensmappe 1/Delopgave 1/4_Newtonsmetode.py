############################
####   Newtonsmetode    ####
############################

import math

def newton(f,df,xinit,tol):                # Funktion 
	xold = xinit + 1.0                     # Startværdi 
                                           # +1 for vi ikke starter under tollerencen
	xnew = xinit                           # Næste værdi 
	k = 0                                  # Tæller op 
	while abs(xnew - xold) > tol:          # Numerisk værdi 
		k = k+1                            # Tæller iterationer 
		xold = xnew                        # Sætter x0 til x1
		xnew = xold - f(xold) / df(xold)   # Sætter x1 til den nye værdi 
	return xnew, k                         # Returnere
		
def fun1(x):                               # Eksakt funktion 
	return x*math.cosh(75/x) - x - 15
	
def dfun1(x):                              # Eksakt f'
	return math.cosh(75/x)-75/x*math.sinh(75/x) - 1
	
sol, n = newton(fun1, dfun1, 100, 1E-12)     # Udregner den færdige 

print('Approximation is %8.7E' % sol)

print('Number of interations used is %d' % n)
