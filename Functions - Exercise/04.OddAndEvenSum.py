def oddAndEvenSum(number):
    oddSum = 0
    evenSum = 0
    while(number != 0):
        lastDigit = number % 10
        if(lastDigit % 2 == 0):
            evenSum += lastDigit
        else:
            oddSum += lastDigit
        number //= 10
    print(f"Odd sum = {oddSum}, Even sum = {evenSum}")

number = int(input())
oddAndEvenSum(number)
