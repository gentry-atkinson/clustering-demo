#!/usr/bin/env python3

import json
import matplotlib.pyplot as plot
xarray = list()
yarray = list()

inFile = open("real_data.json")
try:
    while (inFile):
        line = inFile.readline()
        item = json.loads(line)
        xarray.append(item["X"])
        yarray.append(item["Y"])
        #print ("X=", item["X"], " Y=", item["Y"])
except:
    print ("bad value in file")

plot.scatter(xarray, yarray, 100)
plot.show()