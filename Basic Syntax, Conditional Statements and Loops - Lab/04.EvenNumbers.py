number = int(input())
counter = 0
for i in range(number):
    numbers = int(input())
    if(numbers % 2 == 0):
        counter += 1
    else:
        print(f"{numbers} is odd!")
        break
if(counter == number):
    print("All numbers are even.")