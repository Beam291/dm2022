
import math
import json
import re

data_file = open("/media/leon/MCU/USTH/Data mining/DataMining data/yelp_academic_dataset_review.json")

class cluster:
    def __init__(self, cluster_mode):
        self.cluster_mode = cluster_mode
        self.points = []

    def add_points(self, point):
            self.points.append(point)

class point:
    def __init__(self, text):
        self.text = text
        self.datapoint = len(text)
        self.mode = self.datapoint

    def flat_kernel(self, x , h):
        if x <= h:
            k = 1
        else:
            k = 0
        return k

    def distance_cal(self,x1, x2):
        distance = abs(x1 - x2)
        return distance

    def shift_mode(self, pointlist, h):
            self.mode = sum(p.datapoint * self.flat_kernel(self.distance_cal(p.datapoint, self.mode),h) for p in pointlist) \
                 / sum(self.flat_kernel(self.distance_cal(p.datapoint, self.mode),h) for p in pointlist)

            #print(self.mode)
            return self.mode

pointlist = []
for i, line in enumerate(data_file):
    x = json.loads(line)['text']
    p = point(x)
    pointlist.append(p)
    if i>10:
        break


modelist = []
for i in pointlist:
    mode_of_i = 0
    while True:
        new_mode = i.shift_mode(pointlist,100)
        #print(new_mode)
        if round(new_mode,3) == round(mode_of_i,3):
            #print("break")
            break
        else:
            #print("new mode")
            mode_of_i = round(new_mode,3)
    modelist.append(mode_of_i)

#print(modelist)


cluster_mode = []
for i in modelist:
    if i not in cluster_mode:
        cluster_mode.append(i)
print(cluster_mode)


cluster_list = []
for i in cluster_mode:
    cluster_list.append(cluster(i))
#print(cluster_list)

for i, c in enumerate(cluster_list):
    for j, m in enumerate(modelist):
        if  cluster_mode[i] == m:
            c.add_points(pointlist[j])

for i, c in enumerate(cluster_list):
    print("cluser: ", i, "cluter mode:", c.cluster_mode)
    for j in c.points:
        print (j.datapoint)