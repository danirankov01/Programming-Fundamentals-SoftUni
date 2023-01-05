budget = float(input())
flourPrice = float(input())

eggsPackPrice = flourPrice * 3 / 4
literMilkPrice = flourPrice + flourPrice / 4
quarterMilkPrice = literMilkPrice / 4

oneLoavePrice = eggsPackPrice + flourPrice + quarterMilkPrice
loaveCounter = 0
coloredEggs = 0
while(True):
    if(budget >= oneLoavePrice):
        budget -= oneLoavePrice
        loaveCounter += 1
        coloredEggs += 3
        if(loaveCounter % 3 == 0):
            coloredEggs -= loaveCounter - 2
    else:
        break
print(f"You made {loaveCounter} loaves of Easter bread! Now you have {coloredEggs} eggs and {budget:.2f}BGN left.")