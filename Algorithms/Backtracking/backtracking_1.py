def find_way_from_maze(r, c):
    visited[r][c] = True
    print(r,c)
    # 여기에 길찾기 함수 코드 작성
    print(M[r][c])
    if M[r][c] == '1':
        print("M[r][c] is Blocked")
        return
    elif r == ex and c == ey: 
        print("SUCCESS!")
        return True
    if c+1 < n and not visited[r][c+1]: #East
        print("EAST")
        if find_way_from_maze(r, c+1):
            M[r][c+1] = trace
            return True
    if r+1 < n and not visited[r+1][c]: #South
        print("SOUTH")
        if find_way_from_maze(r+1, c):
            M[r+1][c] = trace
            return True
    if c-1 >= 0 and not visited[r][c-1]: #West
        print("WEST")
        if find_way_from_maze(r, c-1):
            M[r][c-1] = trace
            return True
    if r-1 >= 0 and not visited[r-1][c]: #North
        print("NORTH")
        if find_way_from_maze(r-1, c):
            M[r-1][c] = trace
            return True



trace = '\u00B7'
global n
n = int(input())
sx, sy, ex, ey = (int(x) for x in input().split())
M = []
# row 0 and n+1 are all 1's
# col 0 and n+1 are all 1's
for i in range(n):
    M.append([c for c in input()])

visited = [[False for _ in range(n)] for _ in range(n)]
M[sx][sy] = 's'
print(visited)
success = find_way_from_maze(sx, sy)
print(success)
M[ex][ey] = 'e'
if success:
    for row in M:
        for c in row:
            if c == '1': 
                print('#', end="")
            elif c == '0':
                print(' ', end="")
            else:
                print(c, end="")
        print()
    print()
else:
    print("NO WAY!")
