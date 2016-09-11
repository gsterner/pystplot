import csv
import pystplot as pl

'''
Larger amounts of data can also be displayed
'''
with open('time_series_data.csv', 'rb') as f:
    reader = csv.reader(f)
    all_rows = [row for row in reader]

y_data =  [float(row[1]) for row in all_rows]
x_vals = range(len(y_data))

pl.plot(x_vals, y_data)
pl.show()
