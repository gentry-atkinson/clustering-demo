#!/usr/bin/env python

import numpy
from freediscovery.cluster import Birch, birch_hierarchy_wrapper
import json
import matplotlib.pyplot as plot

inFile = open("Real-Time_Traffic_Incident_Reports.json")

line = inFile.readline()
line = inFile.readline()
item = json.loads(line)

X = numpy.array([float(item["Latitude"]), float(item["Longitude"])])


try:
    while (inFile):
        line = inFile.readline()
        item = json.loads(line)
        if (float(item["Latitude"]) > 28):
            item_array = numpy.array([float(item["Latitude"]), float(item["Longitude"])])
            X = numpy.vstack((X, item_array))
except:
    print ("Bad value in file")

print (len(X), " values in data")

cluster_model = Birch(threshold=0.1, branching_factor=20, compute_sample_indices=True, n_clusters=3)

cluster_model.fit(X)

htree, _ = birch_hierarchy_wrapper(cluster_model)
print('Total number of subclusters:', htree.tree_size)

print (cluster_model.labels_)

print (len(cluster_model.labels_))

color = {1 : "red", 2 : "green", 3 : "blue", 4: "black", 5 : "white", 0 : "yellow"}
counter = 0

for point in X:
    plot.scatter(point[0], point[1], 10, color[cluster_model.labels_[counter]])
    counter += 1

plot.title("BIRCH on Set 2")
plot.show()

#htree.display_tree()
