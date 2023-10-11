# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water 
# cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in 
# the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is 
# |x0 - x1| + |y0 - y1|.

from collections import deque

grid = [[1,0,1],
        [0,0,0],
        [1,0,1]]

queue = deque()
ans = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            queue.append((i, j, 0))

while queue:
    row, col, step = queue.popleft()
    for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]):
            if grid[row + i][col + j] == 0:
                grid[row + i][col + j] = step + 1
                queue.append((row + i, col + j, step + 1))
                ans = max(ans, grid[row + i][col + j])

print(ans if ans else -1)