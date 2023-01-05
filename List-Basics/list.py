#########4444444444########

# numbers = input().split(",")
# index = int(input())
# listNumbers = [int(x) for x in numbers]
# result = []
# for i in range(len(listNumbers)):
#     if(index <= len(listNumbers)):
#         if(index > i):
#             result.append(listNumbers[i])
#             listNumbers[i] = " "
#         else:
#             break
#     else:
#         while(index >= len(listNumbers)):
#             index -= len(listNumbers)
#         index -= 1
#         for j in range(len(listNumbers)):
#             if(index >= j):
#                 result.append(listNumbers[j])
#                 listNumbers[j] = " "
#         break
# for i in range(len(listNumbers)):
#     if(listNumbers[0] == " "):
#         listNumbers.remove(" ")
#     else:
#         break
# for i in result:
#     listNumbers.append(i)
# print(*listNumbers,sep=",")
    

# listN = [5,3,2,1]
# for i in range(len(listN)):
#     if(i <= 2):
#         listN.pop(i)




#########8888888888########


# number = input().split(",")
# listNumbers = [int(x) for x in number]
# sum = 0

# below = []
# above = []

# for i in listNumbers:
#     sum += i

# averge = sum / len(listNumbers)
# rounded = round(averge,2)

# for i in listNumbers:
#     if(i == rounded):
#         continue
#     if(i < rounded):
#         below.append(i)
#     else:
#         above.append(i)
# print(f"avg: {rounded}")
# print("below: ",end="")
# print(*below,sep=",")
# print("above: ",end="")
# print(*above,sep=",")







#############10 10 10 10 10 10 10 10 10 10 10#################


# number = input().split(",")
# listNumbers = [int(x) for x in number]
# listNumbers.sort()

# result = []

# for i in range(len(listNumbers)):
#     for j in range(i + 1, len(listNumbers)):
#         if(listNumbers[i] < listNumbers[j]):
#             for k in range(listNumbers[i] + 1, listNumbers[j]):
#                 result.append(listNumbers[i] + 1)
#                 listNumbers[i] += 1
#         else:
#             if(listNumbers[i] > listNumbers[j]):
#                 listNumbers[j] += listNumbers[i]
#                 result.append(listNumbers[j])
#             else:
#                 listNumbers[i] == listNumbers[j]
#                 listNumbers[j] += 1
#                 result.append(listNumbers[j])
#         break
# print(*result)




inpt = input().split(",")
numbers = [int(x) for x in inpt]

result = ""
for i in range(1, len(numbers) + 1):
    if(i not in numbers):
        result += str(i) + ","
        
result = result.removesuffix(",")
print(result)






#####PRIME FACTORS LOOPS 12###########

# number = int(input())

# while(number % 2 == 0):
#     number //= 2
#     print(2)
# while(number % 3 == 0):
#     number //= 3
#     print(3)
# while(number % 5 == 0):
#     number //= 5
#     print(5)
# while(number % 7 == 0):
#     number //= 7
#     print(7)
