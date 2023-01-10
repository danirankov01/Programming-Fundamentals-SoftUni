def order(drink, quantity):
    if(drink == "coffee"):
        print(f"{quantity * 1.50:.2f}")
    elif(drink == "coke"):
        print(f"{quantity * 1.40:.2f}")
    elif(drink == "water"):
        print(f"{quantity * 1:.2f}")
    elif(drink == "snacks"):
        print(f"{quantity * 2:.2f}")

drink = input()
quantity = float(input())
order(drink, quantity)