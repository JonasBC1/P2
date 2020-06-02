############################
####   Plot figur       ####
############################

import matplotlib.pyplot as plt
import numpy as np
import math

# Variabler
h0 = 10
T = 1
p = 1
L = T/p                 # Lampda
l = 10                  # Længde

def cosh(x):            # cosh funktionen
    return(0.5*(math.exp(x)+math.exp(-x)))
   
# Array med værdier mellem pæle og 3 gange så mange punkter som længden
x = np.array(np.linspace(int(-l/2),int((l/2)),l*3))

y = []

for k in x:                 # Tilsvarende y værdier
    y_h = h0 + L*cosh(k/L)
    y.append(y_h)           
np.asarray(y)               # Laver det om til et array 

plt.plot(x,y)               # Plotter funktionen

plt.show()                  # Viser plottet