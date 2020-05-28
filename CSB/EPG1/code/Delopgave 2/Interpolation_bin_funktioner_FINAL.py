# 

from math import sin,cos,pi
import matplotlib.pyplot as plt
import numpy as np
# Interpolating polynomial
def lagrange(x, x_values, y_values):  #funktionen defineres
    
    from functools import reduce #func tools importeres for at samle udtrykket
    def l(k,x): #Lagrange polynomier konstrueres ud fra en liste af x- og y-værdier
        temp = [(x-x_values[j])/(x_values[k]-x_values[j])\
              for j in range(len(x_values)) if j != k] #se formel for l_polynomier laver liste over de enkelte udtryk
        
        result = reduce(lambda x, y: x*y, temp) #ganger resultater fra listen i temp sammen
        return result
        
    
    # Lagrange interpolation polynomial: kører forrige funktion og konstrue på baggrund lister for polynomier
    p = []
    for i in range(len(x)):
        temp = [y_values[k]*l(k,x[i]) for k in range(len(x_values))]
        p.append(sum(temp))
    return p

# Parameters for the experiment
a = 0
b = 3

def f(x): #funktionen der ønskes undersøgt
    return x**2-sin(10*x)

# Error bound for equidistant points for the function f(x)=x^2-sin(10x)
def equi_bound(h, N):
    M = 10**(N+1) #M er funktionens maks da sinus går mellem 0 og 1 og maks for funktion derfor bliver 10^(n+1)
    return 0.25*h**(N+1)*M #teoretisk fejl det fatter vi heller ikke

# Print the results
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)
for N in range(10,300,10):
    
    # Parameters for Lagrange interpolation
    h = abs(b-a)/N   #Steplings=længden mellem hver x 
    #x_values = [a+k*h for k in range(N+1)] #startværdi +et fortløbende*underindelinger(skabt af poly)
    x_values = [3*(1-cos((k*pi)/N))/2 for k in range(N+1)] #X_j-værdier for Chebyshevpunkter (opgave 8)
    y_values = [f(x_values[k]) for k in range(N+1)] #giver nogle y værdier fra funktionen
    
    # New points for calculating the error max|f(x)-p_N(x)|
    N_test = 781
    h_test = abs(b-a)/N_test
    x_test = [a+k*h_test for k in range(N_test+1)] #original x_test
     
    # Calculate the approximation and the solution
    approx = lagrange(x_test, x_values, y_values)
    y_test = [f(x_test[k]) for k in range(N_test+1)]
    
    # Calculate the error
    from operator import sub
    temp1 = list(map(sub, y_test, approx)) #bruger operator.sub til at trække værdier i to lister fra hinanden, syntaxen er dog max forvirrende med den måde han gør det
    temp2 = list(map(abs, temp1))  #tager absolut værdien her
    error = max(temp2)   #hiver det største tal fra listen af absolutværdier over fejl
    
    # Print a table der sker noget pudsigt med tabellen skal vi lige se om også sker når vi ellers kører eller jeg har lavet noget om
    print('{:3d}  {:14.5E}  {:13.5E}'.format(N, \
          equi_bound(h,N), error))

#funktioner til plots
#approx som funktion af x_text
def plot_vent():
    plt.plot(x_test,approx, label='aproksimation')
    plt.plot(x_test,y_test, label='funktion') #er det y_text(x_y) eller x_values(y_values)
    plt.plot(x_test,temp2, label='fejl')    #den er her hvis vi har lyst til at plotte fejl
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('mehh')
    #plt.axis([0,3,0,0.2])
    plt.legend()
    plt.savefig('ventetid_år.png',bbox_inches='tight')
    plt.show()
plot_vent()

