import itertools
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
        
#Find minimum
def reviewMinimum(reviewMatrix : dict):
    reviewMinimumDict = {}
    for key, value in reviewMatrix.items():
        value : dict
        minDict = {}
        lowest = min(value, key = value.get)
        minDict[lowest] = value[lowest]
        reviewMinimumDict[key] = minDict
    return reviewMinimumDict

#Calculate centroid of two point
def calCentroid(value):
    return{value/2}

#Merge cluster
def mergeCluster(reviewMinimumDict : dict):
    for key, value in reviewMinimumDict.items():
        value : dict
        st = {}
        for k, v in value.items():
            if k == key:
                st[k] == key
        print(st)
            
                
# def commonElements(list1, list2):
#     result = []
#     for element in list1:
#         if element in list2:
#             result.append(element)
#     result = [i for i in result if i != 0]
#     return result