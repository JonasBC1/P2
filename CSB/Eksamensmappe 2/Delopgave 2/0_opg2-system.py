######################
####     RK4      ####
######################

import numpy as np
import matplotlib.pyplot as plt

def RK4(f, t_start, x0, t_stop, n):
    h = (t_stop - t_start)/n
    t = [t_start]; x = [x0]
    tn = t_start; xn = x0
    for k in range(n):
        k1 = f(tn,xn)
        k2 = f(tn + h/2,xn + h*k1/2)
        k3 = f(tn + h/2,xn + h*k2/2)
        k4 = f(tn + h,xn + h*k3)
        tn = tn + h
        xn = xn + h*(k1 + 2*(k2 + k3) + k4)/6
        t.append(tn); x.append(xn);
    return np.array(t), np.array(x)

# Time parameters
t_start = 0.0
t_stop  = 20.0
n       = 300

# Model parameters
alpha   = 0.01
beta    = 0.35
x10     = 90
x20     = 5
N       = 100

# The rhs of the system 
def f(t, x):
    return np.array([-alpha*x[0]*x[1],
                     -beta*x[1] + alpha*x[0]*x[1]])

# Numerical solution by RK4
t, x = RK4(f, t_start, np.array([x10, x20]), t_stop, n)

x1 = x[:,0]
x2 = x[:,1]
x3 = N - x1 - x2

# Plots
plt.figure()
plt.plot(x1, x2, 'r-', [x10], [x20], 'k.')
plt.xlabel('susceptible')
plt.ylabel('infected')
plt.show()

plt.figure()
plt.plot(t, x1, 'r-', t, x2, 'k-', t, x3, 'b-')
plt.xlabel('time')
plt.ylabel('no. of cases')
plt.legend(['susceptible', 'infected', 'recovered'])
plt.show()