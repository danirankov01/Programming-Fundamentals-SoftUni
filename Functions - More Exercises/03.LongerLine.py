from math import floor

def check_center(sum1,sum2,sum3,sum4):
    firstCalculation = sum1 + sum2
    secondCalculation = sum3 + sum4
    if firstCalculation > secondCalculation:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif firstCalculation < secondCalculation:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"
    else:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"


x1, x2, y1, y2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))
x3, x4, y3, y4 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))

sumX = floor(abs(x1) + abs(x2))
sumX2 = floor(abs(x3) + abs(x4))
sumY = floor(abs(y1) + abs(y2))
sumY2 = floor(abs(y3) + abs(y4))

print(check_center(sumX, sumY, sumX2, sumY2))