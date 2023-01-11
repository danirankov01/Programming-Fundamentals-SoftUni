def minimum(list):
    return min(list)
def maximum(list):
    return max(list)
def sumAll(list):
    return sum(list)

numbers = list(map(int, input().split()))
print("The minimum number is", minimum(numbers))
print("The maximum number is", maximum(numbers))
print("The sum number is:", sumAll(numbers))