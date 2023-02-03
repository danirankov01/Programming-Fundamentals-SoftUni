n = int(input())
automobiles = {}

for i in range(n):
    line = input().split('|')
    automobiles[line[0]] = {'mileage': int(line[1]), 'fuel': int(line[2])}

while(True):
    line = input().split(" : ")
    if(line[0] == "Stop"): break

    if(line[0] == "Drive"):
        car, distance, fuel = line[1], int(line[2]), int(line[3])

        if(automobiles[car]['fuel'] >= fuel):
            automobiles[car]['fuel'] -= fuel
            automobiles[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if(automobiles[car]['mileage'] >= 100000):
                print(f"Time to sell the {car}!")
                del automobiles[car]

        else:
            print("Not enough fuel to make that ride")

    
    elif(line[0] == "Refuel"):
        car, fuel = line[1], int(line[2])

        if(automobiles[car]['fuel'] + fuel <= 75):
            automobiles[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

        else:
            difference = 75 - automobiles[car]['fuel']
            automobiles[car]['fuel'] = 75
            print(f"{car} refueled with {difference} liters")

    
    elif(line[0] == "Revert"):
        car, kilometers = line[1], int(line[2])
        if(automobiles[car]['mileage'] - kilometers >= 10000):
            automobiles[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

        else:
            automobiles[car]['mileage'] = 10000

for k, v in automobiles.items():
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")