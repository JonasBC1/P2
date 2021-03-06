# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:35:28 2020

@author: rasmu
"""

# Adaptiv Simpson. Naiv implementation der ikke bekymrer sig om genbrug af 
# funktionsevalueringer.

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# implementation af S_{2N} fra kursusgang 7
def simpsonrule(f,a,b,N):
    h = (b - a)/N # bemærk: Dette er dobbelt afstanden mellem kvadraturpunkterne
    xL = a - h
    xR = a
    I = 0
    for k in range(N):
        xL = xL + h
        xR = xR + h
        I = I + h*(f(xL)+4.0*f((xL+xR)/2.0)+f(xR))/6.0 # Bemærk: Division med 6, da vi bruger h
    return I

# global variabel til at gemme kvadraturpunkter, bruges KUN til plot
quadpoints = []; 
  
def adaptivestep(f,xL,xR,tol):
    S2 = simpsonrule(f,xL,xR,1)
    S4 = simpsonrule(f,xL,xR,2)
    xM = (xL+xR)/2
    quadpoints.append(xM) # bruges kun til plot
    if abs(S4-S2) <= 15*tol: # bemærk at faktoren 15 er specifik for Simpons regel
        quadpoints.append((xL+xM)/2) # bruges kun til plot
        quadpoints.append((xM+xR)/2) # bruges kun til plot
        return S4 # denne approksimation har fejl ca. tol/(2^k) på delintervallet
    else:
        return adaptivestep(f,xL,xM,tol/2) + adaptivestep(f,xM,xR,tol/2)

def adaptivesimpson(f,a,b,tol):
    quadpoints.append(a) # bruges kun til plot
    quadpoints.append(b) # bruges kun til plot
    return adaptivestep(f,a,b,tol)

def fun(x):
    if x>sqrt(2): 
        return (x-sqrt(2))**2
    else: 
        return -(x-sqrt(2))**2

a = 0
b = 1.5

Iexact = (-(sqrt(2)-sqrt(2))**3/3) -(-(sqrt(0)-sqrt(2))**3/3)+((b-sqrt(2))**3/3-(sqrt(2)-sqrt(2))**3/3)
#interval_1=(-(sqrt(2)-sqrt(2))**3/3) -(-(sqrt(0)-sqrt(2))**3/3)+((b-sqrt(2))**3/3-(sqrt(2)-sqrt(2))**3/3)
#inteval_2= (b-sqrt(2))**3/3-(a-sqrt(2))**3/3 
#helefunk=15-((31*sqrt(2))/3)
    
# a = 1.5
# b = 3.0 
# Pas på med for lav tolerance: Der er ikke sat et maksimum på antallet af 
# inddelinger, så ved meget lav tolerance kan afrundingsfejl gøre at den 
# rekursive inddeling ikke kan opnå tolerancen. 
tol = 1e-5 

J = adaptivesimpson(fun, a, b, tol)
print(J)
print('Fejl: ',abs(Iexact-J))
print('Antal indelinger: ', len(quadpoints)-1)

# plot af kvadraturpunkter
quadpoints = np.sort(np.array(quadpoints));
x = np.linspace(a,b,500)

plt.figure()
plt.plot([a,b],[0,0],'k--')
plt.plot(x,fun(x),'b-')
plt.plot(quadpoints,fun(quadpoints),'r.')
plt.xlim([a,b])
plt.title('Adaptiv Simpson regel for $f(x) = x, sin(x^2)$')
plt.show()

# Ved tolerance på 1e-4, giver øvre grænse på 13500 af fjerde afledede at der 
# skal bruges S_166, frem for 112 inddelinger med adaptiv metode. En besparelse 
# på 32,5%. 
# Bemærk at den fjerde afledede tager meget store værdier i en lille del af 
# intervallet.
#plt.figure()
# abs af fjerde afledede:
#plt.plot(x,np.abs(-60*fun(x) - 80*(x**3)*np.cos(x**2) + 16*(x**4)*fun(x)),'b-') 
#plt.xlim([a,b])
#plt.ylim([0,13500])
#plt.title('Plot af $|f^{(4)}|$')
#plt.show()