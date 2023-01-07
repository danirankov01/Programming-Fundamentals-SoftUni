snowballsMade = int(input())
result = []

for i in range(snowballsMade):
    weightOfTheSnowball = int(input())
    timeNeededToReachTarget = int(input())
    qualityOfTheSnowball = int(input())

    value = int((weightOfTheSnowball / timeNeededToReachTarget) ** qualityOfTheSnowball)

    if(len(result) == 0):
        result.append(weightOfTheSnowball)
        result.append(timeNeededToReachTarget)
        result.append(value)
        result.append(qualityOfTheSnowball)
    else:
        if(value >= result[2]):
            result = []
            result.append(weightOfTheSnowball)
            result.append(timeNeededToReachTarget)
            result.append(value)
            result.append(qualityOfTheSnowball)

print(f"{result[0]} : {result[1]} = {result[2]} ({result[3]})")