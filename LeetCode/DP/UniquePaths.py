# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to 
# move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

def uniquePaths(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 0 and n == 0:
        return 1
    if (m, n) in memo:
        return memo[(m, n)]
    memo[(m, n)] = uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
    return memo[(m, n)]

m = 3
n = 7
# 28
# m = 3
# n = 2
# 3

memo = {}

print(uniquePaths(m - 1, n - 1))