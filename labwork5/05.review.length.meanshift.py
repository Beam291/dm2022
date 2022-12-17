import itertools
from traceback import print_tb
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
    #Close the open file
    reviewFile.close()
    return reviewDF

def countLength(reviewDF : pd.DataFrame):
    reviewLength = {}
    for i in range(len(reviewDF)):
        length = len(reviewDF.iloc[i]['text'])
        reviewLength[i] = length
    return reviewLength

def Average(lst):
    return sum(lst) / len(lst)

def meanShift(reviewLength : dict, radius : int, mode : list):
    newModeList = []
    #Find new mode
    for i in mode:
        lengthCen = []
        for k, v in reviewLength.items():
            distCal = abs(i - v)
            if distCal < radius:
                lengthCen.append(v)
            else:
                continue
        newMode = Average(lengthCen)
        newMode = float("{:.2f}".format(newMode))
        newModeList.append(newMode)
    #find duplicate node
    newModeList = list(dict.fromkeys(newModeList))
    return newModeList

#Program start from here
nbComment = 10
radius = 100
mode = []

reviewDF = readFile(nbComment)
reviewLength = countLength(reviewDF)  
for k, v in reviewLength.items():
    mode.append(v)
mode.sort()    

while(True):
    newModeList = meanShift(reviewLength, radius, mode)
    if mode != newModeList:
        mode = newModeList
        print(mode)
    else:
        break
    