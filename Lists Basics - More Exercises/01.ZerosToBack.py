inpt = input().split(", ")
listNumbers = []
listZeros = []
for i in inpt:
    if(i == '0'):
        listZeros.append(int(i))
    else:
        listNumbers.append(int(i))
listNumbers.extend(listZeros)
print(listNumbers)