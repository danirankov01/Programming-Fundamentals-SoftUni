inpt = input().split()
listNumbers = []

firstCar = 0
secondCar = 0

for i in inpt:
    listNumbers.append(int(i))

for i in range(int((len(listNumbers) - 1) / 2)):
    if(listNumbers[i] != 0):
        firstCar += listNumbers[i]
    else:
        firstCar *= 0.8
        firstCar = round(firstCar, 1)

for i in range(len(listNumbers)):
    if(listNumbers[-i - 1] != 0):
        secondCar += listNumbers[-i - 1]
    else:
        secondCar *= 0.8
        secondCar = round(secondCar, 1)
    if(i + 1 == (len(listNumbers) - 1) / 2):
        break

if(firstCar < secondCar):
    print(f"The winner is left with total time: {firstCar:.1f}")
else:
    print(f"The winner is right with total time: {secondCar:.1f}")