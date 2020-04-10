import numpy as np

def secant(f,x0,x1,eps): 
    count = 0  
    while abs(x0 - x1) > eps:  
        x_temp = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0)) 
        x0 = x1 
        x1 = x_temp 
        count += 1 
    return x1, count  

def fun_test(x):
    return np.exp(x) - 5*x+2

x0 = 2
x1 = 3
eps = 1E-12

s,count = secant(fun_test, x0, x1, eps)

print ('x0 = %g and x1 = %g' % (x0,x1))
print ('A zero is located at: %19.7E' % s)
print ('Number of interations used: %d' % count)

import matplotlib.pyplot as plt 
x = np.linspace(2,3,100,endpoint=True)
plt.plot(x, fun_test(x))
plt.grid(axis = 'both')
plt.title('$e^x-5x+2$')
plt.xlabel('x')
plt.ylabel('y')