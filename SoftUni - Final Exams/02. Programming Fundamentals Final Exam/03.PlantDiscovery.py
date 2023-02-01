# from pydoc import stripid


# n = int(input())
# plants = {}

# for i in range(n):
#     line = input().split("<->")
    
#     plant = line[0]
#     rarity = int(line[1])

#     if(plant not in plants):
#         plants[plant] = rarity

#     else:
#         plants[plant] = rarity

# ratings = {}

# while(True):
#     line = input().split(":")

#     if(line[0] == "Exhibition"): break

#     if(line[0] == "Rate"):
#         splitted = line[1].split(" - ")
        
#         plant = splitted[0].strip()
#         rating = int(splitted[1])

#         if(plant in plants):
#             if(plant not in ratings):
#                 ratings[plant] = [rating]

#             else:
#                 ratings[plant].append(rating)
        
#         else:
#             print("error")

#     elif(line[0] == "Update"):
#         splitted = line[1].split(" - ")

#         plant = splitted[0].strip()
#         newRarity = int(splitted[1])

#         if(plant in plants):
#             plants[plant] = newRarity
        
#         else:
#             print("error")

#     elif(line[0] == "Reset"):
#         plant = line[1].strip()

#         if(plant in plants):
#             ratings[plant] = []

#         else:
#             print("error")

# print("Plants for the exhibition:")
# for key, value in plants.items():
#     print(f"- {key}; Rarity: {value}; Rating:", end=" ")
    
#     for k, v in ratings.items():
#         if(k == key):
#             if(len(ratings[k]) == 0):
#                 print("0.00")
#                 break
            
#             else:
#                 print(f"{sum(ratings[k]) / len(ratings[k]):.2f}")
#                 break






from pydoc import stripid

n = int(input())
plants = {}

for i in range(n):
    line = input().split("<->")
    plants[line[0]] = int(line[1])

ratings = {}

while(True):
    line = input().split(":")
    if(line[0] == "Exhibition"): break

    splitted = line[1].split(" - ")
    plant = splitted[0]

    if(plant not in plants):
        print("error")
        continue

    if(line[0] == "Rate"):
        rating = int(splitted[1])

        if(plant in ratings):
            ratings[plant].append(rating)
            continue
        ratings[plant] = [rating]

    elif(line[0] == "Update"):
        newRarity = int(splitted[1])

        plants[plant] = newRarity

    elif(line[0] == "Reset"):
        ratings[plant] = []

print("Plants for the exhibition:")
for key, value in plants.items():
    print(f"- {key}; Rarity: {value}; Rating: ", end="")

    for k, v in ratings.items():
        if(k == key):
            if(len(ratings[k]) != 0):
                print(f"{sum(ratings[k]) / len(ratings[k]):.2f}")
            else:
                print("0.00")

# l = []
# print(sum(l) / len(l))