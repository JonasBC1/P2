
import numpy as np

import pylab as py



def g(x):
	return (x+15)/(np.cosh(75/x))



a = 150
b = 250

x = np.linspace(a, b, abs(b-a)*100, endpoint=True)


x_init = 160




py.figure(1,(6,6))


py.xlabel('x')  
py.ylabel('y') 


py.plot(x, x, 'b--', antialiased=True)


py.plot(x, g(x), 'g', antialiased=True)



state = x_init


x0 = [ ] 
x1 = [ ] 

nIterates = 5


for n in range(nIterates):
	x0.append( state )
	x1.append( state )
	x0.append( state )
	state = g(state)
	x1.append( state )
py.plot(x0, x1, 'r', x_init, x_init, '.k', antialiased=True)


py.show()

