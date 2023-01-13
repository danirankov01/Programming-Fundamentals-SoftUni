message = input().split()
output = ""

for i in message:
    firstLetter = ""
    index = 0
    for j in i:
        if(ord(j) >= 48 and ord(j) <= 57):
            firstLetter += j
            index += 1
        else:
            listTheRest = list(i)
            temp = listTheRest[index]
            listTheRest[index] = listTheRest[-1]
            listTheRest[-1] = temp
            rest = "".join(listTheRest[index:])
            output += chr(int(firstLetter)) + rest + ' '
            break
print(output)