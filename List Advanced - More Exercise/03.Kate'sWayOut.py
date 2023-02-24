def all_false(x):
    for check in x:
        if check:
            return False
    return True
 
 
def char_replace(string, x, y):
    temp = list(string[x])
    temp[y] = "#"
    temp = "".join(temp)
    maze[x] = temp
 
 
def kate(x):
    for row in x:
        if "k" in row:
            return x.index(row), row.index("k")
 
 
def way_out_path(x):
    way_out_map = []
    for a, row in enumerate(x):
        for b, column in enumerate(row):
            if column == " ":
                way_out_map.append([a, b])
    return way_out_map
 
 
def way_out(x, y, way_out_map):
    move = 0
    while True:
        found_a_way = [[x, y+1] in way_out_map, [x, y-1] in way_out_map, [x+1, y] in way_out_map, [x-1, y] in way_out_map]
        found_a_way_value = [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]
 
        if x == maze_rows-1 or y == len(maze[0])-1 or y == 0:
            return f"Kate got out in {move+1} moves"
 
        if not all_false(found_a_way):
            x, y = found_a_way_value[found_a_way.index(True)]
            char_replace(maze, x, y)
            way_out_map.remove(found_a_way_value[found_a_way.index(True)])
            move += 1
 
        else:
            return "Kate cannot get out"
 
 
maze_rows = int(input())
maze = [input() for x in range(maze_rows)]
kate_row, kate_column = kate(maze)
map_to_freedom = way_out_path(maze)
print(way_out(kate_row, kate_column, map_to_freedom))






# n=int(input())
# maze=[list(input()) for i in range(n)]
# flag=False
# spaces=[]
# steps = 0
# steps_old=-1

# for i in range(n):
#     if 'k' in maze[i]:
#         k_idx=[i,maze[i].index(('k'))]

# maze[k_idx[0]][k_idx[1]]=' '    # make the space ocupied by Kate as a free space to move over
#                                 # in case a closed path was chosen and a new one is needed that passes
#                                 # through K's initial position

# visited=[[k_idx[0], k_idx[1]]]  # all spaces that Kate has visited
# def find_space(k,ma):
#     s_u=[] # space up .. etc...
#     s_r=[]
#     s_d=[]
#     s_l=[]
#     if k[0]!=0 and ma[k[0]-1][k[1]]==' ': s_u+= [k[0]-1,k[1]]
#     if k[1]<(len(ma[k[0]])-1) and ma[k[0]][k[1]+1]==' ': s_r+=[k[0],k[1]+1]
#     if k[0]<(len(ma)-1) and ma[k[0] + 1][ k[1]] == ' ': s_d+=[k[0] + 1, k[1]]
#     if k[1]!=0 and ma[k[0]][ k[1] - 1] == ' ':  s_l+=[k[0], k[1] - 1]
#     return [s_u,s_r,s_d,s_l]    # list of available spaces in each direction , busy spaces are empty,
#                                 # Edge spaces are covered separatly

# def move(k,s,v,maze,m):
#     for i in range(len(s)): # all available spaces around kate, s is the output from def find_space
#         if s[i] not in v and bool(s[i]):    #if the space is not visited and is free
#             k=s[i]                         #Kate moves there
#             v.append(s[i])
#             m+=1
#             return k,v,m
#         elif all(i in v for i in list(filter(lambda x : bool(x),s))): # if all available spaces are already visited
#             maze[k[0]][k[1]]='@'                  #Kate marks the space with @ BECAUSE this position doesnt lead to any new spaces or exits
#             k = v[-2]                       # Kate moves one step back
#             del v[-1]                       # Kate removes the marked with @ space from the visited spaces as
#                             # it is clearly a dead end and from now on will be part of the Maze walls
#             m-=1            # as Kate moves back, we decrease the steps
#             return k,v,m




# while k_idx[0]<=(n-1):
#     if k_idx[1] == 0 or k_idx[1] == len(maze[0]) - 1 or k_idx[0] == 0 or k_idx[0] == n - 1:
#         steps_old = max(steps, steps_old) # if Kate is on the Edge then we have a possible exit
#                                             # but will explore other options


#     spaces=find_space(k_idx,maze) # check where Kate can go
#     #  now check if there are spaces to go
#     if not sum((lambda x : bool(x))(x) for x in spaces) and k_idx[0]<(n-1) and steps_old==-1:
#         # if we didn't encounter a possible exit in the past (steps_old==-1)
#         # and we have ways to go now, then there is no exit
#         print("Kate cannot get out")
#         flag=True
#         break
#     elif not sum((lambda x: bool(x))(x) for x in spaces) and steps_old != -1:
#         steps=steps_old #if we have no ways to go, and we have a possible exit, then that's the exit
#         break
#     # then if there are spaces to go, GO
#     k_idx, visited, steps = move(k_idx,spaces,visited,maze,steps)
#     # print('\n\n')
#     # for elem in range(n):  # check your way back building walls in the Maze
#     #     print(''.join(maze[elem]))
#     # print(k_idx)

# if  not flag:
#     print(f"Kate got out in {max(steps,steps_old)+1} moves")