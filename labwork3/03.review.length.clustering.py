import pandas as pd
import itertools
import json

#open review file
reviewFile = open("../dataset/Yelp/yelp_academic_dataset_review.json")
data = []

#Because json file too heavy so only read 10000 first lines
for line in itertools.islice(reviewFile,10000):
  line = line.strip()
  if not line: continue
  data.append(json.loads(line))
  
#DataFrame of review_file
reviewDF = pd.DataFrame(data)

#close the review_file
reviewFile.close()

#count words in each review
reviewLength = []
for r in range(reviewDF.shape[0]):
    length = len(reviewDF.iloc[r]['text'])
    reviewLength.append(length)
    
