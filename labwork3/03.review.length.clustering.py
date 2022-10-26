import pandas as pd
import itertools
import json

#open review file
reviewFile = open("../dataset/Yelp/yelp_academic_dataset_review.json")
data = []

#Because json file too heavy so only read 100 first lines
for line in itertools.islice(reviewFile,100):
  line = line.strip()
  if not line: continue
  data.append(json.loads(line))
  
#DataFrame of review_file
reviewDF = pd.DataFrame(data)
nbRow = reviewDF.shape[0] #number of Row

#close the review_file
reviewFile.close()

#count words in each review
reviewLength = []
for r in range(nbRow):
    length = len(reviewDF.iloc[r]['text'])
    reviewLength.append(length)

distDict = {}
for i in reviewLength:
    dist = []
    for k in reviewLength:
        dist2point = abs(k - i)
        dist.append(dist2point)
    indexReviewLength = reviewLength.index(i)
    distDict[indexReviewLength] = dist
    