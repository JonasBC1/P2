# cobweb1.py:
#	Illustration of the iteration method
#   for solving x=cos(x)

# Modified version of script from 
# http://csc.ucdavis.edu/~chaos/courses/nlp/

# Import modules
import numpy as np
# Plotting
import pylab as py


# Define function to iterate (frastødende påpunkt)
#def g(x):
#	return (x+15)/(np.cosh(75/x))

# anden funktion som kan konveteres ind (tiltrækkende påpunkt)
def g(x):
	return x*np.cosh(75/x)-15
    

# Setup x array
# Make sure we have the endpoint x = 1.0

# Define interval (a,b) for iteration and mesh


a = 150
b = 250

x = np.linspace(a, b, abs(b-a)*100, endpoint=True)


# We set the initial value

x_init = 160




# Setup the plot
# It's numbered 1 and is 6 x 6 inches, to make the plot square.
py.figure(1,(6,6))


py.xlabel('x')   # set x-axis label
py.ylabel('y') # set y-axis label

# We plot the identity y = x for reference
py.plot(x, x, 'b--', antialiased=True)

# Plot y=g(x) 
py.plot(x, g(x), 'g', antialiased=True)


# Set the initial condition
state = x_init

# Establish the arrays to hold the line end points
x = [ ] # The x_n value
y = [ ] # The next value x_n+1
# Iterate for a few time steps
nIterates = 10
# nIterates = 40
# Plot lines, showing how the iteration is reflected off of the identity
for n in range(nIterates):
	x.append( state )
	y.append( state )
	x.append( state )
	state = g( state )
	y.append( state )

# Plot the lines all at once. Also plot the starting value 
# as a black dot.
py.plot(x, y, 'r', x_init, x_init, '.k', antialiased=True)

# Display plot in window
py.show()

