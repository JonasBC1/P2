################################
####     Simpsonssregel     ####
################################

# Simpson (S_{2N}) sammensatte kvadraturregel (naiv implementation)

import numpy as np
from math import sqrt

def simpsonrule(f,a,b,N):           # Funktion f, interval a,b og indelinger N
    h = (b - a)/N                   # Bemærk: Dobbelt afstanden
    xL = a - h                      # De to punkter x_{j-1}  
    xR = a                          # og x_j
    I = 0
    for k in range(N):
        xL = xL + h                 # Første punkt bliver a til a+h
        xR = xR + h
        I = I + h*(f(xL)+4.0*f((xL+xR)/2.0)+f(xR))/6.0  # Simpsons
        # Bemærk: Division med 6, da vi bruger h
        # Vigtig! Rigtige h 
    return I


def fun(x):                         # Funktion
    if x>sqrt(2): 
        return (x-sqrt(2))**2
    else: 
        return -(x-sqrt(2))**2
    
Iexact = 15-((31*sqrt(2))/3)        # Eksakte værdi
    
iter_max = 15

L0 = [0.0 for i in range(iter_max)] # Liste med 15 "0"
L1 = [0.0 for i in range(iter_max)]
L2 = [0.0 for i in range(iter_max)]
L3 = [0.0 for i in range(iter_max)]

a = 0.0
b = 3.0

for k in range(iter_max):           # N blive fordoblet
    N = 2**(k+1)                    # Den fordobler
    L0[k] = N                       # Tilføjer N til listen
    J = simpsonrule(fun, a, b, N) 
    L1[k] = J                       # Appeksimation
    L2[k] = abs(J - Iexact)         # Fejlen
    if k>0:
        L3[k] = L2[k-1]/L2[k]       # Orden

L = zip(L0,L1,L2,L3)                # Lynlåsen - Samler den 


header_fmt='{0:^7} {1:^16} {2:^9} {3:^8}'
print(header_fmt.format('N', 'Approksimation', 'Fejl', 'Orden'))    # Printer oversigten
print(header_fmt.format('-'*7, '-'*16, '-'*9, '-'*8))               # Laver linjer 

for n, Z, fejl, ord in L:                                           # Printer listen
    print('{0:>7} {1:<11.10E} {2:4.3E} {3:4.3E}'.format(n, Z, fejl, ord))