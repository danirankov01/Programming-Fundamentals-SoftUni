number = int(input())
totalSum = 0
for i in range(number):
    charachters = input()
    totalSum += ord(charachters)
print(f"The sum equals: {totalSum}")