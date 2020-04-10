# Sekantmetoden 
import numpy as np

def secant(f,x0,x1,eps): # Funktionen 
    count = 0  # Tæller op 
    while abs(x0 - x1) > eps: # Numerisk værdi 
        x_temp = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0)) # Approksimerede løsning
        x0 = x1 # Sætter x0 til x1 
        x1 = x_temp # Sætter x1 til den nye værdi 
        count += 1 # Tæller op for ntallet af iterationer 
    return x1, count # Returnere 

def fun_test(x):
    return np.exp(x) - 5*x+2

x0 = 2
x1 = 3
eps = 1E-12

s,count = secant(fun_test, x0, x1, eps)

print ('x0 = %g and x1 = %g' % (x0,x1))
print ('A zero is located at: %19.7E' % s)
print ('Number of interations used: %d' % count)

# plot
import matplotlib.pyplot as plt 
x = np.linspace(2,3,100,endpoint=True)
plt.plot(x, fun_test(x))
plt.grid(axis = 'both')
plt.title('$e^x-5x+2$')
plt.xlabel('x')
plt.ylabel('y')
