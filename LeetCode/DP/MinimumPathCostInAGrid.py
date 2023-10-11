# You are given a 0-indexed m x n integer matrix grid consisting of distinct integers from 0 to m * n - 1. You can move 
# in this matrix from a cell to any other cell in the next row. That is, if you are in cell (x, y) such that x < m - 1, 
# you can move to any of the cells (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1). Note that it is not possible to move from
# cells in the last row.

# Each possible move has a cost given by a 0-indexed 2D array moveCost of size (m * n) x n, where moveCost[i][j] is the 
# cost of moving from a cell with value i to a cell in column j of the next row. The cost of moving from cells in the last 
# row of grid can be ignored.

# The cost of a path in grid is the sum of all values of cells visited plus the sum of costs of all the moves made. 
# Return the minimum cost of a path that starts from any cell in the first row and ends at any cell in the last row.

def minPathCost(grid, moveCost):
    dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    for j in range(len(grid[0])):
        dp[0][j] = grid[0][j]

    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            idx = grid[i][j]
            for k in range(len(moveCost[idx])):
                dp[i + 1][k] = min(dp[i + 1][k], moveCost[idx][k] + dp[i][j] + grid[i + 1][k])
    
        
    return dp[-1]



# moveCost = [[9,8],
#             [1,5],
#             [10,12],
#             [18,6],
#             [2,4],
#             [14,3]]

# grid = [[5,3],
#         [4,0],
#         [2,1]]
# 17

grid = [[5,1,2],
        [4,0,3]]

moveCost = [[12,10,15],
            [20,23,8],
            [21,7,1],
            [8,1,13],
            [9,10,25],
            [5,3,2]]
# 6

print(min(minPathCost(grid, moveCost)))