numberOfOrders = int(input())
total = 0

for i in range(numberOfOrders):
    price = 0
    pricePerCapsule = float(input())
    if(pricePerCapsule < 0.01 or pricePerCapsule > 100):
        continue
    days = int(input())
    if(days < 1 or days > 31):
        continue
    capsulesPerDay = int(input())
    if(capsulesPerDay < 1 or capsulesPerDay > 2000):
        continue
    price += pricePerCapsule * capsulesPerDay * days
    total += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")