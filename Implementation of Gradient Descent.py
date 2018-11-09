# ALGORITHM FOR IMPLEMENTMENTATION :

# Find local minima of the function y = (x+5)^2 starting from point x=3
​
​
# SOLUTION :
​
# its's minimum value when x = -5 when y = 0
# => x = -5 is the local & global minima of the function
​
# STEP : 1
    # Initialize x=3, find the Gradient of the function, dy/dx = 2*(x+5)
​
# STEP : 2
    # : Move in the direction of the negative of the gradient.
    #    how much to move? For that, we require a learning rate. Let us assume the learning rate → 0.01
​
# STEP : 3
    # how many iterations should we perform? 
    # Let us set a precision variable in our algorithm 
    # which calculates the difference between two consecutive “x” values
    # If the difference between x values from 2 consecutive iterations is lesser than the precision we set, stop the algorithm

# Function used : y = (x+5) ^2
# It's Derivative : (dy/dx) = 2*(x+5)

# ----- CODE BEGINS ---------

from matplotlib import pyplot as plt
import numpy as np
from IPython.display import HTML;import ipywidgets as widgets;from ipywidgets import Layout; from IPython.display import display
import os
from subprocess import call

# the local or global minima (the curren position)
cur_x = 3
​
# learning rate
lRate = 0.1
​
# threshold prediction value 
precision = 0.000001
​
# difference in two consecutive iterations
convergence = 1
​
# maximum number of iteration off algo
max_iters = 1000
​
# Gradient of our function
df = lambda x : 2*(x+5)
f_x = lambda x: (x + 5)**2
​
# Iteration counter
iters = 0

​
# Iterate untill (x2 - x1) > prediction & iterations < maximum set iterations  
n = 0
x = [cur_x]
y = [f_x(cur_x)]
​
while convergence > precision and iters < max_iters:
   
    # Store current x value
    prev_x = cur_x
    
    # Gradient
    cur_x = cur_x - lRate * df(prev_x)
    
    # convergence in 2 consecutive steps
    convergence = abs(cur_x - prev_x)
    
    # increment the counter
    iters+=1
    
    x.append(cur_x)
    y.append(f_x(cur_x))
    
    # print interation and convered value of 'x' :
    print("Interation : ", iters, "and Converged value of 'x' : ", cur_x)



# Plot Graph 

plt.figure()
for n in range(len(x)):
    plt.cla()
    plt.plot(x,y)
    plt.scatter(x[0:n], y[0:n])

    plt.xlim(-6,5)
    plt.ylim(-10,70)
    plt.xticks(np.arange(min(x)-1, max(x)+2,1))
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title(" y = (x - 5)^2")
    plt.savefig('gif/Frame%03d.png' %n, transparent=True)


# Create GIF of graph

os.chdir("gif")
call(['mogrify', '-resize', '640x480', '*.png'])
call(['convert', '-delay', '0', '-loop', '0', '-alpha', 'set','-dispose', 'previous', '*.png', 'gradientDescent.gif'])
call(["ls","-i"])
os.chdir("..")