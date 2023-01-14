inpt = input().split(", ")
countOfBeggars = int(input())
list = []
result = []

for i in inpt:
    list.append(int(i))

beggar = 0
finishedBeggars = 0
if(countOfBeggars < len(list)):
    for i in range(countOfBeggars):
        currentBeggar = []
        for j in range(len(list)):
            if(beggar == j):
                currentBeggar.append(list[j])
                beggar += countOfBeggars
        result.append(sum(currentBeggar))
        finishedBeggars += 1
        beggar = finishedBeggars
    print(result)        
elif(countOfBeggars == len(list)):
    print(list)

elif(countOfBeggars > len(list)):
    difference = countOfBeggars - len(list)
    list.extend([0] * difference)
    print(list)