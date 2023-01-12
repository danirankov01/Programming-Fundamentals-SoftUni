line = input().split()
palindrome = input()
words = [x for x in line]
index = 0
for i in range(len(words)):
    isPalindrome = True
    for j in range(len(words[index])):
        if(words[index][j] != words[index][-j - 1]):
            isPalindrome = False
            break
    if(isPalindrome == False):
        words.pop(index)
        index -= 1
    index += 1

counter = 0
for i in words:
    if(i == palindrome):
        counter += 1

print(words)
print(f"Found palindrome {counter} times")