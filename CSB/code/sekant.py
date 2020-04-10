# -*- coding: utf-8 -*-

# Denne er lavet om til sekant metoden

import math

def iter(f,df,xinit,tol):
	xold = xinit + 1.0 #Denne værdi er sat til at starte med til 1 større end xnew
	xnew = xinit
	k = 0 # Den som tæller interations 
	while abs(xnew - xold) > tol: 
		k = k+1 # Tæller op 
		xold = xnew #Sætter vores x gamel til at være lige den nye 
		xnew = xold - f(xold) / df(xold) # Finder xnew til at tage xold 
	return xnew, k # Returnerer xnew og tælleværdien 
		

#Originale funktioner	
#def fun1(x):
#	return x**2-10.0
	
#def dfun1(x):
#	return 2.0*x

#Originalt    
#sol, n = iter(fun1, dfun1, 1, 1E-9)

    
###############################################################################   
 
    # Resten laves i dokument sektant
        
###############################################################################   
    
def fun1(x):
	return 4*x**3-x**2-12*x+3
	
def dfun1(x):
	return 4*3*x**2-2*x-12

sol, n = iter(fun1, dfun1, 0, 1E-9)

	
print('Approximation is %8.7E' % sol)

print('Number of interations used is %d' % n)
