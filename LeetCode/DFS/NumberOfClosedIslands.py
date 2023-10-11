# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and 
# a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

from itertools import product

def DFS(row, col):
    if grid[row][col] == 1: return 
    grid[row][col] = 1
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nextRow, nextCol = row + i, col + j
        if 0 <= nextRow < n and 0 <= nextCol < m:
            DFS(nextRow, nextCol)


grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]

grid = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]

# grid = [[1,1,1,1,1,1,1],
#         [1,0,0,0,0,0,1],
#         [1,0,1,1,1,0,1],
#         [1,0,1,0,1,0,1],
#         [1,0,1,1,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,1,1,1,1,1,1]]

n = len(grid)
m = len(grid[0])

borders = list(product(range(n), [0, m - 1])) + list(product([0, n - 1], range(m)))

for i, j in borders:
    DFS(i, j)

cnt = 0

for row in range(1, n - 1):
    for col in range(1, m - 1):
        if grid[row][col] == 0:
            cnt += 1
            DFS(row, col)

print(cnt)