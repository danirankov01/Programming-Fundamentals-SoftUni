number = int(input())
matrix = []
path = []
positionOfKate = 0
for i in range(number):
    maze = list(map(str, input()))
    if("k" in maze):
        positionOfKate = maze.index("k")
    if(" " in maze):
        for i in range(len(maze)):
            if(maze[i] == " "):
                path.append(i)
    matrix.append(maze)


for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])
        if(matrix[row][col] == "k"):
            pass