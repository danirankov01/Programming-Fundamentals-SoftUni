employee = []
for i in range(3):
    receptionist = int(input())
    employee.append(receptionist)

students = int(input())
hours = 0

while(students > 0):
    students -= sum(employee)
    hours += 1

    if(hours % 4 == 0):
        hours += 1

print(f"Time needed: {hours}h.")
