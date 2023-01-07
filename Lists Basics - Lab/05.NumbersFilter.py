n = int(input())
numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()
result = []

if(command == "even"):
    for i in numbers:
        if(i % 2 == 0):
            result.append(i)
elif(command == "odd"):
    for i in numbers:
        if(i % 2 != 0):
            result.append(i)
elif(command == "positive"):
    for i in numbers:
        if(i >= 0):
            result.append(i)
else:
    for i in numbers:
        if(i < 0):
            result.append(i)

print(result)