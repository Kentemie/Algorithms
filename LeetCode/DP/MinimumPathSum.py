# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the 
# sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

def minPathSum(n, m):
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if i == n - 1 and j != m - 1:
                grid[i][j] = grid[i][j] + grid[i][j + 1]
            elif i != n - 1 and j == m - 1:
                grid[i][j] = grid[i][j] + grid[i + 1][j]
            elif i != n - 1 and j != m - 1:
                grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])
    return grid[0][0]

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]

n = len(grid)
m = len(grid[0])

print(minPathSum(n, m))