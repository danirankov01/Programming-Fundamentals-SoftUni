def loadingBar(number):
    output = ""
    percent = int(number / 10) * "%"
    dots = (10 - int(number / 10)) * "."
    percentAndDots = ""
    percentAndDots += percent + dots
    output += str(number) + "% " + "[" + percentAndDots + "]"
    print(output)
    print("Still loading...")

number = int(input())
if(number != 100):
    loadingBar(number)
else:
    print("100% Complete!")
    print("[%%%%%%%%%%]")