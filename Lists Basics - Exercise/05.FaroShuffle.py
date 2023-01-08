inpt = input().split()
shuffles = int(input())

deck = []
for i in inpt:
    deck.append(i)

first = deck[0]
last = deck[-1]

deck.remove(deck[0])
deck.remove(deck[-1])

newDeck = []
index = 0
result = deck
for i in range(shuffles):
    for j in result:
        if(index == len(deck) / 2):
            break
        tempDeck = []
        tempDeck.append(result[index + 2])
        tempDeck.append(result[index])
        newDeck += tempDeck
        index += 1
    result = newDeck
    newDeck = []
    index = 0

result.insert(0, first)
result.append(last)
print(result)