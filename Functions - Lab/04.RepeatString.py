def repeat(text, number):
    x = lambda a, b: a * b
    result = x(text, number)
    print(result)

text = input()
number = int(input())
print(repeat(text, number))