import pystplot as pl

'''
To plot a function, simply assign x and y values two two lists and call pystplot.plot().
The pystplot.show() function needs to be called to create an output file and show it in the browser.
'''
x_values = range(-10,11)
y_values = [x*x for x in x_values]
pl.plot(x_values, y_values)

pl.show()
