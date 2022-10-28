import json
import re

data_file = open("../dataset/Yelp/yelp_academic_dataset_review.json")

n = 9

lengthdict = {}
for i, line in enumerate(data_file):
    x = json.loads(line)['text']
    lengthdict[i] = len(x)
    if i>n:
        break

def distancematrixcal(lengthdict):
    distancematrix ={}
    for k1, v1 in lengthdict.items():
        distance = {}
        for k2, v2 in lengthdict.items():
            distance[k2] = abs(lengthdict[k1] - v2)
        distancematrix[k1] = distance
    print(distancematrix)
    print("======================================")
    #remove 0
    for k1, v1 in distancematrix.items():
        v1 = {key: val for key, val in v1.items() if val != 0}
        distancematrix[k1] = v1
    print(distancematrix)
    return distancematrix

distancematrixcal(lengthdict)

#print(matrix)
"""
for k, v in matrix.items():
    print(k)
    print(v)
"""

def mindistancecal(matrix):
    distance = []
    for k1, v1 in matrix.items():
        k2 = min(v1, key=v1.get)
        v2 = min(v1.values())
        distance.append(v2)
    return min(distance)

def pointstomerge(distancematrix, distance):
    mindistance = mindistancecal(matrix)
    for k1, v1 in matrix.items():
        for k2, v2 in v1.items():
            if v2 == mindistance:
                return k1, k2

def mergingpoints(lengthdict, distancematrix, lastposition):
    newvalue = 0
    for i in pointstomerge(distancematrix, mindistancecal(distancematrix)):
        newvalue = newvalue + lengthdict[i]
        lengthdict.pop(i)
    lengthdict[lastposition+1] = newvalue/2
    lastposition = lastposition+1
    return lengthdict, lastposition


"""
lastposition = n
for i in range(n):
    matrix = distancematrixcal(lengthdict)
    lengthdict, lastposition = mergingpoints(lengthdict, distancematrixcal(lengthdict), lastposition)
    print(lengthdict)
"""
