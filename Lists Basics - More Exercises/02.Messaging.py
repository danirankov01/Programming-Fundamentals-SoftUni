inpt = input().split()
message = input()
listNumbers = []
plusOne = 0
result = ""

for i in inpt:
    listNumbers.append(int(i))

for i in listNumbers:
    sum = 0
    while(i != 0):
        lastNumber = i % 10
        sum += lastNumber
        i //= 10
    if(len(message) >= sum + 1):
        result += message[sum + plusOne]
        plusOne += 1
    else:
        while(True):
            sum -= (len(message))
            if(len(message) >= sum + 1):
                break
        result += message[sum + plusOne]
        plusOne += 1
print(result)