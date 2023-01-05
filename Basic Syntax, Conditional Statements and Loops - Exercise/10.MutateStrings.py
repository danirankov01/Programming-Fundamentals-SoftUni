firstString = input()
secondString = input()

for i in range(len(firstString)):
    for j in range(i, len(secondString)):
        if(firstString[i] != secondString[j]):
            firstString = firstString[:i] + secondString[j] + firstString[i + 1:]
            print(firstString)
        break