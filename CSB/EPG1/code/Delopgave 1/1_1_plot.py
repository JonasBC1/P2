import matplotlib.pyplot as plt
import numpy as np
import math

#variabler
h0 = 10
T = 1
p = 1
Lamda = T/p
l = 10
# cosh funktionen
def cosh(x):
    return(0.5*(math.exp(x)+math.exp(-x)))
   
#lav et array med værdier mellem de 2 værdier og med 3 gange så mange punkter som længden
x = np.array(np.linspace(-l/2,l/2,l*3))

#udregner tilsvarende y værdier
y = []
for k in x:
    y_h = h0 + Lamda*cosh(k/Lamda)
    y.append(y_h)
np.asarray(y)

#plotter funktionen
plt.plot(x,y)
#gemmer plottet
#plt.savefig('fig4.pdf')
#viser plottet
plt.show()
