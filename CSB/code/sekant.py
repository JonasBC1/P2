import math

def secant(f,x0,x1,tol): 
    count = 0  
    while abs(x0 - x1) > tol:  
        x_temp = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0)) 
        x0 = x1 
        x1 = x_temp 
        count += 1 
    return x1, count  

def fun_test(x):
    return x*math.cosh(75/x) - x - 15

x0 = 90
x1 = 110
tol = 1E-12

s,count = secant(fun_test, x0, x1, tol)

print ('x0 = %g and x1 = %g' % (x0,x1))
print ('A zero is located at: %19.7E' % s)
print ('Number of interations used: %d' % count)