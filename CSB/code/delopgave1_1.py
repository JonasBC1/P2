import matplotlib.pyplot as plt
import numpy as np
import math

h0 = 10
T = 1
p = 1
L = T/p
l = 10

def cosh(x):
    return(0.5*(math.exp(x)+math.exp(-x)))
   

x = np.array(np.linspace(int(-l/2),int((l/2)),l*3))


y = []
for k in x:
    y_h = h0 + L*cosh(k/L)
    y.append(y_h)
np.asarray(y)


plt.plot(x,y)

plt.show()
