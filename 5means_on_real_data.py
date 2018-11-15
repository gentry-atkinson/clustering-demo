#!/usr/bin/env python

from pypr.clustering.kmeans import *
import json
import matplotlib.pyplot as plot
import numpy

inFile = open("real_data.json")

line = inFile.readline()
item = json.loads(line)

X = numpy.array([float(item["X"]), float(item["Y"])])


try:
    while (inFile):
        line = inFile.readline()
        item = json.loads(line)
        item_array = numpy.array([float(item["X"]), float(item["Y"])])
        X = numpy.vstack((X, item_array))
except:
    print ("Bad value in file")

m, cc = kmeans(X, 5)

plot.scatter(X[m==0, 0], X[m==0, 1], 10, 'red')
plot.scatter(X[m==1, 0], X[m==1, 1], 10, 'blue')
plot.scatter(X[m==2, 0], X[m==2, 1], 10, 'white')
plot.scatter(X[m==3, 0], X[m==3, 1], 10, 'yellow')
plot.scatter(X[m==4, 0], X[m==4, 1], 10, 'black')

plot.title("5-Means on Set 1")

plot.show()