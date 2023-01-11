def chars(first, second):
    result = []
    for i in range(ord(first) + 1, ord(second)):
        result.append(chr(i))
    print(*result)

firstChar = input()
secondChar = input()
chars(firstChar, secondChar)