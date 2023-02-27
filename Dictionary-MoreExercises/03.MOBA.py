players_pool = {}

while True:
    line = input()
    if line == "Season end": break

    if '->' in line:
        splitted = line.split(' -> ')
        player, position, skill = splitted[0], splitted[1], int(splitted[2])

        if player not in players_pool:
            players_pool[player] = {}
            players_pool[player][position] = skill

        else:
            d = {k1: v1 for k1, v1 in players_pool[player].items()}
            if position in d:
                if players_pool[player][position] < skill:
                    players_pool[player][position] = skill

            else:
                players_pool[player][position] = skill

    elif 'vs' in line:
        splitted = line.split(' vs ')
        first_player, second_player = splitted[0], splitted[1]

        if first_player in players_pool and second_player in players_pool:
            f = {k1: v1 for k1, v1 in players_pool[first_player].items()}
            s = {k1: v1 for k1, v1 in players_pool[second_player].items()}
            
            positions = 0
            total_poinst_first = 0
            total_poinst_second = 0

            for k, v in f.items():
                if k in s:
                    total_poinst_first += v
                    total_poinst_second += s[k]
                    positions += 1


            if positions > 0:
                if total_poinst_first > total_poinst_second:
                    del players_pool[second_player]
                elif total_poinst_first < total_poinst_second:
                    del players_pool[first_player]

name_points = {}
peoples = []

for k, v in players_pool.items():
    for k1, v1 in v.items():
        if k not in name_points:
            name_points[k] = v1
            peoples.append(k)
        
        else:
            name_points[k] += v1

result_dict = {}
for i in peoples:
    result_dict[i] = {}
    for k, v in players_pool[i].items():
        result_dict[i][k] = v


for k, v in sorted(name_points.items(), key=lambda x: (-x[1])):
    print(f"{k}: {v} skill")
    for k1, v1 in sorted(result_dict[k].items(), key=lambda y: (-y[1])):
        print(f"- {k1} <::> {v1}")