sequence = list(map(int, input().split()))

while(True):

    line = input().split()

    if(line[0] == "End"): 
        print(*sequence, sep="|")
        break

    command = line[0]

    if(command == "Shoot"):

        index = int(line[1])
        power = int(line[2])

        if(0 <= index < len(sequence)):

            if(sequence[index] - power > 0):
                sequence[index] -= power

            else:
                sequence.pop(index)

    elif(command == "Add"):

        index = int(line[1])
        value = int(line[2])

        if(0 <= index <= len(sequence)):
            sequence.insert(index, value)

        else:
            print("Invalid placement!")

    elif(command == "Strike"):

        index = int(line[1])
        radius = int(line[2])

        if(0 <= index < len(sequence)):

            if(index - radius >= 0 and index + radius < len(sequence)):

                # start = index - radius

                # for i in range(index - radius, index + radius + 1):
                    
                #     sequence.pop(start)

                start = index - radius
                end = index + radius + 1

                for i in range(start, end):
                    sequence.pop(start)

            else:

                print("Strike missed!")