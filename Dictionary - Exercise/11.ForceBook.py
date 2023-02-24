sides = {}
all_users = []

while True:
    line = input()
    if line == "Lumpawaroo": break

    if '|' in line:
        splitted = line.split(' | ')

        force_side = splitted[0]
        force_user = splitted[1]

        all_sides = list(sides.keys())

        if force_user not in all_users and force_side not in all_sides:
            sides[force_side] = [force_user]
            all_users.append(force_user)

        elif force_user not in all_users:
            if force_side in all_sides:
                sides[force_side].append(force_user)
                        
            else:
                sides[force_side] = force_user
            all_users.append(force_user)

    elif '->' in line:
        splitted = line.split(' -> ')
        reached_user = False

        force_user = splitted[0]
        force_side = splitted[1]

        all_sides = list(sides.keys())

        if force_user not in all_users and force_side not in all_sides:
            sides[force_side] = [force_user]
            all_users.append(force_user)

        elif force_user in all_users:
            for k in sides.keys():
                if force_user in sides[k]:
                    sides[k].remove(force_user)
                    if force_side in all_sides:
                        sides[force_side].append(force_user)

                    else:
                        sides[force_side] = force_user
                    reached_user = True
                    break

        elif not reached_user:
            if force_side in all_sides:
                sides[force_side].append(force_user)
                        
            else:
                sides[force_side] = force_user
            all_users.append(force_user)

        print(f"{force_user} joins the {force_side} side!")


for k in sides.keys():
    if(len(sides[k]) != 0):
        print(f"Side: {k}, Members: {len(sides[k])}")
    for v in range(len(sides[k])):
        print(f"! {sides[k][v]}")


# d = {"name" : []}