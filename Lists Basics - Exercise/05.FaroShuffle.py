line = list(input().split(' '))
shuffle = int(input())
 
first = line[0]
last = line[len(line) - 1]
 
line.remove(first)
line.remove(last)
 
for i in range(0, shuffle):
    A = line[:len(line)//2]
    B = line[len(line)//2:]
    line = []
 
    for j in range(0, len(A)):
        line.append(B[j])
        line.append(A[j])
 
line.insert(0, first)
line.append(last)
print(line)