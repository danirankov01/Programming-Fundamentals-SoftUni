inpt1 = input().split()
inpt2 = input().split()
inpt3 = input().split()

firstList = [x for x in inpt1]
secondList = [x for x in inpt2]
thirdList = [x for x in inpt3]

winner = False
winnerNumber = 0

for i in range(len(firstList)):
    if(firstList[i] == secondList[i] == thirdList[i]):
        if(firstList[i] != 0):
            winnerNumber = firstList[i]
            winner = True
            break
    if(i == 0):
        if(firstList[i] == secondList[i + 1] == thirdList[i + 2]):
            winnerNumber = firstList[i]
            winner = True
            break
    if(i == 1):
        if(firstList[i - 1] == firstList[i] == firstList[i + 1]): winnerNumber = firstList[i]
        if(secondList[i - 1] == secondList[i] == secondList[i + 1]): winnerNumber = secondList[i]
        if(thirdList[i - 1] == thirdList[i] == thirdList[i + 1]): winnerNumber = thirdList[i]
        if(winnerNumber != 0):
            winner = True
            break
    if(i == 2):
        if(firstList[i] == secondList[i - 1] == thirdList[i - 2]):
            winnerNumber = firstList[i]
            winner = True
            break
if(winnerNumber == "1"): 
    print("First player won")           
elif(winnerNumber == "2"): 
    print("Second player won")
else:
    print("Draw")