def addAndSubtract(a, b, c):
    def sumNumbers():
        return a + b
    def subtract():
        return sumNumbers() - c
    return subtract()

a = int(input())
b = int(input())
c = int(input())

print(addAndSubtract(a, b, c))