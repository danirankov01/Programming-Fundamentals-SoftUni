n = int(input())
heroes = {}

for i in range(n):
    line = input().split()
    hero = line[0]

    hp = int(line[1])
    mp = int(line[2])

    heroes[hero] = heroes.get(hero, {'hp': hp, 'mp': mp})

while(True):
    commands = input().split(' - ')
    if(commands[0] == "End"): break

    if(commands[0] == "CastSpell"):
        hero, mpNeeded, spellName = commands[1], int(commands[2]), commands[3]

        if(heroes[hero]['mp'] >= mpNeeded):
            heroes[hero]['mp'] -= mpNeeded
            print(f"{hero} has successfully cast {spellName} and now has {heroes[hero]['mp']} MP!")
        
        else:
            print(f"{hero} does not have enough MP to cast {spellName}!")

    elif(commands[0] == "TakeDamage"):
        hero, damage, attacker = commands[1], int(commands[2]), commands[3]

        heroes[hero]['hp'] -= damage
        if(heroes[hero]['hp'] > 0):
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")

        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]

    elif(commands[0] == "Recharge"):
        hero, amount = commands[1], int(commands[2])

        if(heroes[hero]['mp'] + amount <= 200):
            heroes[hero]['mp'] += amount
            print(f"{hero} recharged for {amount} MP!")

        else:
           rechargedFor = 200 - heroes[hero]['mp']
           print(f"{hero} recharged for {rechargedFor} MP!")
           heroes[hero]['mp'] = 200

    elif(commands[0] == "Heal"):
        hero, amount = commands[1], int(commands[2])

        if(heroes[hero]['hp'] + amount <= 100):
            heroes[hero]['hp'] += amount
            print(f"{hero} healed for {amount} HP!")

        else:
            rechargedFor = 100 - heroes[hero]['hp']
            print(f"{hero} healed for {rechargedFor} HP!")
            heroes[hero]['hp'] = 100

for hero in heroes.keys():
    print(f"{hero}\n  HP: {heroes[hero]['hp']}\n  MP: {heroes[hero]['mp']}")