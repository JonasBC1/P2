#####################################
####   Lagrange Interpolation    ####
####       Decimal modulet       ####
##################################### 

import decimal
context = decimal.getcontext()  # Standard pakke 
digits = 80                     # Væsendtlige cifte 
context.prec = digits           
D = decimal.Decimal             # Decimal

def Dpi():                                  # Pi - Decimal computation
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    """
    
    decimal.getcontext().prec += 2          # Ekstra sifre til mellemregninger 
    three = D(3)                            # Et decimal "three" 
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s                               # Den nye præcision 


def Dsin(x):                                # Sin - Decimal computation
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)
    """
    
    decimal.getcontext().prec += 2
    x = x % (2 * Dpi())
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s

#####################################
####   Lagrange Interpolation    ####
#####################################
    
def lagrange(x, x_values, y_values):                         # Lagrange polynomier
    
    from functools import reduce                             # Samle udtrykket
    def l(k,x):                                              # Liste af x- og y-værdier   
        temp = [(x-x_values[j])/(x_values[k]-x_values[j])\
              for j in range(len(x_values)) if j != k]       # temp = ET legrange polynomie - Skifter k    
        # Reducere det sammen hvis nogle bliver gentaget 
        result = reduce(lambda x, y: x*y, temp)              # Ganger resultater fra listen i temp sammen
        return result
    

    p = []                      # Tom liste     
    for i in range(len(x)):
        temp = [y_values[k]*l(k,x[i]) for k in range(len(x_values))]
        p.append(sum(temp))     # Summere dem sammen
    
    return p

#####################
####    Fejl     ####
#####################
    
def equi_bound(h, N):
    M = D(10)**(N+1)            # Maks 
    return D(0.25)*h**(N+1)*M   # Teoretisk fejl


def f(x):                       # Funktionen 
    return x**2-Dsin(D(10)*x)

# Begyndelsesetinglser 
a = D(0)
b = D(3)

# Printer resultatet
print('-'*34)
print('      Lagrange interpolation ')
print('-'*34)
print('          Precision = ',digits) # Printer præcision
print('-'*34)
print('  N     Error bound       Error')
print('-'*34)

# Dårlig approksimation
#Start = 
#Stop = 
#Step = 

# God approksimation
Start = 10 
Stop = 91 
Step = 10

for N in range(Start,Stop,Step): 

    # Parameters for Lagrange interpolation
    h = abs(b-a)/D(N)                                   # Skridtlængde
    x_values = [a+k*h for k in range(N+1)]             
    y_values = [f(x_values[k]) for k in range(N+1)]     # y-værdier fra funktionen
   
    # max|f(x)-p_N(x)|
    N_test = 797 # 1297                                 # Værdien fra den oprindelige
    h_test = abs(b-a)/D(N_test)
    x_test = [a+k*h_test for k in range(N_test+1)]      # Original x_test
     
    # Approksimation
    approx = lagrange(x_test, x_values, y_values)
    y_test = [f(x_test[k]) for k in range(N_test+1)]
    
    # Fejlen
    from operator import sub, abs
    temp1 = list(map(sub, y_test, approx))              # Trække værdier i to lister fra hinanden
    temp2 = list(map(abs, temp1))                       # Absolut værdien 
    error = max(temp2)                                  # Største tal af absolutværdier 
    
    # Print a table
    print('{:3d}  {:14.5E}  {:13.5E}'.format(N, \
          equi_bound(h,N), error))                      # Printer oversigten