def tribonacci(number):
    listTribonacci = [1, 1, 2]
    if(number <= 3):
        for i in range(number):
            print(listTribonacci[i], end=" ")
        print()
    else:
        for i in range(len(listTribonacci), number):
            listTribonacci.append(listTribonacci[i - 1] 
            + listTribonacci[i - 2] + listTribonacci[i - 3])
        print(*listTribonacci, sep=" ")

number = int(input())
tribonacci(number)