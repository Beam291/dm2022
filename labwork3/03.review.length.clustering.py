import pandas as pd
import Labwork3Function as func

reviewDF = func.readFile(100)
nbRow = reviewDF.shape[0] #number of Row

# reviewMatrix = Matrix = [[0 for x in range(nbRow)] for y in range(nbRow)] 

#count words in each review
reviewLength = []
for r in range(nbRow):
    length = len(reviewDF.iloc[r]['text'])
    reviewLength.append(length)

distDict = {}
for i in range(len(reviewLength)):
    dist = []
    for k in reviewLength:
        dist2point = abs(k - reviewLength[i])
        dist.append(dist2point)
    distDict[i] = dist

# for m in range(nbRow):
#     for n in range(nbRow):
#         listDist = distDict[m]
#         reviewMatrix[m][n] = listDist[n]
