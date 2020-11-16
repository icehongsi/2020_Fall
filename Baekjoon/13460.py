import sys
global blue
import time

def solution(row, col, brow, bcol, count = 0):
    if count == 10:
        return False
    for i in visited:
        print(i)
    reverse = {1: 2, 2: 1, 3: 4, 4: 3}
    for i in range(1, 5):
        print(i)
        coord = move_marble(row, col, i)
        if coord != [row, col]: #좌표가 기존과 달라졌을 경우
            if coord == [brow,bcol]: #파란 구슬이 빨간 구슬보다 이동이 선행될 경우, 또한 파란 구슬이 움직일 수 있는 경우
                print("if")
                if [brow, bcol] != move_marble(brow, bcol, i):
                    while [brow, bcol] != move_marble(brow, bcol, i): #벽 또는 O이 나올 떄 까지 이동
                        brow, bcol = move_marble(row, col, i)
                    if maze[brow][bcol] == "O":
                        return
                    row, col = move_marble(brow, bcol, reverse[i])
            #빨간 구슬이 선행할 경우 그대로 진행
            else:
                print("else")
                while [row, col] != move_marble(row, col, i): #벽 또는 O이 나올 떄 까지 빨간 구슬 이동
                    print("red")
                    row, col = move_marble(row, col, i)
                while [brow, bcol] != move_marble(row, col, i): #벽 또는 O이 나올 떄 까지 파란 구슬 이동
                    print("blue")
                    brow, bcol = move_marble(row, col, i)
                if maze[row][col] == "O":
                    solutions.append(count)
                if maze[brow][bcol] == "O":
                    solutions.pop()
                    return
                if (brow, bcol) == (row, col):
                    brow, bcol = move_marble(row, col, reverse[i])
                print(row, col)
                print(brow, bcol)
                solution(row, col, brow, bcol, count + 1)


def move_marble(r, c, direction): # 1: East, 2: West, 3: South, 4: North
    time.sleep(1)
    print(r,c,direction)
    visited[r][c] = True
    move_to = {
        1: lambda x: [x[0], x[1]+1],
        2: lambda x: [x[0], x[1]-1],
        3: lambda x: [x[0]+1, x[1]],
        4: lambda x: [x[0]-1, x[1]]
    }
    temp = move_to[direction]([r,c])
    if maze[temp[0]][temp[1]] in ("#", "O") and visited[temp[0]][temp[1]]:
        return [r,c]
    else:
        visited[temp[0]][temp[1]] = True
        return temp


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