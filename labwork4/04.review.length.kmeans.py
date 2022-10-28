import Labwork4Function as func

reviewDF = func.readFile(10)
reviewLength = func.reviewLength(reviewDF)
reviewMatrix = func.reviewMatrix(reviewLength)
selectRandomPoint = func.randomPoint(reviewLength)
print(selectRandomPoint)