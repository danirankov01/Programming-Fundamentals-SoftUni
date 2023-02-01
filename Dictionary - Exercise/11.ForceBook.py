force = {}

while(True):
    line = input()
    if(line == "Lumpawaroo"): break

    if("|" in line):
        line = line.split(" | ")
        side = line[0]
        user = line[1]

        if(side not in force):
            force[side] = [user]
        
        else:
            reached = False
            for k, v in force.items():
                if(user in v):
                    reached = True
                    break

            if(not reached):
                force[side].append(user)

    elif("->" in line):
        line = line.split(" -> ") 
        user = line[0]
        side = line[1]

        reached = False
        if(side not in force):
            for k, v in force.items():
                if(user in v):
                    reached = True
                    break

            if(not reached):
                force[side] = [user]
                print(f"{user} joins the {side} side!")
                continue 

        reached = False
        for k, v in force.items():
            if(user in v):
                force[k].remove(user)
                force[side].append(user)
                reached = True
                
        if(not reached):
            force[side].append(user)

for k, v in force.items():
    if(len(force[k]) != 0):
        print(f"Side: {k}, Members: {len(force[k])}")
        for key, value in force.items():
            print(f"! {value}") 