# solving an autonomous syste of ODEs using the R4 method.
# linear system example
import numpy as np
import matplotlib.pyplot as plt
from RK4 import *

# time parameters
t_start = 0.0
t_stop = 10.0
N = 500
t_step = (t_stop - t_start)/N

# parameter value
a, b, c, d = -1.0, 4.0, -2.0, -1.0 # asymptotically stable equilibrium
# starting point
x10 = 13.5
x20 = -11.1

# parameter value
#a, b, c, d = 1.0, 4.0, -2.0, 1.0 # unstable equilibrium
# starting point
#x10 = 0.05
#x20 = -0.05

# rhs of system
A = np.array([[a,b],
              [c,d]])
def f(t,x):
    return A.dot(x)

# Numerical solution by RK4
t, x = RK4(f, t_start, np.array([x10, x20]), t_stop, N)

x1 = x[:,0] 
x2 = x[:,1]
    
plt.figure()
plt.plot(x1, x2, 'r-', [x10], [x20], 'k.')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.show()