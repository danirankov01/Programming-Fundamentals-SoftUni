courses = {}

while True:
    line = input().split(':')
    if line[0] == "end of contests": break

    course, password = line[0], line[1]    
    courses[course] = password

participants = {}

while True:
    line = input().split('=>')
    if line[0] == "end of submissions": break

    contest, password, username, points = line[0], line[1], line[2], int(line[3])

    if contest in courses:
        if password == courses[contest]:

            if username not in participants:
                participants[username] = {}
                participants[username][contest] = points

            else:
                if contest not in participants[username]:
                    participants[username][contest] = points

                else:
                    if points > participants[username][contest]:
                        participants[username][contest] = points


bestUser = ""
bestPoints = -1

for k in participants.keys():
    currentPoints = 0
    for c, p in participants[k].items():
        currentPoints += p

    if currentPoints > bestPoints:
        bestPoints = currentPoints
        bestUser = k

print(f"Best candidate is {bestUser} with total {bestPoints} points.\nRanking:")
sorted_participants = sorted(participants.items(), key=lambda n: n[0])

for k in sorted_participants:
    print(k[0])
    for c, p in sorted(k[1].items(), key=lambda points: -points[1]):
        print(f"#  {c} -> {p}")
