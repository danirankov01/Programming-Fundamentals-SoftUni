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


# quantity_decorations = int(input())
# days_until_christmas = int(input())
# points = 0
# total_price = 0
# days_counter = 0
# for day in range(days_until_christmas, 0, -1):
#     days_counter += 1
#     if days_counter % 11 == 0:
#         quantity_decorations = quantity_decorations + 2
#     if days_counter % 2 == 0:
#         total_price += quantity_decorations * 2
#         points += 5
#     if days_counter % 3 == 0:
#         total_price += (quantity_decorations * 5) + (quantity_decorations * 3)
#         points += 3 + 10
#     if days_counter % 5 == 0:
#         total_price += quantity_decorations * 15
#         points += 17
#         if days_counter % 3 == 0:
#             points += 30
#     if days_counter % 10 == 0:
#         points -= 20
#         total_price += 5 + 3 + 15
# if days_counter % 10 == 0:
#     points -= 30
# print(f"Total cost: {total_price} \nTotal spirit: {points}")





# quantityOfDecorations = int(input())
# daysUntilChristmas = int(input())

# spirit = 0
# moneyNeeded = 0
# days = 0

# while(daysUntilChristmas != 0):
#     days += 1
#     if(days % 2 == 0):
#         moneyNeeded += quantityOfDecorations * 2
#         spirit += 5
#     if(days % 3 == 0):
#         moneyNeeded += quantityOfDecorations * (5 + 3)
#         spirit += 3
#     if(days % 5 == 0):
#         moneyNeeded += quantityOfDecorations * 15
#         spirit += 17
#         if(days % 3 == 0):
#             spirit += 30
#     if(days % 10 == 0):
#         spirit -= 20
#         moneyNeeded += 
#     daysUntilChristmas -= 1