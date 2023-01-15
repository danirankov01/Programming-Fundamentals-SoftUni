inpt = input().split()
movingPositions = int(input())
listNumbers = []
result = []

counter = 0
index = 0

for i in inpt:
    listNumbers.append(int(i))

while(len(listNumbers) != 0):
    counter += 1
    if(counter % movingPositions == 0):
        result.append(listNumbers[index])
        listNumbers.pop(index)
    elif(counter % movingPositions != 0):
        index += 1

    if(index >= len(listNumbers)):
        index = 0

print(str(result).replace(' ', ''))