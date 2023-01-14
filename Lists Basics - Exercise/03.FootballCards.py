inpt = input().split()

teamAList = [int(x) for x in range(1, 12)]
teamBList = [int(x) for x in range(1, 12)]

sequenceOfCards = []
terminated = False

for i in inpt:
    sequenceOfCards.append(i)

for i in sequenceOfCards:
    separate = i.split("-")
    team = separate[0]
    number = int(separate[1])

    if(team == "A"):
        if(number in teamAList):
            teamAList.remove(number)
        if(len(teamAList) < 7):
            terminated = True
            break

    elif(team == "B"):
        if(number in teamBList):
            teamBList.remove(number)
        if(len(teamBList) < 7):
            terminated = True
            break

print(f"Team A - {len(teamAList)}; Team B - {len(teamBList)}")
if(terminated):
    print("Game was terminated")
