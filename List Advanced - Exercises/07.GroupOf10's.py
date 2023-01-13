numbers = list(map(int, input().split(", ")))
group = 10
start = -1
checkList = 0
biggest = max(numbers)
while(len(numbers) > 0):
    filtered = filter(lambda gr: gr <= group and gr > start, numbers)
    checkList = list(filtered)
    print(f"Group of {group}'s: {checkList}")
    if(biggest in checkList):
        break
    group += 10
    if(start == -1):
        start += 11
    else:
        start += 10