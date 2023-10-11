# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1))
# such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

from collections import deque

def BFS(row, col):
    if grid[row][col] == 1 or grid[-1][-1] == 1:
        return -1
    
    queue = deque([(row, col, 1)])
    
    grid[row][col] = 1

    while queue:
        r, c, path = queue.popleft()
        distance = grid[r][c]
        if (r, c) == (n - 1, n - 1):
            return distance
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            nextRow, nextCol = r + i, c + j
            if 0 <= nextRow < n and 0 <= nextCol < n:
                if grid[nextRow][nextCol] == 0:
                    grid[nextRow][nextCol] = path + 1
                    queue.append((nextRow, nextCol, path + 1))
    
    return -1


grid = [[0,0,0],
        [1,1,0],
        [1,1,0]]

grid = [[0,1],
        [1,0]]

# grid = [[1,0,0],
#         [1,1,0],
#         [1,1,0]]

n = len(grid)

print(BFS(0, 0))