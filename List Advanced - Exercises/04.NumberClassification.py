list = list(map(int, input().split(", ")))
positive = [x for x in list if x > -1]
negative = [x for x in list if x < 0]
even = [x for x in list if x % 2 == 0]
odd = [x for x in list if x % 2 != 0]

if(len(positive) > 0): print("Positive:", ", ".join(map(str, positive)))
else: print("Positive:")

if(len(negative) > 0): print("Negative:", ", ".join(map(str, negative)))
else: print("Negative:")

if(len(even) > 0): print("Even:",", ".join(map(str, even)))
else: print("Even:")

if(len(odd) > 0): print("Odd:",", ".join(map(str, odd)))
else: print("Odd:")