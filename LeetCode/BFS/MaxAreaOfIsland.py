from collections import deque

def BFS(row, col):
    queue = deque([(row, col)])
    area = 1
    grid[row][col] = 2

    while queue:
        r, c = queue.popleft()
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + i < n and 0 <= c + j < m:
                if grid[r + i][c + j] == 1:
                    area += 1
                    grid[r + i][c + j] = 2
                    queue.append((r + i, c + j))

    return area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

# grid = [[1,1,0,0,0],
#         [1,1,0,0,0],
#         [0,0,0,1,1],
#         [0,0,0,1,1]]

# grid = [[1]]

n = len(grid)
m = len(grid[0])

res = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            res = max(res, BFS(i, j))

print(res)