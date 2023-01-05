n = int(input())
for i in range(n):
    number = int(input())
    if(number == 88):
        print("Hello")
        continue
    if(number == 86):
        print("How are you?")
        continue
    if(number < 88):
        print("GREAT!")
    else:
        print("Bye.")