firstList = [x for x in input().split(", ")]
secondList = [x for x in input().split(", ")]

result = []
for i in range(len(firstList)):
    for j in secondList:
        if(firstList[i] in j):
            result.append(firstList[i])
            break
print(result)