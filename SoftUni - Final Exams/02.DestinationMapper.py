import re

text = input()
regex = r"(=|\/)([A-Z][A-Za-z]{2,})(=|\/)"
match = re.findall(regex, text)

result = []
travelPoints = 0

for i in match:
    if(i[0] == i[2]):
        result.append(i[1])
        travelPoints += len(i[1])

print("Destinations: ", end="")
print(*result, sep=", ")
print(f"Travel Points: {travelPoints}")