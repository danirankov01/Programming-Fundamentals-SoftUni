listNumbers = list(map(int, input().split()))
sum = 0
while(len(listNumbers) != 0):
    index = int(input())
    if(index < len(listNumbers)):
        popped = listNumbers.pop(index)
        sum += popped
        for i in range(len(listNumbers)):
            if(popped >= listNumbers[i]):
                listNumbers[i] += popped
            else:
                listNumbers[i] -= popped

    elif(index < 0):
        popped = listNumbers[0]
        sum += popped
        listNumbers.pop(0)

        for i in range(len(listNumbers)):
            if(popped >= listNumbers[i]):
                listNumbers[i] += popped
            else:
                listNumbers[i] -= popped

        listNumbers.insert(0, listNumbers[-1])

    elif(index >= len(listNumbers) - 1):
        popped = listNumbers[-1]
        sum += popped
        listNumbers.pop(len(listNumbers) - 1)

        for i in range(len(listNumbers)):
            if(popped >= listNumbers[i]):
                listNumbers[i] += popped
            else:
                listNumbers[i] -= popped

        listNumbers.insert(len(listNumbers), listNumbers[0])


print(sum)