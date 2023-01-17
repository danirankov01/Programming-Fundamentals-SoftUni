peoples = int(input())
lift = list(map(int, input().split()))

for i in range(len(lift)):
    if(lift[i] >= 4):
        continue
    
    else:
        difference = 4 - lift[i]

        if(peoples - difference >= 0):
            peoples -= difference
            lift[i] += difference

            if(peoples == 0 and i == len(lift) - 1):
                print(*lift)
                exit()
        else:
            lift[i] += peoples
            print("The lift has empty spots!")
            print(*lift)
            exit()

print(f"There isn't enough space! {peoples} people in a queue!")
print(*lift)