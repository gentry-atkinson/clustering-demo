#!/usr/bin/env python3

import json
import matplotlib.pyplot as plot
xarray = list()
yarray = list()

inFile = open("real_data.json")

line = inFile.readline()

try:
    while (inFile):
        line = inFile.readline()
        item = json.loads(line)
        #if (float(item["Latitude"]) > 28):
        xarray.append(float(item["X"]))
        yarray.append(float(item["Y"]))
        #print ("X=", item["Latitude"], " Y=", item["Longitude"])
except:
    print ("bad value in file")

plot.scatter(xarray, yarray, 5, "blue")
plot.show()