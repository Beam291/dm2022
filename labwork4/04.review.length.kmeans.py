import itertools
from random import random
import pandas as pd
import json
import random
import warnings

warnings.filterwarnings("ignore")

#read file and number of comment you want to load in 
def readFile(nbComment : int):
    #open review file
    reviewFile = open("../dataset/Yelp/yelp_academic_dataset_review.json")
    data = []
    #Because json file too heavy so only read 100 first lines
    for line in itertools.islice(reviewFile, nbComment):
        line = line.strip()
        if not line: continue
        data.append(json.loads(line))
    #DataFrame of review_file
    reviewDF = pd.DataFrame(data)
    #Close the open file
    reviewFile.close()
    return reviewDF

#count the length of reviews from data
def countLength(reviewDF : pd.DataFrame):
    reviewLength = {}
    for i in range(len(reviewDF)):
        length = len(reviewDF.iloc[i]['text'])
        reviewLength[i] = length
    return reviewLength

#Calculate the distance between each point then put to a matrix
def matrixGenerator(reviewLength : dict):
    distMatrix = {}
    for key, value in reviewLength.items():
        dist = {}
        for key1, value1 in reviewLength.items():
            dist2point = abs(value - value1)
            dist[key1] = dist2point
        #remove 0 from dist
        dist = {x:y for x,y in dist.items() if y!=0}
        distMatrix[key] = dist
    return distMatrix

#random centroid 
def randCentroid(reviewLength : dict, numberOfCentroid : int):
    tempList = []
    keys = random.sample(reviewLength.keys(), numberOfCentroid)
    for i in keys:
        tempList.append(reviewLength.get(i))
    return tempList

def kCluster(reviewLength : dict, randCenList : list):
    cluster = {}
    for i in randCenList:
        cluster[i] = []
    
    for key, value in reviewLength.items():
        tempDist = {}
        for i in randCenList:
            distToCentroid = abs(i - value)
            tempDist[i] = distToCentroid
        lowest = min(tempDist, key = tempDist.get)
        for k, v in cluster.items():
            v : list
            if lowest == k:
                v.append(reviewLength[key])
    print(cluster)
    return cluster

def Average(lst):
    return sum(lst) / len(lst)

def kCentroid(clusterList : dict):
    tempCen = []
    for k, v in clusterList.items():
        tempCen.append(Average(v))
    return tempCen
        
#Program start from here
nbComment = 10
numberOfCentroid = 3

reviewDF = readFile(nbComment)
# print(reviewDF.head())
reviewLength = countLength(reviewDF)
# print(reviewLength)
randCenList = randCentroid(reviewLength, numberOfCentroid)
# print(randCenList)

while(True):
    tempCen = []
    clusterList = kCluster(reviewLength, randCenList)
    # print(clusterList)
    for k, v in clusterList.items():
        tempCen.append(Average(v))
    if tempCen != randCenList:
        randCenList = tempCen
        print(randCenList)
    else:
        break