word = input().lower()
result = 0

sand = "sand"
water = "water"
fish = "fish"
sun = "sun"

sandNumber = 0
waterNumber = 0
fishNumber = 0
sunNumber = 0

for i in sand: sandNumber += ord(i)
for i in water: waterNumber += ord(i)
for i in fish: fishNumber += ord(i)
for i in sun: sunNumber += ord(i)

counter = 0

for i in word:
    if(i == sand[0]):
        if(word[counter:counter + 4] == "sand"):
            result += 1
        elif(word[counter:counter + 3] == "sun"):
            result += 1
    if(i == water[0]):
        if(word[counter:counter + 5] == "water"):
            result += 1
    if(i == fish[0]):
        if(word[counter:counter + 4]):
            result += 1

    counter += 1
print(result)

# strin = "dani"

# print(strin[0:3])