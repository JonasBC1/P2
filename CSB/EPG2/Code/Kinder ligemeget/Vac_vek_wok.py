# Solving an autonomous system of ODEs using the RK4 method

import numpy as np
import matplotlib.pyplot as plt

def euler(f, t_start, x0, t_stop, n):
    h = (t_stop - t_start)/n
    t = [t_start]
    x = [x0]
    tn = t_start
    xn = x0

    for k in range(n):
        tn = tn + h
        xn = xn + h*f(tn,xn)
        t.append(tn)
        x.append(xn)
        
    return np.array(t), np.array(x)

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

# Time parameters
t_start = 0.0
t_stop  = 20.0
n       = 300

# Model parameters
alpha   = 0.01
beta    = 0.35
gamma   = 0.00
x10     = 85
x20     = 5
N       = 100

# Uden vaccine (Opg 2.3(a)) Ignorer gamme variablen
def f(t, x):
    return np.array([-alpha*x[0]*x[1],
                     alpha*x[0]*x[1] - beta*x[1]])


# Med vaccine (Opg 2.3(c)) 
# def f(t, x):
#    return np.array([-alpha*x[0]*x[1] - gamma*x[0],
#                     alpha*x[0]*x[1] - beta*x[1]])


# Numerical solution by RK4
tr, xr = RK4(f, t_start, np.array([x10, x20]), t_stop, n)

xr1 = xr[:,0]
xr2 = xr[:,1]
xr3 = N - xr1 - xr2

# Numerical solution by Euler
te, xe = euler(f, t_start, np.array([x10, x20]), t_stop, n)

xe1 = xe[:,0]
xe2 = xe[:,1]
xe3 = N - xe1 - xe2

# RK4 Plots
plt.figure()
plt.plot(xr1, xr2, 'r-', [x10], [x20], 'k.')
plt.xlabel('Susceptible')
plt.ylabel('Infected')
plt.title(f'Alpha = {alpha:0.2f}, Beta = {beta:0.2f}, Gamma = {gamma:0.2f}')
plt.show()

plt.figure()
plt.plot(tr, xr1, 'r-', tr, xr2, 'k-', tr, xr3, 'b-')
plt.xlabel('Time')
plt.ylabel('No. of cases')
plt.legend(['Susceptible', 'Infected', 'Recovered'])
plt.title(f'Alpha = {alpha:0.2f}, Beta = {beta:0.2f}, Gamma = {gamma:0.2f}')
plt.show()

# Euler Plots
# plt.figure()
# plt.plot(xe1, xe2, 'r-', [x10], [x20], 'k.')
# plt.xlabel('Susceptible')
# plt.ylabel('Infected')
# plt.title('Smittede og kan smittes Euler')
# plt.show()

# plt.figure()
# plt.plot(te, xe1, 'r-', te, xe2, 'k-', te, xe3, 'b-')
# plt.xlabel('Time')
# plt.ylabel('No. of cases')
# plt.legend(['Susceptible', 'Infected', 'Recovered'])
# plt.title('Kan smittes, smittede og immune Euler')
# plt.show()