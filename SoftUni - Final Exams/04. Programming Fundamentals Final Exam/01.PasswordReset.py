inpt = input()

while(True):
    line = input().split()

    if(line[0] == "Done"): break
    new = ""

    if(line[0] == "TakeOdd"):
        for i in range(len(inpt)):
            if(i % 2 != 0):
                new += inpt[i]
        inpt = new
        print(inpt)

    elif(line[0] == "Cut"):
        index = int(line[1])
        length = int(line[2])

        new = inpt[:index] + inpt[index + length:]
        inpt = new

        print(inpt)

    elif(line[0] == "Substitute"):
        substring = line[1]
        substitute = line[2]

        if(substring in inpt):
            inpt = inpt.replace(substring, substitute)
            print(inpt)
            
        else:
            print("Nothing to replace!")

print(f"Your password is: {inpt}")