inpt = input().split()
teamA = 11
teamB = 11

teamAList = []
teamBList = []

sequenceOfCards = []
terminated = False

for i in inpt:
    sequenceOfCards.append(i)

if(len(sequenceOfCards) > 0):
    for i in sequenceOfCards:
        teamNumber = i.split("-")
        if(i[0] == "A"):
            if(teamNumber[1] not in teamAList):
                teamA -= 1
                if(teamA < 7):
                    print(f"Team A - {teamA}; Team B - {teamB}\nGame was terminated")
                    terminated = True
                    break
                teamAList.append(i[2])
        else:
            if(teamNumber[1] not in teamBList):
                teamB -= 1
                if(teamB < 7):
                    print(f"Team A - {teamA}; Team B - {teamB}\nGame was terminated")
                    terminated = True
                    break
                teamBList.append(i[2])
else:
    print("Team A - 11; Team B - 11")

if(len(sequenceOfCards) > 0 and terminated == False):
    print(f"Team A - {teamA}; Team B - {teamB}")




# team = "A-10"
# new = team.split("-")
# print(new[1])