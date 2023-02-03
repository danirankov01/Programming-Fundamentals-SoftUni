message = input()

while(True):
    line = input().split(":|:")

    if(line[0] == "Reveal"): break

    if(line[0] == "InsertSpace"):
        index = int(line[1])
        message = message[:index] + " " + message[index:]
        print(message)

    elif(line[0] == "Reverse"):
        substring = line[1]

        if(substring in message):
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)

        else:
            print("error")

    elif(line[0] == "ChangeAll"):
        substring = line[1]
        replacement = line[2]

        if(substring in message):
            message = message.replace(substring, replacement)
            print(message)

print(f"You have a new text message: {message}")