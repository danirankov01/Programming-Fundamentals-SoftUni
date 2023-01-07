word = input()
result = []
for w in range(len(word)):
    if(ord(word[w]) >= 65 and ord(word[w]) <= 90):
        result.append(w)
print(result) 