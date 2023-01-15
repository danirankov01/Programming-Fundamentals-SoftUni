# inpt = input().split("|")
# budget = int(input())
# clothesAndPrice = []

# clothesMax = 50
# shoesMax = 50
# accessoriesMax = 20.50

# profit = 0
# newPrices = 0
# listPrices = []

# for i in inpt:
#     clothesAndPrice.append(i)

# for i in clothesAndPrice:
#     splitted = i.split("->")
#     clothes = splitted[0]
#     prices = float(splitted[1])

#     if(clothes == "Clothes" and prices > clothesMax): continue
#     if(clothes == "Shoes" and prices > shoesMax) : continue
#     if(clothes == "Accessories" and prices > accessoriesMax): continue

#     budget -= prices
#     if(budget < 0):
#         budget += prices
#         continue
    
#     savePrice = prices
#     prices += round(prices * 0.4, 2)
#     listPrices.append(round(prices, 2))
#     profit += prices - savePrice
#     newPrices += prices

# print(*listPrices)
# print(f"Profit: {profit:.2f}")

# if(newPrices + budget >= 150):
#     print("Hello, France!")
# else:
#     print("Not enough money.")



trainTicketPrice = 150
items = list(map(str, input().split("|")))
budget = int(input())
savePrices = []
profit = 0

for i in items:
    splitted = i.split("->")
    clothe = splitted[0]
    priceOfClothe = float(splitted[1])

    if(clothe == "Clothes" and priceOfClothe <= 50):
        if(budget - priceOfClothe >= 0):
            budget -= priceOfClothe
            increased = round(priceOfClothe + priceOfClothe * 0.4, 2)
            profit += increased - priceOfClothe
            savePrices.append(increased)
    
    elif(clothe == "Shoes" and priceOfClothe <= 35):
        if(budget - priceOfClothe >= 0):
            budget -= priceOfClothe
            increased = round(priceOfClothe + priceOfClothe * 0.4, 2)
            profit += increased - priceOfClothe
            savePrices.append(increased)

    elif(clothe == "Accessories" and priceOfClothe <= 20.50):
        if(budget - priceOfClothe >= 0):
            budget -= priceOfClothe
            increased = round(priceOfClothe + priceOfClothe * 0.4, 2)
            profit += increased - priceOfClothe
            savePrices.append(increased)

newBudget = budget + sum(savePrices)
print(*savePrices,sep=" ")
print(f"Profit: {profit:.2f}")

if(newBudget >= trainTicketPrice):
    print("Hello, France!")
else:
    print("No enough money.")