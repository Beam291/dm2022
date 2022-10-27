import Labwork3Function as func

reviewDF = func.readFile(10)
reviewLength = func.reviewLength(reviewDF)
distDict = func.reviewMatrix(reviewLength)
