def perfect(number):
    sum = 0
    saveNumber = number
    for i in range(1, int(number / 2) + 1):
        if(saveNumber % i == 0):
            sum += i
    if(sum == saveNumber):
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
if(number > 1):
    print(perfect(number))
else:
    print("It's not so perfect.")