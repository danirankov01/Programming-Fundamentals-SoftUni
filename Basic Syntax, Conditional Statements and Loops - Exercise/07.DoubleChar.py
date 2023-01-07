while(True):
    newWord = ""
    command = input()
    if(command == "SoftUni"):
        continue
    if(command == "End"):
        break
    for i in command:
        newWord += i + i
    print(newWord)