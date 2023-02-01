inpt = input()

while(True):
    line = input()

    if(line == "Travel"): break

    line = line.split(":")

    if(line[0] == "Add Stop"):
        index = int(line[1])
        text = line[2]

        if(index >= 0 and index < len(inpt)):
            result = inpt[0:index] + text + inpt[index:]
            inpt = result

        print(inpt)

    elif(line[0] == "Remove Stop"):
        start = int(line[1])
        end = int(line[2])

        if(start <= end):
            if(start >= 0 and start < len(inpt) and end < len(inpt)):
                result = inpt[0:start] + inpt[end + 1:]
                inpt = result

        print(inpt)

    elif(line[0] == "Switch"):
        old = line[1]
        new = line[2]

        if(old in inpt):
            index = inpt.index(old)
            result = inpt.replace(inpt[index:len(old)], new)
            inpt = result

        print(inpt)

print(f"Ready for world tour! Planned stops: {inpt}")