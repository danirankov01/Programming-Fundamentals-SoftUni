result = []
while(True):
    line = input()
    if(line == "End"):
        break
    result.append(line)

sorting = sorted(result, key=lambda x: x[0])
result = []
wait = []

for i in sorting:
    if(i[:2] == "10"):
        wait.append(i[3:])
        continue
    result.append(i[2:])

if(len(wait) != 0):
    result.append(wait[0])
print(result)