budget = int(input())
output = False
while(True):
    prices = input()
    if(prices == "End"):
        output = True
        break
    budget -= int(prices)
    if(budget <= 0):
        print("You went in overdraft!")
        break
if(output):
    print("You bought everything needed.")