priceOfParts = 0
invalidOrder = False

while(True):
    prices = input()
    if(prices == "special" or prices == "regular"):
        break
    
    prices = float(prices)
    if(prices < 0):
        print("Invalid price!")
        continue

    priceOfParts += prices

if(not invalidOrder):
    priceWithTax = priceOfParts + priceOfParts * 0.2
    if(priceWithTax == 0):
        print("Invalid order!")
    
    else:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {priceOfParts:.2f}$")
        print(f"Taxes: {priceOfParts * 0.2:.2f}$")
        print("-----------")
        if(prices == "special"):
            print(f"Total price: {priceWithTax - 0.1 * priceWithTax:.2f}$")
        else:
            print(f"Total price: {priceWithTax:.2f}$")