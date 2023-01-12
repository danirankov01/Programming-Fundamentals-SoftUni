number = int(input())
wagons = [0] * number
while(True):
    command = input().split()
    if(command[0] == "End"):
        break
    if(command[0] == "add"):
        addNumber = int(command[1])
        wagons[-1] += addNumber
    elif(command[0] == "insert"):
        index = int(command[1])
        people = int(command[2])
        wagons[index] = people
    elif(command[0] == "leave"):
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
print(wagons)