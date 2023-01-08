factor = int(input())
count = int(input())
result = []

if(factor > 0):
    for i in range(1, count + 1):
        if(len(result) == 0):
            result.append(factor)
        else:
            result.append(factor * i)
print(result)