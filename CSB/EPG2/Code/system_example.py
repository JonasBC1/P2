# solving an autonomous syste of ODEs using the R4 method.
# linear system example
import numpy as np
import matplotlib.pyplot as plt

def RK4(f, t_start, x0, t_stop, n):
    h = (t_stop - t_start)/n
    t = [t_start]
    x = [x0]
    tn = t_start
    xn = x0

    for k in range(n):
        k1 = f(tn,xn)
        k2 = f(tn + h/2,xn + h*k1/2)
        k3 = f(tn + h/2,xn + h*k2/2)
        k4 = f(tn + h,xn + h*k3)
        tn = tn + h
        xn = xn + h*(k1 + 2*(k2 + k3) + k4)/6
        t.append(tn)
        x.append(xn)

    return np.array(t), np.array(x)
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