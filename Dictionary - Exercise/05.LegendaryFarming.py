materials = {}
junk = {}

materials['shards'] = 0
materials['fragments'] = 0
materials['motes'] = 0

breaked = False

while(not breaked):
    inpt = input().split()

    for i in range(len(inpt)):
        if(i % 2 == 0):
            quantity = int(inpt[i])

        else:
            material = inpt[i].lower()
            
            if(material == "shards" or \
                material == "fragments" or \
                    material == "motes"):
                materials[material] += quantity

                if(materials[material] >= 250):
                    if(material == "shards"):
                        print("Shadowmourne obtained!")
                    elif(material == "fragments"):
                        print("Valanyr obtained!")
                    elif(material == "motes"):
                        print("Dragonwrath obtained!")

                    materials[material] -= 250
                    breaked = True
                    break
                    
            else:
                if(material not in junk):
                    junk[material] = quantity
                else:
                    junk[material] += quantity

for k, v in materials.items():
    print(f"{k}: {v}")
for k, v in junk.items():
    print(f"{k}: {v}")