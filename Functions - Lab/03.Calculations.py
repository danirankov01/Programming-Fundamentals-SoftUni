def solve(oper, first, second):
    if(oper == "add"):
        return first + second
    elif(oper == "subtract"):
        return first - second
    elif(oper == "multiply"):
        return first * second
    elif(oper == "divide"):
        return int(first / second)

operator = input()
firstNumber = int(input())
secondNumber = int(input())

print(solve(operator, firstNumber, secondNumber))