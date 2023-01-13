version = input().split(".")
versionZero = int(version[0])
versionOne = int(version[1])
versionTwo = int(version[2])

versionTwo += 1
if(versionTwo > 9):
    versionTwo = 0
    versionOne += 1
    if(versionOne > 9):
        versionOne = 0
        versionZero += 1
print(f"{versionZero}.{versionOne}.{versionTwo}")