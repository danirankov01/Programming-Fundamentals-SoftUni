K = int(input())
L = int(input())
M = int(input())
N = int(input())
 
 
listOne = []
listTwo = []
 
for k in range(K, 8+1):
    if k % 2 == 0:
        for l in range(9, L-1, -1):
            if l % 2 == 1:
                num = k * 10 + l
                listOne.append(num)
 
for m in range(M, 8+1):
    if m % 2 == 0:
        for n in range(9, N-1, -1):
            if n % 2 == 1:
                num = m * 10 + n
                listTwo.append(num)
 
print("listOne ", listOne)
print("listTwo ",  listTwo)
 
 
print()
print("++Comparing each number++")
print()
 
swapCounter = 0
for i in listOne:
    for j in listTwo:
        if swapCounter < 6:
            if i == j: print("Cannot change the same player.")
            else:
                print(i, " - ", j)
                swapCounter += 1