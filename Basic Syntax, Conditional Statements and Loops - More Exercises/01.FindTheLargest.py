number = int(input())
listNumber = []
newNumber = ""
while(number != 0):
    lastNumber = number % 10
    listNumber.append(lastNumber)
    number //= 10
listNumber.sort()
for i in range(len(listNumber)):
    newNumber += str(listNumber[-i - 1])
print(newNumber)

# biggestNumber = int(str(number)[0])
# newNumber = ""
# for i in range(0, len(str(number))):
#     for j in range(1, len(str(number))):
#         if(biggestNumber >= number[i]):




# biggestNumber = number % 10
# number //= 10
# newNumber = ""

# while(number != 0):
#     lastNumber = number % 10
#     if(lastNumber <= biggestNumber):
#         newNumber += str(biggestNumber)
#         biggestNumber = lastNumber
#         if(len(str(number)) == 1):
#             newNumber += str(number)
#     else:
#         newNumber += str(lastNumber)
#         lastNumber = biggestNumber
#         if(len(str(number)) == 1):
#             newNumber += str(biggestNumber)
#     number //= 10
# print(newNumber)
