# listNumbers = list(map(int, input().split()))
# sum = 0
# while(len(listNumbers) != 0):
#     index = int(input())
#     if(index < len(listNumbers)):
#         popped = listNumbers.pop(index)
#         sum += popped
#         for i in range(len(listNumbers)):
#             if(popped >= listNumbers[i]):
#                 listNumbers[i] += popped
#             else:
#                 listNumbers[i] -= popped

#     elif(index < 0):
#         popped = listNumbers[0]
#         sum += popped
#         listNumbers.pop(0)

#         for i in range(len(listNumbers)):
#             if(popped >= listNumbers[i]):
#                 listNumbers[i] += popped
#             else:
#                 listNumbers[i] -= popped

#         listNumbers.insert(0, listNumbers[-1])

#     elif(index >= len(listNumbers) - 1):
#         popped = listNumbers[-1]
#         sum += popped
#         listNumbers.pop(len(listNumbers) - 1)

#         for i in range(len(listNumbers)):
#             if(popped >= listNumbers[i]):
#                 listNumbers[i] += popped
#             else:
#                 listNumbers[i] -= popped

#         listNumbers.insert(len(listNumbers), listNumbers[0])

# print(sum)





sequence = list(map(int, input().split()))
sum = 0

while(len(sequence) != 0):
    indices = int(input())

    if(0 <= indices < len(sequence)):
        popped = sequence.pop(indices)
        sum += popped

        for i in range(len(sequence)):
            if(sequence[i] <= popped):
                sequence[i] += popped
            else:
                sequence[i] -= popped

    elif(indices < 0):
        popped = sequence.pop(0)
        sum += popped

        for i in range(len(sequence)):
            if(sequence[i] <= popped):
                sequence[i] += popped
            else:
                sequence[i] -= popped

        valueOfTheLast = sequence[-1]
        sequence.insert(0, valueOfTheLast)

    elif(indices > len(sequence) - 1):
        popped = sequence.pop(len(sequence) - 1)
        sum += popped

        for i in range(len(sequence)):
            if(sequence[i] <= popped):
                sequence[i] += popped
            else:
                sequence[i] -= popped

        valueOfTheFirst = sequence[0]
        sequence.append(valueOfTheFirst)

print(sum)