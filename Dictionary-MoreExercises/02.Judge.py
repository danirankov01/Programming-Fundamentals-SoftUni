participants = {}
individual = {}

while True:
    line = input().split(' -> ')
    if line[0] == "no more time": break

    username, contest, points = line[0], line[1], int(line[2])

    if contest not in participants:
        participants[contest] = {}
        participants[contest][username] = points
        individual[username] = points

    else:
        for k in {k1 for k1 in participants[contest]}:
            if username not in k:
                participants[contest][username] = points
                individual[username] = 0

            else:
                if points > participants[contest][username]:
                    participants[contest][username] = points
                    individual[username] = points
                    break

            individual[username] += points
            break

for k, v in participants.items():
    print(f"{k}: {len(participants[k])} participants")
    counter = 1

    for k1, v1, in sorted(v.items(), key=lambda x: (-x[1], x[0])):
        print(f"{counter}. {k1} <::> {v1}")
        counter += 1

print("Individual standings:")
