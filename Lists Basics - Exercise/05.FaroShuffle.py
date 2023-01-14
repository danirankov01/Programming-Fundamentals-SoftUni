inpt = input().split()
shuffles = int(input())

deck = []
for i in inpt:
    deck.append(i)

first = deck[0]
last = deck[-1]

deck.remove(deck[0])
deck.remove(deck[-1])

for i in range(shuffles):

    for j in range(len(deck)):
        if(j % 2 == 0):
            if(j + 3 <= len(deck)):
                deck[j], deck[j + 2] = deck[j + 2], deck[j]
                position = deck.index(deck[j])
                element = deck[j + 2]
                del deck[j + 2]
                deck.insert(position + 1, element)

deck.insert(0, first)
deck.append(last)
print(deck)