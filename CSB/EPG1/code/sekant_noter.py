# Sekantmetoden 
import numpy as np

def secant(f,x0,x1,tol): # Funktionen 
    count = 0  # Tæller op 
    while abs(x0 - x1) > tol: # Numerisk værdi 
        x_temp = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0)) # Approksimerede løsning
        x0 = x1 # Sætter x0 til x1 
        x1 = x_temp # Sætter x1 til den nye værdi 
        count += 1 # Tæller op for ntallet af iterationer 
    return x1, count # Returnere 

def fun_test(x):
    return x*math.cosh(75/x) - x - 15

x0 = 10
x1 = 100
tol = 1E-12

s,count = secant(fun_test, x0, x1, tol)

print ('x0 = %g and x1 = %g' % (x0,x1))
print ('A zero is located at: %19.7E' % s)
print ('Number of interations used: %d' % count)

