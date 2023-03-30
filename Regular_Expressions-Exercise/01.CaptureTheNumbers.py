import re

pattern = r'\d+'
numbers = []

while True:
    text = input()
    if text:
        number = re.findall(pattern, text)
        for i in number:
            numbers.append(i)
    else:
        break

print(*numbers)