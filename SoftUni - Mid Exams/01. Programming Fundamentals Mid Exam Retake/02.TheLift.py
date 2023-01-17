# people = int(input())
# lift = list(map(int, input().split()))
# noMorePeople = False
# noEmptySpots = False
# for i in range(len(lift)):
#     if(lift[i] >= 4):
#         continue
#     else:
#         difference = 4 - lift[i]
#         if(people - difference >= 0):
#             people -= difference
#             lift[i] += difference
#             if(people == 0):
#                 noEmptySpots = True
#         else:
#             lift[i] += people
#             people = 0
            
#         if(people <= 0):
#             noMorePeople = True
#             break

# if(noMorePeople and not noEmptySpots):
#     print(f"The lift has empty spots!")
#     for i in lift:
#         print(i, end=" ")
#     print()

# elif(noMorePeople and noEmptySpots):
#     print(*lift, sep=" ")

# else:
#     print(f"There isn't enough space! {people} people in a queue!")
#     for i in lift:
#         print(i, end=" ")
#     print()




peoples = int(input())
lift = list(map(int, input().split()))

availableSpace = True
morePeople = True

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