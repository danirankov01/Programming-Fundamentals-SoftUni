gifts = list(map(str, input().split()))
while(True):
    command = input().split()
    if(command[0] == "No" and command[1] == "Money"):
        break

    if(command[0] == "OutOfStock"):
        if(command[1] in gifts):
            for i in range(len(gifts)):
                if(gifts[i] == command[1]):
                    gifts[i] = "None"
                
    elif(command[0] == "Required"):
        item = command[1]
        index = int(command[2])
        if(0 <= index < len(gifts)):
            gifts[index] = item

    elif(command[0] == "JustInCase"):
        item = command[1]
        gifts[-1] = item

for i in gifts:
    if(i == "None"):
        continue
    print(i, end=" ")
print()