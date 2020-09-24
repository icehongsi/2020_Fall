def numIslands(grid):
    count = 0
    def dfs(i,j):
        if  i > len(grid) or i < 0 or j > len(grid[0]) or j < 0 or grid[i][j] != "1":
            return
        grid[i][j] = 0
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j-1)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                dfs(row, col)
                count += 1
    return count



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))