number = int(input())
for i in range(1, number + 1):
    sum = 0
    saved = i
    while(i != 0):
        lastNumber = i % 10
        sum += lastNumber
        i //= 10
        if(i == 0):
            if(sum == 5 or sum == 7 or sum == 11):
                print(f"{saved} -> True")
            else:
                print(f"{saved} -> False")