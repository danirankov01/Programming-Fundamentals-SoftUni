lostFightCount = int(input())

helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

fightsCount = 0
total = 0
shieldCounter = 0
while(lostFightCount > 0):
    fightsCount += 1
    if(fightsCount % 2 == 0):
        total += helmetPrice
    if(fightsCount % 3 == 0):
        total += swordPrice
        if(fightsCount % 2 == 0):
            total += shieldPrice
            shieldCounter += 1
            if(shieldCounter % 2 == 0):
                total += armorPrice
    lostFightCount -= 1

print(f"Gladiator expenses: {total:.2f} aureus")