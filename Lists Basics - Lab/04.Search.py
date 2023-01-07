n = int(input())
word = input()

list = []
for i in range(n):
    sentences = input()
    list.append(sentences)

result = []
for i in list:
    if (word in i):
        result.append(i)

print(list)
print(result)