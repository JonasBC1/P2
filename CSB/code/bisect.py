# -*- coding: utf-8 -*-

# zero finding using bisection method

import math

def fun1(x):
    return x*1/2*(math.exp(75/x) + math.exp(-75/x)) - x - 15
    
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

x=1
y=200
myeps=1E-12

res, nit = bisect(fun1,x,y,myeps)

tol = myeps/2.0

print('Finding zeroes in [%.2E, %.2E]' % (x, y))
print('A zero is located at %8.7E' % res)
print('Error is less than %.2E' % tol)
print(f"Antal iterationer {nit:0}")