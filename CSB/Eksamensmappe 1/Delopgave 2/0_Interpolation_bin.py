#####################################
####   Lagrange Interpolation    ####
##################################### 

from math import sin

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

# Printer resultatet
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)

Start = 10 
Stop = 300 
Step = 10

for N in range(Start,Stop,Step): 
    
    h = abs(b-a)/N                                              # Skridtlængde
    x_values = [a+k*h for k in range(N+1)]                      # Startværdi +1 
   
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
