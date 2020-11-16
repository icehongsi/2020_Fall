import sys
global blue
import time

def solution(row, col, brow, bcol, count = 0):
    print("-"*50)
    print(row,col)
    print(brow, bcol)
    print(count)
    for i in maze:
        print(i)
    for i in visited:
        print(i)
    print("-"*50)
    move_to = {
        1: lambda x: [x[0], x[1] + 1] if maze[x[0]][x[1]+1] not in ("R","#") and visited[x[0]][x[1]+1] == False else x,
        2: lambda x: [x[0], x[1] - 1] if maze[x[0]][x[1]-1] not in ("R","#") and visited[x[0]][x[1]-1] == False else x,
        3: lambda x: [x[0] + 1, x[1]] if maze[x[0]+1][x[1]] not in ("R","#") and visited[x[0]+1][x[1]] == False else x,
        4: lambda x: [x[0] - 1, x[1]] if maze[x[0]-1][x[1]] not in ("R","#") and visited[x[0]-1][x[1]] == False else x
    }
    reverse = {1: 2, 2: 1, 3: 4, 4: 3}
    if count == 10:
        return False
    for i in range(1, 5):
        print(i)
        if move_to[i]([row, col]) != [row, col]: #이동이 가능할 경우:
            print("moveable, direction: ", i)
            temp = move_to[i]([row, col])
            if [brow, bcol] == temp: #이동한 자리가 blue가 있는 곳인 경우
                #blue 먼저 움직이기
                if move_to[i]([brow, bcol]) != [brow, bcol]:
                    while move_to[i]([brow, bcol]) != [brow, bcol]:
                        visited[brow][bcol] = True #mark as visited
                        brow, bcol = move_to[i]([brow, bcol])
                    if maze[brow][bcol] == "O": return False
                    row, col = move_to[reverse[i]]([brow, bcol])
                    return solution(row, col, brow, bcol, count + 1)
            return

        else: #이동한 자리가 blue가 있는 곳이 아닌 경우
                print("else")
                while ([row,col], [brow,bcol]) != (move_to[i]([row, col]), move_to[i]([brow, bcol])):
                    temp = move_to[i]([row, col])
                    maze[row][col] = "."
                    visited[row][col] = True
                    row, col = temp #새로운 빨간공 좌표
                    if maze[row][col] != "O":
                        maze[row][col] = "R"
                    temp = move_to[i]([brow, bcol]) #새로운 파란공 좌표
                    maze[brow][bcol] = "."
                    visited[brow][bcol] = True
                    brow, bcol = temp
                    if maze[brow][bcol] != "O":
                        maze[brow][bcol] = "B"
                    if maze[row][col] == "O":
                        print("success")
                        solutions.append(count+1)
                        return True
                    if maze[brow][bcol] == "O":
                        solutions.pop()
                        return False
                    print(row, col)
                    print(brow, bcol)
                return solution(row,col,brow,bcol,count+1)
        return
    return



r, c = tuple(map(int, input().split()))
maze = []
for _ in range(r):
    maze.append(list(input())) # get map
    if "R" in maze[-1]:
        red = [_, maze[-1].index("R")]
    if "B" in maze[-1]:
        blue = [_, maze[-1].index("B")]

visited = [[False]*c for _ in range(r)]
solutions = []

solution(red[0], red[1], blue[0], blue[1])
print("*"*50)
print(solutions)
