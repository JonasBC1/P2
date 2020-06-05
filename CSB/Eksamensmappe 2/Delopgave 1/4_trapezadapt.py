#####################################
####    Adaptiv Trapezsregel     ####
#####################################

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def trapezrule(f,a,b,N):                # Funktion f, interval a,b og indelinger N
    h = (b - a)/N                       # Skridtlængden
    xL = a - h                          # De to punkter x_{j-1}  *Minus h fordi løkken starter med at lægge h til
    xR = a                              # og x_j
    I = 0
    for k in range(N):
        xL = xL + h                     # Første punkt bliver a til a+h
        xR = xR + h
        I = I + h*(f(xL)+f(xR))/2.0     # Trapez
    return I

quadpoints = [];                    # Global variable - Gem kvadraturpunkter
  
def adaptivestep(f,xL,xR,tol):
    T2 = trapezrule(f,xL,xR,1)
    T4 = trapezrule(f,xL,xR,2)
    xM = (xL+xR)/2
    quadpoints.append(xM)               # Tilføj
    if abs(T4-T2) <= 3*tol:             # bemærk at faktoren 3 er specifik for Trapez regel
        quadpoints.append((xL+xM)/2)    # Tilføj
        quadpoints.append((xM+xR)/2)    # Tilføj
        return T4                       # Fejl ca. tol/(2^k) på delintervallet
    else:
        return adaptivestep(f,xL,xM,tol/2) + adaptivestep(f,xM,xR,tol/2)

def fun(x):                             # Funktion
    if x>sqrt(2): 
        return (x-sqrt(2))**2
    else: 
        return -(x-sqrt(2))**2
    
Iexact = 15-((31*sqrt(2))/3)            # Eksakte værdi

# interval_1 = (-(sqrt(2)-sqrt(2))**3/3) -(-(sqrt(0)-sqrt(2))**3/3)+((b-sqrt(2))**3/3-(sqrt(2)-sqrt(2))**3/3)
# interval_2 = (b-sqrt(2))**3/3-(a-sqrt(2))**3/3 
# helefunk   = 15-((31*sqrt(2))/3)

# Begyndelsesbetingelser  
a = 0.0
b = 3.0

tol = 1e-5 

J = adaptivestep(fun, a, b, tol)
print(J)
print('Fejl: ',abs(Iexact-J))
print('Antal indelinger: ', len(quadpoints)-1)