inpt = input().split("|")

energy = 100
coins = 100

events = []
finish = True
for i in inpt:
    events.append(i)

for i in events:
    splited = i.split("-")
    eventOrIngredient = splited[0]
    spending = int(splited[1])
    if(eventOrIngredient == "rest"):
        if(energy + spending > 100):
            print(f"You gained {100 - energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            energy += spending
            print(f"You gained {spending} energy.")
            print(f"Current energy: {energy}.")
    elif(eventOrIngredient == "order"):
        coins += spending
        energy -= 30
        if(energy > 0):
            print(f"You earned {spending} coins.")
        else:
            coins -= spending
            energy += 80
            print("You had to rest!")
    else:
        coins -= spending
        if(coins >= 0):
            print(f"You bought {eventOrIngredient}.")
        else:
            print(f"Closed! Cannot afford {eventOrIngredient}.")
            finish = False
            break

if(finish):
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")