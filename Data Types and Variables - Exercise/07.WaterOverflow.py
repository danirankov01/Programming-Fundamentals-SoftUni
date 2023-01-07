n = int(input())
capacity = 255
result = 0
for i in range(n):
    litersOfWater = int(input())
    if(capacity >= litersOfWater):
        capacity -= litersOfWater
        result += litersOfWater
    else:
        print("Insufficient capacity!")
print(result)