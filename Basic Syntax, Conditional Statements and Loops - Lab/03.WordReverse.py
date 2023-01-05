word = input()
reversed = ""
for letters in range(len(word)):
    reversed += word[len(word) - letters - 1]
print(reversed)