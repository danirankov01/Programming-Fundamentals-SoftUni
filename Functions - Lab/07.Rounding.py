def rounding(number):
    result = [round(x) for x in number]
    return result
    

numbers = list(map(float, input().split()))
print(rounding(numbers))