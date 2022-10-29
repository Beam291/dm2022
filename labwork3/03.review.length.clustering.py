import itertools
from traceback import print_tb
import pandas as pd
import json
import re

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
def matrixGenerator(reviewDF : pd.DataFrame):
    reviewLength = countLength(reviewDF) 
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

#Find the min distant
def findMinDist(reviewMatrix : dict):
    minDist = {}
    for key, value in reviewMatrix.items():
        value : dict
        lowest = min(value, key = value.get)
        minDist[lowest] = value[lowest]
    return minDist
            
#Merging Point
def pointMerge(reviewMatrix : dict, minDist : dict):
    pointMerge = []
    for key, value in reviewMatrix.items():
        value : dict
        for k, v in value.items():
            for km, vm in minDist.items():
                if v == vm and km == key:
                    return key, k
    # return pointMerge

# Merging 
def merging(reviewMatrix : dict, reviewLength : dict, nbComment : int):
    # print(pointMerge(minDist, reviewMatrix))
    mergeData = 0
    for i in pointMerge(reviewMatrix, findMinDist(reviewMatrix)):
        if i in reviewLength:
            mergeData = mergeData + reviewLength[i]
            del reviewLength[i]
    reviewLength[nbComment + 1] = mergeData/2
    nbComment = nbComment + 1
    return reviewLength, nbComment
        
#Program start from here
nbComment = 10
reviewDF = readFile(nbComment)
reviewLength = countLength(reviewDF)
print(reviewLength)
# print(reviewLength)
for i in range(nbComment):
    reviewMatrix = matrixGenerator(reviewDF)  
    reviewLength, nbComment =  merging(reviewMatrix, reviewLength, nbComment)
print(reviewLength)

