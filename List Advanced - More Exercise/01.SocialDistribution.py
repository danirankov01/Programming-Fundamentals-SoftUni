population = list(map(int, input().split(", ")))
minimumWealth = int(input())

sumOfPopulation = sum(population)
lenOfPopulation = len(population)

index = 0

if(sumOfPopulation / len(population) == minimumWealth):
    population = []
    population = [minimumWealth] * lenOfPopulation
    print(population)

elif(sumOfPopulation / len(population) < minimumWealth):
    print("No equal distribution possible")

else:
    for i in range(len(population)):
        if(population[i] >= minimumWealth):
            break
        difference = minimumWealth - population[i]
        if(population[-index - 1] - difference >= minimumWealth):
            population[-index - 1] -= difference
            population[i] += difference
        else:
            index += 1
            population[-index - 1] -= difference
            population[i] += difference
    print(population)