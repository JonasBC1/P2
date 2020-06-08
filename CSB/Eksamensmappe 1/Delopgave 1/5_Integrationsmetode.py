##################################
####   Integrationssmetode    ####
##################################

import math

def iter(f, xinit, tol):                # Funktionen 
	xold = 0                            # Startværdi
	xnew = 1                            # Næste værdi 
	xtemp = xinit                       # Startværdi 
	n = 0                               # Tæller op 

	while abs(xold - xnew) > tol:       # Numerisk værdi 
		n += 1                          # Tæller iterationer 
		xold = xtemp                    # Sætter x0 til xtemp
		xnew = f(xold)                  # Sætter x1 til f(x0)
		xtemp = xnew                    # Sætter xtempt til x1 

	return xnew, n                      # Returnere 

def fun1(x):                            # Eksakt funktion
    return (x+15)/(math.cosh(75/x))

def fun2(x):                            # Eksakt funktion
    return x*math.cosh(75/x)-15

tol = 1E-12
xinit = 100
	
nul, it = iter(fun2, xinit, tol)        # Udregner den færdige 

print(f"Nulpunkt fundet ved x = {nul:0.7E} efter {it} iterationer.")
