def result(a, b, c):
    listNumbers = [a, b, c]
    if(0 in listNumbers):
        print("zero")
        exit()

    isPositive = True
    for i in listNumbers:
        if(isPositive and i < 0):
            isPositive = False
            continue
        if(isPositive == False and i < 0):
            isPositive = True
    if(isPositive):
        print("positive")
    else:
        print("negative")

first = int(input())
second = int(input())
third = int(input())
result(first, second, third)