import re

n = int(input())
barcodes = [input() for x in range(n)]

regex = r"^(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})$"

for i in barcodes:
    group = ""
    matches = re.findall(regex, i)
    if(len(matches) != 0):
        for i in range(len(matches[0][1])):
            if(ord(matches[0][1][i]) >= 48 and ord(matches[0][1][i]) <= 57):
                group += str(matches[0][1][i])

        if(len(group) != 0):
            print(f"Product group: {group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")