#############################
####    Cobweb Diagram   ####
#############################

# Solving x=cos(x)

import numpy as np
import pylab as py

# 1. Isolering
def g(x):                          # Funktion                    
	return (x+15)/(np.cosh(75/x))  # Frastødende punkt 

# 2. Isolering
#def g(x):
#	return x*np.cosh(75/x)-15      # Tiltrækkende punkt 
    
# Begyndelsesbetingelser 
a = 150
b = 250

x = np.linspace(a, b, abs(b-a)*100, endpoint=True)  # Ligeligt fordelte punkter 

x_init = 160                       # Eksakte værdi 


py.figure(1,(6,6))      # Nummeret 1, 6x6 = Kvadratisk plot
py.xlabel('x')          # x-axis label
py.ylabel('y')          # y-axis label

py.plot(x, x, 'b--', antialiased=True)  # Plot y = x


py.plot(x, g(x), 'g', antialiased=True) # Plot y=g(x) 

state = x_init                          # Optimale betingelser 

# Arrays
x = [ ]                                 # x_n
y = [ ]                                 # x_n+1

nIterates = 5                           # Skriftlængde
# nIterates = 40

for n in range(nIterates):    # Plot
	x.append( state )         # 
	y.append( state )         # x0, x1 punkt 
	x.append( state )         # 
	state = g(state)          # 
	y.append( state )         # x0, x1 punkt

py.plot(x, y, 'r', x_init, x_init, '.k', antialiased=True) # Plotter alle linjerne 

py.show()