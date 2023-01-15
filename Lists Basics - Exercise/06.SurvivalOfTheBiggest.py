listOfNumbers = list(map(int, input().split()))
numberToRemove = int(input())

for i in range(numberToRemove):
    minNumber = min(listOfNumbers)
    for j in range(len(listOfNumbers)):
        listOfNumbers.remove(minNumber)
        break
print(*listOfNumbers, sep=", ")