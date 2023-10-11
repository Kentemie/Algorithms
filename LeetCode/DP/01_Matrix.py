# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

def updateMatrix(mat):
    dp = [[float('inf')] * len(mat[0]) for _ in range(len(mat))]

    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                dp[row][col] = 0
            else:
                if row > 0:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col] + 1)
                if col > 0:
                    dp[row][col] = min(dp[row][col], dp[row][col - 1] + 1)
    
    for row in reversed(range(len(mat))):
        for col in reversed(range(len(mat[0]))):
            if row < len(mat) - 1:
                dp[row][col] = min(dp[row][col], dp[row + 1][col] + 1)
            if col < len(mat[0]) - 1:
                dp[row][col] = min(dp[row][col], dp[row][col + 1] + 1)

    return dp


# mat = [[0,0,0],
    #    [0,1,0],
    #    [0,0,0]]

mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]

print(updateMatrix(mat))