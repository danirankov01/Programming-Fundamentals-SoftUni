events = list(map(str, input().split("|")))
currentEnergy = 100
coins = 100
closed = False

for i in events:
    splitted = i.split("-")
    eventOrIngredient = splitted[0]
    number = int(splitted[1])

    if(eventOrIngredient == "rest"):
        if(currentEnergy + number > 100):
            gainedEnergy = 100 - currentEnergy
            print(f"You gained {gainedEnergy} energy.")
            currentEnergy = 100
            print(f"Current energy: {currentEnergy}.")
        
        elif(currentEnergy + number <= 100):
            currentEnergy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {currentEnergy}.")

    elif(eventOrIngredient == "order"):
        if(currentEnergy - 30 >= 0):
            coins += number
            currentEnergy -= 30
            print(f"You earned {number} coins.")
        else:
            currentEnergy += 50
            print("You had to rest!")

    else:
        if(coins - number >= 0):
            coins -= number
            print(f"You bought {eventOrIngredient}.")
        else:
            print(f"Closed! Cannot afford {eventOrIngredient}.")
            closed = True
            break

if(not closed):
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {currentEnergy}")                