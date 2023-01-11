def factorial(first, second):
    factorialFirst = 1
    factorialSecond = 1

    for i in range(1, first + 1):
        factorialFirst *= i
    for i in range(1, second + 1):
        factorialSecond *= i

    print(f"{factorialFirst / factorialSecond:.2f}") 

first = int(input())
second = int(input())
factorial(first, second)