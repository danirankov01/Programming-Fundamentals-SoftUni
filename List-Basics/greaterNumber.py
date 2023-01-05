firstInput = input().split(",")
secondInput = input().split(",")

firstList = [int(i) for i in firstInput]
secondList = [int(i) for i in secondInput]

output = []

for i in range(len(firstList)):
    for j in range(len(secondList)):
        if(firstList[i] == secondList[j]):
            for k in range(j, len(secondList)):
                if(secondList[k] > secondList[j]):
                    output.append(secondList[k])
                    break
                else:
                    if(k + 1 == len(secondList)):
                        output.append(-1)
print(*output,sep=",")