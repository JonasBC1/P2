#########################################
####    Adaptiv Simpsonssregel  4D   ####
#########################################

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def simpsonrule(f,a,b,N):           # Funktion f, interval a,b og indelinger N
    h = (b - a)/N                   # Bemærk: Dobbelt afstanden
    xL = a - h                      # De to punkter x_{j-1}  *Minus h fordi løkken starter med at lægge h til
    xR = a                          # og x_j
    I = 0
    for k in range(N):
        xL = xL + h                 # Første punkt bliver a til a+h
        xR = xR + h
        I = I + h*(f(xL)+4.0*f((xL+xR)/2.0)+f(xR))/6.0  # Simpsons
        # Bemærk: Division med 6, da vi bruger h
        # Vigtig! Rigtige h 
    return I

quadpoints = [];                    # Global variable - Gem kvadraturpunkter

def adaptivestep(f,xL,xR,tol):
    S2 = simpsonrule(f,xL,xR,1)         # N = 1 
    S4 = simpsonrule(f,xL,xR,2)         # N = 2
    xM = (xL+xR)/2
    quadpoints.append(xM)               # Tilføj
    if abs(S4-S2) <= 15*tol:            # bemærk at faktoren 15 er specifik for Simpons regel
        quadpoints.append((xL+xM)/2)    # Tilføj
        quadpoints.append((xM+xR)/2)    # Tilføj
        return S4                       # Fejl ca. tol/(2^k) på delintervallet
    else:                               # Ellers deles intervallet op
        return adaptivestep(f,xL,xM,tol/2) + adaptivestep(f,xM,xR,tol/2)

def fun(x):                             # Funktion
    if x>sqrt(2): 
        return (x-sqrt(2))**2
    else: 
        return -(x-sqrt(2))**2

# Begyndelsesbetingelser     
a = 0
b = 1.5 

############################
####    Intervallet     ####
############################

Iexact = (-(sqrt(2)-sqrt(2))**3/3) -(-(sqrt(0)-sqrt(2))**3/3)+((b-sqrt(2))**3/3-(sqrt(2)-sqrt(2))**3/3)
#interval_1=(-(sqrt(2)-sqrt(2))**3/3) -(-(sqrt(0)-sqrt(2))**3/3)+((b-sqrt(2))**3/3-(sqrt(2)-sqrt(2))**3/3)
#inteval_2= (b-sqrt(2))**3/3-(a-sqrt(2))**3/3 
#helefunk=15-((31*sqrt(2))/3)
    
tol = 1e-5 

J = adaptivestep(fun, a, b, tol)
print(J)
print('Fejl: ',abs(Iexact-J))
print('Antal indelinger: ', len(quadpoints)-1)