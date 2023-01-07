number = int(input())
isItPrime = False
if(number > 1):
    for i in range(2, number):
        if(number % i == 0):
            isItPrime = True
            break
    if(isItPrime):
        print(False)
    else:
        print(True)
else:
    print(False)