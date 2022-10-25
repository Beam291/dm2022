import itertools
import json
import pandas as pd
import string

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

#Dealing with the first line review of the json file
#first data
reviewText1 = reviewDF.iloc[0]['text']

#remove punctuation
reviewText1 = reviewText1.translate(str.maketrans('', '', string.punctuation))

#Lowercase
reviewText1 = reviewText1.lower()