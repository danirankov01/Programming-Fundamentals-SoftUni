numberOfRooms = int(input())
freeChairs = 0
game = True
for i in range(1, numberOfRooms + 1):
    room = input().split()
    chairs = room[0]
    numberOfVisitors = int(room[1])
    if(len(chairs) - numberOfVisitors < 0):
        print(f"{numberOfVisitors - len(chairs)} more chairs needed in room {i}")
        game = False
    else:
        freeChairs += len(chairs) - numberOfVisitors
if(game):
    print(f"Game On, {freeChairs} free chairs left")