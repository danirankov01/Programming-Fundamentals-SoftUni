input = input()

x = 0
y = 0

for i in input:
    if(i == "R"):
        x += 1
    elif(i == "L"):
        x -= 1
    elif(i == "U"):
        y += 1
    else:
        y -= 1
print(f"({x}, {y})")