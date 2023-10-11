# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
# right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square 
# that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# def uniquePathsWithObstacles(i, j):
#     if obstacleGrid[i][j] == 1:
#         return 0
#     if i == 0 and j == 0:
#         return 1
#     if i < 0 or j < 0:
#         return 0
#     if (i, j) in memo:
#         return memo[(i, j)]
    
#     memo[(i, j)] = uniquePathsWithObstacles(i - 1, j) + uniquePathsWithObstacles(i, j - 1)

#     return memo[(i, j)]

# # obstacleGrid = [[0,0,0],
#                 # [0,1,0],
#                 # [0,0,0]]

# # obstacleGrid = [[0,1],
#                 # [0,0]]

# obstacleGrid = [[1]]


# memo = {}

# n = len(obstacleGrid)
# m = len(obstacleGrid[0])

# print(uniquePathsWithObstacles(n - 1, m - 1))


obstacleGrid = [[1]]

n = len(obstacleGrid)
m = len(obstacleGrid[0])

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if obstacleGrid[i - 1][j - 1] == 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        

print(dp[n][m])