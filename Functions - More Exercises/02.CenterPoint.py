def coordinates(X1, Y1, X2, Y2):
    firstDistance = (X1, X2)
    result1 = min(abs(x) for x in firstDistance)
    secondDistance = (Y1, Y2)
    result2 = min(abs(x) for x in secondDistance)
    if(result1 != result2):
        print(f"({result1}, {result1})")
    else:
        print(f"({result1})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

coordinates(x1, y1, x2, y2)