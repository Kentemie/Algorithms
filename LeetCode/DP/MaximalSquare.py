# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
maxSqrLen = 0
dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

for row in range(1, len(matrix) + 1):
    for col in range(1, len(matrix[0]) + 1):
        if matrix[row-1][col-1] == '1':
            dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
            maxSqrLen = max(maxSqrLen, dp[row][col])
    
print(maxSqrLen * maxSqrLen)