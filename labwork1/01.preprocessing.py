import itertools
import json
import pandas as pd
import string
from nltk.corpus import stopwords

#open review file
reviewFile = open("../../dataset/Yelp/yelp_academic_dataset_review.json")
data = []

#Because json file too heavy so only read 3 first lines
for line in itertools.islice(reviewFile,3):
  line = line.strip()
  if not line: continue
  data.append(json.loads(line))
  
#DataFrame of review_file
reviewDF = pd.DataFrame(data)

#close the review_file
reviewFile.close()

#count word function 
def word_count(str : str):
    counts = dict()
    words = str.split() #Break by space

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

#preprcoessing function 
def preprocessing(reviewDataFrame : pd.DataFrame):
  reviewCombie = ""
  
  #Combie the review data
  for r in range(reviewDataFrame.shape[0]):
    reviewText = reviewDataFrame.iloc[r]['text']
    reviewText : str
    reviewCombie+=reviewText
    
  reviewCombie = reviewCombie.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
  reviewCombie = reviewCombie.lower() #Lowercase
  
  reviewDict = word_count(reviewCombie) #count word 
  
  stopWords = set(stopwords.words('english'))

  for i in list(reviewDict.keys()):
    if i in stopWords:
      del reviewDict[i]
  
  print(reviewDict)
    
preprocessing(reviewDF)