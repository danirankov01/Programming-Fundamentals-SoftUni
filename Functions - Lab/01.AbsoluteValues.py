def absolute(number):
    result = [abs(x) for x in number]
    return result

numbers = list(map(float, input().split()))
print(absolute(numbers))