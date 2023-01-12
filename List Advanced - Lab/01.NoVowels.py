text = list(map(list, input().lower()))
result = ""
for i in text:
    if(i != "a"):
        result.append(i)
print(*result, end="")