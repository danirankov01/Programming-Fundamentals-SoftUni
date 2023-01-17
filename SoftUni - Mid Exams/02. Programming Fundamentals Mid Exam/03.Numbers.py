list = list(map(int, input().split()))
average = sum(list) / len(list)

result = []

for i in list:
    if(i > average):
        result.append(i)

result.sort()
counter = len(result)

if(len(result) != 0):
    for i in range(5):

        print(result[-i - 1],end=" ")
        counter -= 1

        if(counter == 0):
            print()
            break
else:
    print("No")



# list = [-10, 5, 50, 50, 51, 60, 61]
# for i in range(5):
#     print(list[-i - 1], end=" ")