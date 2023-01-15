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
    print("Not enough money.")