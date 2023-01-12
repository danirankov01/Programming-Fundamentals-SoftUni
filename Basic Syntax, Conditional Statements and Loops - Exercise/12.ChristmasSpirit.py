quantityOfDecorations = int(input())
daysUntilChristmas = int(input())
christmasSpirit = 0
moneyToSpend = 0

ornamentSet = 2 #5
treeSkirt = 5 #3
treeGarland = 3 #10
treeLights = 15 #17

days = 0

while(daysUntilChristmas != 0):
    days += 1
    if(days % 11 == 0):
        quantityOfDecorations += 2
    if(days % 2 == 0):
        moneyToSpend += ornamentSet * quantityOfDecorations
        christmasSpirit += 5
    if(days % 3 == 0 and days % 5 == 0):
        moneyToSpend += (treeSkirt + treeGarland + treeLights) * quantityOfDecorations
        christmasSpirit += 60
    else:
        if(days % 3 == 0):
            moneyToSpend += (treeSkirt + treeGarland) * quantityOfDecorations
            christmasSpirit += 13
        if(days % 5 == 0):
            moneyToSpend += treeLights * quantityOfDecorations
            christmasSpirit += 17
    if(days % 10 == 0):
        christmasSpirit -= 20
        moneyToSpend += treeSkirt + treeGarland + treeLights
        if(daysUntilChristmas == 1):
            christmasSpirit -= 30
    daysUntilChristmas -= 1

print(f"Total cost: {moneyToSpend}")
print(f"Total spirit: {christmasSpirit}")