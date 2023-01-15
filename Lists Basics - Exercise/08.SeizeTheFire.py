import re

inpt = input()
levelOfFire = re.split(r' = |#', inpt)
amountOfWater = int(input())
effort = 0
puttedOut = []

for i in range(len(levelOfFire)):
    if(levelOfFire[i] == "High"):
        number = int(levelOfFire[i + 1])
        if(number >= 81 and number <= 125):
            if(amountOfWater >= number):
                amountOfWater -= number
                effort += number / 4
                puttedOut.append(number)
    
    elif(levelOfFire[i] == "Medium"):
        number = int(levelOfFire[i + 1])
        if(number >= 51 and number <= 80):
            if(amountOfWater >= number):
                amountOfWater -= number
                effort += number / 4
                puttedOut.append(number)

    elif(levelOfFire[i] == "Low"):
        number = int(levelOfFire[i + 1])
        if(number >= 1 and number <= 50):
            if(amountOfWater >= number):
                amountOfWater -= number
                effort += number / 4
                puttedOut.append(number)

print("Cells:")
for i in puttedOut:
    print(f" - {i}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(puttedOut)}")