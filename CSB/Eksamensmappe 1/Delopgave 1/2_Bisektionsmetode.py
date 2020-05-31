################################
####   Bisektionsmetoden    ####
################################

import math

def fun1(x):                                    # Eksakt funktion
    return x*(math.cosh(75/x)) - x - 15
    
def bisect(f, a, b, eps):                       # Funktionen 
    if f(a) * f(b) > 0:                         # Sikre gode betingelser
        print('Two endpoints have same sign')

    if f(a)*f(b)<=0:
        nit =   0                               # Tæller op 

        while b-a>=eps:
            nit +=  1                           # Tæller iterationer 
            m=(b+a)/2.0

            if f(a)*f(m)<=0:                    # Nulpunkt imellem a og m
                b=m                             # Sæt 
            else:
                a=m
                
        return (a + b)/2.0, nit                 # Returnere 

# Begyndelseskriterier
x=100
y=200
tol = 1E-12

myeps=tol * 2

res, nit = bisect(fun1,x,y,myeps)               # Udregner den færdige 

print('A zero is located at %8.7E' % res)
print(f"Antal iterationer {nit:0}")