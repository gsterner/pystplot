import pystplot as pl
import math
import random

'''
Several lines of different types can be displayed in the same plot. The last argument of the plot function sets the display type. 'o' displays the data as filled dots.
'''
x_inds = range(-20,10)
x_vals = [xi/10.0 for xi in x_inds]

y_random = [x + random.randint(-10,10)/10.0 for x in x_vals]

pl.plot(x_vals, x_vals,'-r')
pl.plot(x_vals, y_random, 'o')

pl.show()
