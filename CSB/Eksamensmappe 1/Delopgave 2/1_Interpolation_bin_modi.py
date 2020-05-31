#####################################
####   Lagrange Interpolation    ####
#####################################

from math import sin,cos,pi
import matplotlib.pyplot as plt
import numpy as np

def lagrange(x, x_values, y_values):                        # Lagrange polynomier
    
    from functools import reduce                            # Samle udtrykket
    def l(k,x):                                             # Liste af x- og y-værdier
        temp = [(x-x_values[j])/(x_values[k]-x_values[j])\
              for j in range(len(x_values)) if j != k]      # temp = ET legrange polynomie - Skifter k 
        
        # Reducere det sammen hvis nogle bliver gentaget 
        result = reduce(lambda x, y: x*y, temp)             # Ganger resultater fra listen i temp sammen
        return result 
        
    p = []                      # Tom liste 

    for i in range(len(x)):
        temp = [y_values[k]*l(k,x[i]) for k in range(len(x_values))]
        p.append(sum(temp))     # Summere dem sammen
    return p

# Begyndelsesbetingelser
a = 0
b = 3

def f(x):                       # Funktionen 
    return x**2-sin(10*x)

#####################
####    Fejl     ####
#####################
    
def equi_bound(h, N):
    M = 10**(N+1)           # Maks 
    return 0.25*h**(N+1)*M  # Teoretisk fejl

# Print the results
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)

# Dårlig approksimation
Start = 1
Stop = 13
Step = 1

# God approksimation
#Start = 10 
#Stop = 300 
#Step = 10

for N in range(Start,Stop,Step): # Start, stop, spring
    
    h = abs(b-a)/N   #Skridtlængde
    
    ############################################
    # Ændre Chebyshevpunkter eller almindelige #
    ############################################
    
    #x_values = [a+k*h for k in range(N+1)]                     # Startværdi +1 
    x_values = [3*(1-cos((k*pi)/N))/2 for k in range(N+1)]      # Chebyshevpunkter
   
    y_values = [f(x_values[k]) for k in range(N+1)]             # y-værdier fra funktionen
    
    # max|f(x)-p_N(x)|
    N_test = 781                                                # Værdien fra den oprindelige 
    h_test = abs(b-a)/N_test
    x_test = [a+k*h_test for k in range(N_test+1)]              # Original x_test
     
    # Approksimation 
    approx = lagrange(x_test, x_values, y_values)
    y_test = [f(x_test[k]) for k in range(N_test+1)]
    
    # Fejlen
    from operator import sub
    temp1 = list(map(sub, y_test, approx))  # Trække værdier i to lister fra hinanden
    temp2 = list(map(abs, temp1))           # Absolut værdien 
    error = max(temp2)                      # Største tal af absolutværdier 

    print('{:3d}  {:14.5E}  {:13.5E}'.format(N, \
          equi_bound(h,N), error))          # Printer oversigten

#####################
####    Plot     ####
#####################

def plot_vent():                                    # Til plot - approx som funktion af x_text
    plt.plot(x_test,approx, label='Aproksimation')
    plt.plot(x_test,y_test, label='Funktion') 
    plt.plot(x_test,temp2, label='Fejl')    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolationspolynomium')
    #plt.axis([0,3,0,0.2])
    plt.legend()
    plt.savefig('ventetid_år.png',bbox_inches='tight')
    plt.show()
plot_vent()

