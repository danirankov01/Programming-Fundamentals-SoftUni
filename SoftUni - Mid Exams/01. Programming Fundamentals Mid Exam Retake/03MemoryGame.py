elements = list(map(str, input().split()))
moves = 0
inputs = 0

while(True):

    if(inputs != 0):
        if(len(elements) == 0):
            print(f"You have won in {moves} turns!")
            break

    inputs += 1

    indices = input().split()

    if(indices[0] == "end"):
        print("Sorry you lose :(")
        print(*elements, sep=" ")
        break

    firstIndex = indices[0]
    secondIndex = indices[1]

    if(firstIndex.isdigit()): firstIndex = int(firstIndex)
    if(secondIndex.isdigit()): secondIndex = int(secondIndex)

    # if(not firstIndex.isdigit()):
    if(str(firstIndex)[0] == "-"): firstIndex = int(firstIndex)
    
    # if(not secondIndex.isdigit()):
    if(str(secondIndex)[0] == "-"): secondIndex = int(secondIndex)


    if(firstIndex == secondIndex or \
        firstIndex < 0 or firstIndex > len(elements) or\
        secondIndex < 0 or secondIndex > len(elements)):
        
        moves += 1
        middle = int(len(elements) / 2)
        elements.insert(middle, f"{-moves}a")
        elements.insert(middle + 1, f"{-moves}a")
        print("Invalid input! Adding additional elements to the board")


    elif(firstIndex >= 0 or firstIndex < len(elements) and secondIndex >= 0 or secondIndex < len(elements)):
        if(elements[firstIndex] == elements[secondIndex]):

            poppedElement = elements[firstIndex]
            minimum = min(firstIndex, secondIndex)
            moves += 1

            if(minimum == firstIndex):
                elements.pop(firstIndex)
                elements.pop(secondIndex - 1)
            else:
                elements.pop(secondIndex)
                elements.pop(firstIndex - 1)

            print(f"Congrats! You have found matching elements - {poppedElement}!")

        else:
            print("Try again!")
            moves += 1


# seq = [1, 2, 3, 5, 6]
# middle = int(len(seq) / 2)

# seq.insert(middle, 4)
# print(seq)