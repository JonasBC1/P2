# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:36:23 2020

@author: Jonas
"""
import matplotlib.pyplot as plt
import numpy as np
import math

h0 = 10
T = 0.5
p = 0.5
L = T/p
l = 10
def cosh(x):
    return(0.5*(math.exp(x)+math.exp(-x)))
   
  
x = np.array(np.linspace(int(-l/2),int((l/2)),30))

y = []
for k in x:
    y_h = h0 + L*cosh(k/L)
    y.append(y_h)
np.asarray(y)


plt.plot(x,y)

plt.show()
