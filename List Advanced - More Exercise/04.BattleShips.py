n = int(input())
result = []

for i in range(n):
    numbers = list(map(int, input().split()))
    result.append(numbers)    

commands = input().split()
destroyedShips = 0

for i in commands:
    splittedCommands = i.split("-")
    row = int(splittedCommands[0])
    col = int(splittedCommands[1])

    result[row][col] -= 1

    if(result[row][col] == 0):
        destroyedShips += 1

print(destroyedShips)