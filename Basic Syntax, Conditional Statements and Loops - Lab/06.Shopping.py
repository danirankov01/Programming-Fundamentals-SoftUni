budget = int(input())
bought = False
while(True):
    prices = input()
    if(prices != "End" and budget - int(prices) < 0):
        print("You went in overdraft!")
        break
    if(prices == "End"):
        bought = True
        break
    budget -= int(prices)

if(bought):
    print("You bought everything needed.")