PyStPlot
========

A VERY simple plotting tool for python that creates plots to be viewed in the web broser.
Creates an html file containing the plot drawn with html canvas.

Install with pip
-----------------
```
pip install pystplot
```
Usage
------
To plot a function, simply assign x and y values to two lists and call pystplot.plot(...).
Call either the pystplot.show() to create an output file and show it in the browser or pystplot.save(...) to just save the html file.

Example
--------
```
import pystplot as pl

x_values = range(-10,11)
y_values = [x*x for x in x_values]
pl.plot(x_values, y_values)

pl.show()
```
Functions
----------
```
plot(...)
```
show()
```
save(...)
```
subplot(...)
```