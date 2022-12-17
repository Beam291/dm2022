
import math
import json
import re

data_file = open("/media/leon/MCU/USTH/Data mining/DataMining data/yelp_academic_dataset_review.json")

class cluster:
    def __init__(self, centroid):
        self.points = []
        self.centroid = centroid

    def __del__(self):
        return None

    def new_centroid(self):
        self.centroid = sum(self.points) / len(self.points)
        self.points = []
        return self.centroid

    def add_points(self, point):
        self.points.append(point)


pointlist = []
for i, line in enumerate(data_file):
    x = json.loads(line)['text']
    pointlist.append(len(x))
    if i>100:
        break

def kmean(centroidlist):
    centroidlist = centroidlist
    clusterlist = []
    for i in centroidlist:
        c = cluster(i)
        clusterlist.append(c)

    for i in pointlist:
        distance_list = []
        for j in clusterlist:
            distance_list.append(abs(i - j.centroid))
        min_distance = min(distance_list)

        for j in clusterlist:
            if min_distance == abs(i - j.centroid):
                j.add_points(i)

    centroidlist = []
    for k in clusterlist:
        centroidlist.append(k.new_centroid())

    return centroidlist


centroidlist = [200,500,600]
threshold = 5

while True:
    if (abs(sum(centroidlist)/len(centroidlist) - sum(kmean(centroidlist))/len(kmean(centroidlist)))) < threshold:
        print("End")
        break
    else:
        centroidlist = kmean(centroidlist)
        print(centroidlist)






