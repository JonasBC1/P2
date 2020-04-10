# -*- coding: utf-8 -*-

# zero finding using bisection method

import math

def fun1(x):
    return 1 - x + math.sin(x)
    
def fun2(x):
    return 4*x**3 - x**2 -12*x + 3
    
def fun3(x):
    return math.exp(x)-0.7

    
    
def bisect(f, a, b, eps):
    if f(a) * f(b) > 0:
        print('Two endpoints have same sign')
        return
    if f(a)*f(b)<=0:
        nit =   0
        while b-a>=eps:
            nit +=  1
            m=(b+a)/2.0
            if f(a)*f(m)<=0:
                b=m
            else:
                a=m
        return (a + b)/2.0, nit

#Opgave 4. Nulpunkt ved (0;-1;-0.357) 27 iterationer (-100;100;35 it) E-12 48 it
x=-100
y=100
myeps=1E-12 
res, nit = bisect(fun3,x,y,myeps)

#Opgave 3 nulpunkt (1;2;1,732) 27 it, (-1;1;0,25) 28 it og (-2;-1;-1,732) 27 it
#x=1
#y=2
#myeps=1E-8
#res, nit = bisect(fun2,x,y,myeps)

#Opgave 2 (1;2;1.934) 27 it
#x=1
#y=2
#myeps=1E-8
#res, nit    =   bisect(fun1,x,y,myeps)

tol = myeps/2.0

print('Finding zeroes in [%.2E, %.2E]' % (x, y))
print('A zero is located at %8.7E' % res)
print('Error is less than %.2E' % tol)
print(f"Antal iterationer {nit:0}")