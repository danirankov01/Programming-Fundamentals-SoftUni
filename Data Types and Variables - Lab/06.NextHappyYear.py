number = int(input()) + 1
saved = number
while(number != 0):
    lastNumber = number % 10
    number //= 10
    if(str(lastNumber) in str(number)):
        saved += 1
        number = saved
    if(number == 0):
        print(saved)