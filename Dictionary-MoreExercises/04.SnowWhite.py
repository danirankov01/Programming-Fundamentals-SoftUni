dwarfs = {}

while True:
    line = input()
    if line == "Once upon a time": break

    line = line.split(' <:> ')
    name, hat_color, physics = line[0], line[1], int(line[2])

    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
        dwarfs[hat_color][name] = physics

    elif name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = physics

    elif physics > dwarfs[hat_color][name]:
            dwarfs[hat_color][name] = physics
    
result = []

for hat in dwarfs:
    for name, physic in dwarfs[hat].items():
        result.append({'length': len(dwarfs[hat]), 'name': name, 'physic': physic, 'hat_color': hat})
        
for res in sorted(result, key=lambda x: (-x['physic'], -x['length'])):
    print(f"({res['hat_color']}) {res['name']} <-> {res['physic']}")