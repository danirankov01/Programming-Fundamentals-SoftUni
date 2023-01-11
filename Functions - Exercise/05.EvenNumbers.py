def checkEven(number):
    if(number % 2 == 0):
        return True

number = input().split()
numbers = [int(x) for x in number]
result = filter(checkEven, numbers)
print(list(result))