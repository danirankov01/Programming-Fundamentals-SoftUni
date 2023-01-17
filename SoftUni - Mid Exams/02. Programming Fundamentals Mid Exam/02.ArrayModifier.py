list = list(map(int, input().split()))

while(True):

    commmands = input().split()

    if(commmands[0] == "end"): break

    if(commmands[0] == "decrease"):
        for i in range(len(list)):
            list[i] -= 1
    
    if(commmands[0] != "decrease"):

        firstIndex = int(commmands[1])
        secondIndex = int(commmands[2])

        if(commmands[0] == "swap"):
            list[firstIndex], list[secondIndex] = \
            list[secondIndex], list[firstIndex]


        elif(commmands[0] == "multiply"):
            multiplied = list[firstIndex] * list[secondIndex]
            list[firstIndex] = multiplied

print(*list, sep=", ")