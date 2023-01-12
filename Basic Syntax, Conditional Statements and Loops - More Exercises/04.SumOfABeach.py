# word = input().lower()
# result = 0

# sand = "sand"
# water = "water"
# fish = "fish"
# sun = "sun"

# counter = 0

# for i in word:
#     if(i == sand[0]):
#         if(word[counter:counter + 4] == "sand"):
#             result += 1
#         elif(word[counter:counter + 3] == "sun"):
#             result += 1
#     if(i == water[0]):
#         if(word[counter:counter + 5] == "water"):
#             result += 1
#     if(i == fish[0]):
#         if(word[counter:counter + 4]):
#             result += 1

#     counter += 1
# print(result)


word = input().lower()
counter = 0

counter += word.find("sand")
counter += word.find("water")
counter += word.find("fish")
counter += word.find("sun")

print(counter)