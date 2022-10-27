import Labwork3Function as func

reviewDF = func.readFile(100)
nbRow = reviewDF.shape[0] #number of Row

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

distDict1 = {}
#find min
for key, value in distDict.items():
    list1 = value
    list2 = value
    print(func.commonElements(list1, list2))        
        