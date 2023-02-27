n = int(input())
dragons = {}

for i in range(n):
    line = input().split()

    color, name, damage, health, armor = \
        line[0], line[1], line[2], line[3], line[4]
    
    if damage == 'null': damage = 45
    if health == 'null': health = 250
    if armor == 'null': armor = 10

    if color not in dragons:
        dragons[color] = {}
        dragons[color][name] = [damage, health, armor]

    else:
        dragons[color][name] = [damage, health, armor]

stats = []
for k, v in dragons.items():
    avg = [0, 0, 0]
    for k1, v1 in v.items():
        for i in range(3):
            avg[i] += int(v1[i])
    for j in range(3):
        avg[j] /= len(dragons[k])
    stats.append(f"{k}::({avg[0]:.2f}/{avg[1]:.2f}/{avg[2]:.2f})")

index = 0

for k, v in dragons.items():
    print(stats[index])
    for k1, v1 in sorted(v.items(), key=lambda x: (x[0])):
        print(f"-{k1} -> damage: {v1[0]}, health: {v1[1]}, armor: {v1[2]}")
    index += 1