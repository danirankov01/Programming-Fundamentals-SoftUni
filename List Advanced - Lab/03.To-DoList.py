result = []
while(True):
    line = input()
    if(line == "End"):
        break
    result.append(line)
sorting = sorted(result, key=lambda x: x[0])
result = []
for i in sorting:
    result.append(i[2:])
print(result)