import Labwork3Function as func

reviewDF = func.readFile(10)
reviewLength = func.reviewLength(reviewDF)
reviewMatrix = func.reviewMatrix(reviewLength)
reviewMinumum = func.reviewMinimum(reviewMatrix)
mergeCluster = func.mergeCluster(reviewMinumum)