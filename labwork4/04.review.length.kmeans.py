import itertools
import random
import pandas as pd
import json

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
    reviewFile.close()
    
    return reviewDF

#Find review length
def reviewLength(reviewDF : pd.DataFrame):
    reviewLength = []
    for r in range(reviewDF.shape[0]):
        length = len(reviewDF.iloc[r]['text'])
        reviewLength.append(length)
    return reviewLength

#create matrix
def reviewMatrix(reviewLength : list): 
    distDict = {}
    for i in reviewLength:
        distList = []
        for k in reviewLength:
            dist2point = abs(k - i)
            distList.append(dist2point)
        distDict[reviewLength.index(i)] = distList
    
    for key, value in distDict.items():     
        value : list
        cluster = {}
        for v in value:
            cluster[value.index(v)] = v
        cluster = {x:y for x,y in cluster.items() if y!=0}
        distDict[key] = cluster
    return distDict

#Select 3 random point
def randomPoint(reviewLength : list):
    rngPoint = random.sample(reviewLength, 3)
    return rngPoint

reviewDF = func.readFile(10)
reviewLength = func.reviewLength(reviewDF)
reviewMatrix = func.reviewMatrix(reviewLength)
selectRandomPoint = func.randomPoint(reviewLength)
print(selectRandomPoint)