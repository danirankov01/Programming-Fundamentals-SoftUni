line = input().split()
text = [x for x in line]

numberList = []
nonNumbersList = []

for i in text:
    for j in i:
        if(ord(j) >= 48 and ord(j) <= 57):
            numberList.append(int(j))

for i in text:
    for j in i:
        if(ord(j) < 48 or ord(j) > 57):
            nonNumbersList.append(j)

takeList = []
skipList = []

for i in range(len(numberList)):
    if(i % 2 == 0):
        takeList.append(numberList[i])
    else:
        skipList.append(numberList[i])

result = ""
for i in range(len(takeList)):
    for j in range(i, len(skipList)):
        takenString = ""
        skippedString = ""

        takenString += "".join(nonNumbersList[0:takeList[i]])
        del nonNumbersList[0:takeList[i]]
        skippedString += "".join(nonNumbersList[0:skipList[j]])
        del nonNumbersList[0:skipList[j]]

        result += takenString
        break

print(result)