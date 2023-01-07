inpt = input().split(", ")
words = []
for i in inpt:
    words.append(i)

counterToTheWolf = 0
for i in words:
    if(i == "wolf"):
        counterToTheWolf += 1
        break
    counterToTheWolf += 1

if(counterToTheWolf == len(words)):
    print("Please go away and stop eating my sheep")
if(counterToTheWolf < len(words)):
    print(f"Oi! Sheep number {len(words) - counterToTheWolf}! You are about to be eaten by a wolf!")