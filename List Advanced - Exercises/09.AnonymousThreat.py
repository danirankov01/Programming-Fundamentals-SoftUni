data = list(map(str, input().split()))
while(True):
    command = input().split()
    if(command[0] == "3:1"):
        break
    mergeOrDivide = command[0]

    if(mergeOrDivide == "merge"):
        startIndex = int(command[1])
        endIndex = int(command[2])
        if(0 <= startIndex < len(data) and 0 <= endIndex < len(data)):
            nextOne = data.index(data[startIndex + 1])
            for i in range(startIndex + 1, endIndex + 1):
                data[startIndex] += data[nextOne]
                data.pop(nextOne)

        elif(0 <= startIndex and startIndex < len(data)): #and endIndex < 0 or endIndex > len(data)):
            nextOne = data.index(data[startIndex + 1])
            for i in range(startIndex + 1, len(data)):
                data[startIndex] += data[nextOne]
                data.pop(nextOne)

        elif(0 > startIndex and endIndex < len(data)):
            finalOne = data.index(data[endIndex])
            firstElement = ""
            for i in range(finalOne + 1):
                firstElement += data[0]
                data.pop(0)
            data.insert(0, firstElement)

    elif(mergeOrDivide == "divide"):
        index = int(command[1])
        partitions = int(command[2])
        currentWord = data[index]

        if(len(data[index]) < partitions):
            continue

        if(len(currentWord) % partitions == 0):
            newElement = ""
            data.pop(index)
            position = index
            howMuch = len(currentWord) / partitions
            rememberHowMuch = howMuch
            for i in range(len(currentWord)):
                newElement += currentWord[i]
                if(i + 1 == howMuch):
                    data.insert(position, newElement)
                    newElement = ""
                    position += 1
                    howMuch += rememberHowMuch 
        else:
            newElement = ""
            data.pop(index)
            position = index
            howMuch = len(currentWord) % partitions
            letters = int(len(currentWord) / partitions)
            rememberLetters = letters
            equalToPartition = 0
            for i in range(len(currentWord)):
                newElement += currentWord[i]
                if(i + 1 == letters):
                    if(equalToPartition + 1 < partitions):
                        data.insert(position, newElement)
                        newElement = ""
                        position += 1
                        letters += rememberLetters
                        equalToPartition += 1
                    else:
                        newElement += currentWord[i + 1:]
                        data.insert(position, newElement)
                        break

for i in data:
    print(i, end=" ")
print()    


# print(8 % 3)
# print(7 / 3)