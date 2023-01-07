first = int(input())
second = int(input())

print(f"Before:\na = {first}\nb = {second}")

temp = first
first = second
second = temp

print(f"After:\na = {first}\nb = {second}")