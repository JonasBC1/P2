from math import sin,cos,pi
import matplotlib.pyplot as plt
import numpy as np

def lagrange(x, x_values, y_values):  
    
    from functools import reduce 
    def l(k,x): 
        temp = [(x-x_values[j])/(x_values[k]-x_values[j])\
              for j in range(len(x_values)) if j != k] 
        
        result = reduce(lambda x, y: x*y, temp) 
        return result
        
    
    p = []
    for i in range(len(x)):
        temp = [y_values[k]*l(k,x[i]) for k in range(len(x_values))]
        p.append(sum(temp))
    return p

a = 0
b = 3

def f(x): 
    return x**2-sin(10*x)


def equi_bound(h, N):
    M = 10**(N+1) 
    return 0.25*h**(N+1)*M 

print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)
for N in range(10,300,10):
    
  
    h = abs(b-a)/N   
    x_values = [3*(1-cos((k*pi)/N))/2 for k in range(N+1)] 
    y_values = [f(x_values[k]) for k in range(N+1)] 
    
    
    N_test = 781
    h_test = abs(b-a)/N_test
    x_test = [a+k*h_test for k in range(N_test+1)] 
     
    
    approx = lagrange(x_test, x_values, y_values)
    y_test = [f(x_test[k]) for k in range(N_test+1)]
    
    
    from operator import sub
    temp1 = list(map(sub, y_test, approx)) 
    temp2 = list(map(abs, temp1))  
    error = max(temp2)   
    
    
    print('{:3d}  {:14.5E}  {:13.5E}'.format(N, equi_bound(h,N), error))


def plot_vent():
    plt.plot(x_test,approx, label='aproksimation')
    plt.plot(x_test,y_test, label='funktion') 
    plt.plot(x_test,temp2, label='fejl')   
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plotning')
    plt.legend()
    plt.savefig('ventetid_år.png',bbox_inches='tight')
    plt.show()
plot_vent()