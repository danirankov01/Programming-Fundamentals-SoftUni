names = input().split(", ")
list = [x for x in names]

sortedList = sorted(list, key=lambda x: (-len(x), x))
print(sortedList)