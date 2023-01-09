inpt = input().split()
listNumbers = []
result = []

for i in inpt:
    listNumbers.append(int(i))

while(True):
    command = input().split()
    if(command[0] == "end"):
        break

    if(command[0] == "exchange"):
        index = int(command[1])
        if(index + 1 <= len(listNumbers) and index >= 0):
            for i in range(index + 1):
                result.append(listNumbers[0])
                listNumbers.pop(0)
                if(i == index):
                    break
            listNumbers.extend(result)
            result = []
        else:
            print("Invalid index")

    elif(command[0] == "max"):
        evenOrOdd = command[1]
        if(evenOrOdd == "even"):
            iterat = 0
            for i in range(len(listNumbers)):
                if(listNumbers[i] % 2 == 0):
                    if(iterat == 0):
                        iterat += 1
                        biggestEven = listNumbers[i]
                        index = i
                    else:
                        if(biggestEven <= listNumbers[i]):
                            biggestEven = listNumbers[i]
                            index = i
            if(iterat != 0):
                print(index)
            else:
                print("No matches")

        else:
            iterat = 0
            for i in range(len(listNumbers)):
                if(listNumbers[i] % 2 != 0):
                    if(iterat == 0):
                        iterat += 1
                        biggestOdd = listNumbers[i]
                        index = i
                    else:
                        if(biggestOdd <= listNumbers[i]):
                            biggestEven = listNumbers[i]
                            index = i
            if(iterat != 0):
                print(index)
            else:
                print("No matches")

    elif(command[0] == "min"):
        evenOrOdd = command[1]
        if(evenOrOdd == "even"):
            iterat = 0
            for i in range(len(listNumbers)):
                if(listNumbers[i] % 2 == 0):
                    if(iterat == 0):
                        iterat += 1
                        minEven = listNumbers[i]
                        index = i
                    else:
                        if(minEven >= listNumbers[i]):
                            minEven = listNumbers[i]
                            index = i
            if(iterat != 0):
                print(index)
            else:
                print("No matches")
            
        else:
            iterat = 0
            for i in range(len(listNumbers)):
                if(listNumbers[i] % 2 != 0):
                    if(iterat == 0):
                        iterat += 1
                        minOdd = listNumbers[i]
                        index = i
                    else:
                        if(minEven >= listNumbers[i]):
                            minOdd = listNumbers[i]
                            index = i
            if(iterat != 0):
                print(index)
            else:
                print("No matches")

    elif(command[0] == "first"):
        count = int(command[1])
        if(count > len(listNumbers)):
            print("Invalid count")
            continue
        counter = 0
        if(command[2] == "even"):
            firstEvenList = []
            for i in range(len(listNumbers)):
                if(listNumbers[i] % 2 == 0):
                    firstEvenList.append(listNumbers[i])
                    counter += 1
                    if(counter == count):
                        break
            print(firstEvenList)

        else:
            firstOddList = []
            for i in range(len(listNumbers)):
                if(listNumbers[i] % 2 != 0):
                    firstOddList.append(listNumbers[i])
                    counter += 1
                    if(counter == count):
                        break
            print(firstOddList)

    elif(command[0] == "last"):
        count = int(command[1])
        if(count > len(listNumbers)):
            print("Invalid count")
            continue
        counter = 0
        if(command[2] == "even"):
            lastEvenList = []
            for i in range(len(listNumbers)):
                if(listNumbers[-i - 1] % 2 == 0):
                    lastEvenList.append(listNumbers[-i - 1])
                    counter += 1
                    if(counter == count):
                        break
            lastEvenList.reverse()
            print(lastEvenList)

        else:
            lastOddList = []
            for i in range(len(listNumbers)):
                if(listNumbers[-i - 1] % 2 != 0):
                    lastOddList.append(listNumbers[-i - 1])
                    counter += 1
                    if(counter == count):
                        break
            lastOddList.reverse()
            print(lastOddList)
print(listNumbers)