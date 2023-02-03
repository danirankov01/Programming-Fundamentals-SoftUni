import re

text = input()
regex = r"([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
matches = re.findall(regex, text)
mirror = False

if(matches):
    print(f"{len(matches)} word pairs found!")

else:
    print("No word pairs found!")

mirrorWords = []

for i in range(len(matches)):
    if(matches[i][1] == matches[i][4][::-1]):
        mirrorWords.append(matches[i][1])
        mirrorWords.append(matches[i][4])

oneTime = 0

for i in range(0, len(mirrorWords), 2):
    mirror = True
    if(oneTime == 0):
        oneTime += 1
        print("The mirror words are:")

    if(i + 2 < len(mirrorWords)):
        print(f"{mirrorWords[i]} <=> {mirrorWords[i + 1]}", end=", ")
    else:
        print(f"{mirrorWords[i]} <=> {mirrorWords[i + 1]}")

if(not mirror):
    print("No mirror words!")