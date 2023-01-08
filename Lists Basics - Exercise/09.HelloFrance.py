inpt = input().split("|")
budget = int(input())
clothesAndPrice = []

clothesMax = 50
shoesMax = 50
accessoriesMax = 20.50

profit = 0
newPrices = 0
listPrices = []

for i in inpt:
    clothesAndPrice.append(i)

for i in clothesAndPrice:
    splitted = i.split("->")
    clothes = splitted[0]
    prices = float(splitted[1])

    if(clothes == "Clothes" and prices > clothesMax): continue
    if(clothes == "Shoes" and prices > shoesMax) : continue
    if(clothes == "Accessories" and prices > accessoriesMax): continue

    budget -= prices
    if(budget < 0):
        budget += prices
        continue
    
    savePrice = prices
    prices += prices * 0.4
    listPrices.append(round(prices, 2))
    profit += round(prices - savePrice)
    newPrices += prices

print(*listPrices)
print(f"Profit: {profit:.2f}")

if(newPrices + budget >= 150):
    print("Hello, France!")
else:
    print("Not enough money.")

