# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque

def BFS(grid):
    queue = deque()
    ans = 0
    cnt = 0
    totalSum = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            totalSum += grid[i][j]
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            if grid[i][j] == 0:
                cnt += 1
    
    while queue:
        row, col, minutes = queue.popleft()
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nextRow, nextCol = row + i, col + j
            if 0 <= nextRow < len(grid) and 0 <= nextCol < len(grid[0]):
                if grid[nextRow][nextCol] == 1:
                    queue.append((nextRow, nextCol, minutes + 1))
                    grid[nextRow][nextCol] = 2
                    totalSum += 1
        ans = minutes
    
    return ans if totalSum == (len(grid) * len(grid[0]) - cnt) * 2 else -1

grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]

grid = [[0,2]]

grid = [[1]]

print(BFS(grid))