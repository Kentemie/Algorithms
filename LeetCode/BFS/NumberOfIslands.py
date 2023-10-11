# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
# all four edges of the grid are all surrounded by water.

from collections import deque

def BFS(grid):
    queue = deque()
    cnt = 0
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                cnt += 1
                queue.append((i, j))
                while queue:
                    row, col = queue.popleft()
                    grid[row][col] = '0'

                    if col < m - 1 and grid[row][col + 1] == "1":
                        queue.append((row, col + 1))
                        grid[row][col + 1] = "0"
                    if row < n - 1 and grid[row + 1][col] == "1":
                        queue.append((row + 1, col))
                        grid[row + 1][col] = "0"
                    if col > 0 and grid[row][col - 1] == "1":
                        queue.append((row, col - 1))
                        grid[row][col - 1] = "0"
                    if row > 0 and grid[row - 1][col] == "1":
                        queue.append((row - 1, col))
                        grid[row - 1][col] = "0"
    return cnt

# grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(BFS(grid))