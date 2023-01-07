groupSize = int(input())
daysOfAdventure = int(input())

profit = 0
days = 0
while(daysOfAdventure != 0):
    days += 1
    profit += 50
    if(days % 10 == 0):
        groupSize -= 2
    if(days % 15 == 0):
        groupSize += 5
    profit -= groupSize * 2
    if(days % 3 == 0):
        profit -= groupSize * 3
    if(days % 5 == 0):
        profit += groupSize * 20
        if(days % 3 == 0):
            profit -= groupSize * 2
    daysOfAdventure -= 1
print(f"{groupSize} companions received {int(profit / groupSize)} coins each.")