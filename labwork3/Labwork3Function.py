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

#Calculate center of two point
def calCenter(value):
    return{value/2}

def commonElements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    result = [i for i in result if i != 0]
    return result