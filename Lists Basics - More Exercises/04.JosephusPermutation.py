inpt = input().split()
movingPositions = int(input())
listNumbers = []
result = []

for i in inpt:
    listNumbers.append(int(i))

for i in range(len(listNumbers)):
    result.append(listNumbers[movingPositions - 1])
