# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

from collections import deque

def BFS(row, col):
    grid[row][col] = 'S'
    queue = deque([(row, col)])

    while queue:
        r, c = queue.popleft()
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nextRow, nextCol = r + i, c + j
            if 0 <= nextRow < n and 0 <= nextCol < m:
                if grid[nextRow][nextCol] == 1:
                    grid[nextRow][nextCol] = 'S'
                    queue.append((nextRow, nextCol))

def BFS2():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                
    res = float('inf')
    while queue:
        r, c, dist = queue.popleft()
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nextRow, nextCol = r + i, c + j
            if 0 <= nextRow < n and 0 <= nextCol < m:
                if grid[nextRow][nextCol] == 0:
                    grid[nextRow][nextCol] = dist + 1
                    queue.append((nextRow, nextCol, dist + 1))
                elif grid[nextRow][nextCol] == 'S':
                    res = min(res, dist)
    
    return res

grid = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

# grid = [[0,1,0],[0,0,0],[0,0,1]]

# grid = [[0,0,1,0,1],
#         [0,1,1,0,1],
#         [0,1,0,0,1],
#         [0,0,0,0,0],
#         [0,0,0,0,0]]

n = len(grid)
m = len(grid[0])

initRow, initCol = 0, 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            initRow, initCol = i, j
            break


BFS(initRow, initCol)

print(BFS2())

for row in grid:
    print(row)