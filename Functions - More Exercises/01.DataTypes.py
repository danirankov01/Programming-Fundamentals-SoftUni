def operations(inpt, data):
    if(inpt == "int"):
        data = int(data)
        data *= 2
        print(data)
    elif(inpt == "real"):
        data = float(data)
        data *= 1.5
        print(f"{data:.2f}")
    elif(inpt == "string"):
        dollar = "$"
        dollar += data + dollar
        print(dollar)

operation = input()
numberOrString = input()
operations(operation, numberOrString)