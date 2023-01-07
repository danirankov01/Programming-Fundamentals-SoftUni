n = int(input())
positiveList = []
negativeList = []

for i in range(n):
    number = int(input())
    if(number >= 0):
        positiveList.append(number)
    else:
        negativeList.append(number)

print(positiveList)
print(negativeList)
print(f"Count of positives: {len(positiveList)}")
print(f"Sum of negatives: {sum(negativeList)}")