inpt = list(map(int, input().split()))
factor = int(input())

employeeHappiness = [factor * x for x in inpt]
average = sum(employeeHappiness) / len(employeeHappiness)
filtered = filter(lambda medium: medium >= average, employeeHappiness)
filteredLengthList = list(filtered)

if(len(filteredLengthList) >= len(employeeHappiness) / 2):
    print(f"Score: {len(filteredLengthList)}/{len(employeeHappiness)}. Employees are happy!")
else:
    print(f"Score: {len(filteredLengthList)}/{len(employeeHappiness)}. Employees are not happy!")