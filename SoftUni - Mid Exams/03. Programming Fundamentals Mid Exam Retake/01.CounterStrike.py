energy = int(input())
wins = 0

while(True):
    line = input().split()
    if(line[0] == "End" and line[1] == \
        "of" and line[2] == "battle"):

        print(f"Won battles: {wins}. Energy left: {energy}")
        break
        
    distance = int(line[0])

    if(energy - distance >= 0):
        energy -= distance
        wins += 1

        if(wins % 3 == 0):
            energy += wins

    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break