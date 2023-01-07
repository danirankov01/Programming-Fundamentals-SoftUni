lostFights = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

lost = 0
total = 0
shieldBreaks = 0
while(lostFights != 0):
    lost += 1
    if(lost % 2 == 0 and lost % 3 == 0):
        total += helmetPrice + swordPrice + shieldPrice
        shieldBreaks += 1
        if(shieldBreaks == 2):
            total += armorPrice
    else:
        if(lost % 2 == 0):
            total += helmetPrice
        if(lost % 3 == 0):
            total += swordPrice
    lostFights -= 1

print(f"Gladiator expenses: {total:.2f} aureus")