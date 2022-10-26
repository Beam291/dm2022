import pandas as pd
import itertools
import json

#open review file
reviewFile = open("../dataset/Yelp/yelp_academic_dataset_review.json")
data = []

#Because json file too heavy so only read 1000 first lines
for line in itertools.islice(reviewFile,100):
  line = line.strip()
  if not line: continue
  data.append(json.loads(line))
  
#DataFrame of review_file
reviewDF = pd.DataFrame(data)
nbRow = reviewDF.shape[0] #number of Row

#Create matrix
reviewMatrix = [[0 for x in range(nbRow)] for y in range(nbRow)]

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
          
    
#     for m in range(nbRow):
#         for n in range(nbRow): 
#             for x in dist:
#                 reviewMatrix[m][n] = x

# print(reviewMatrix)
            
# print(reviewMatrix)