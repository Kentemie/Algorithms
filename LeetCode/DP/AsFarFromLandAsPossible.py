def maxDistance(grid):
    dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                dp[row][col] = 0
            else:
                if row > 0:
                    dp[row][col] = min(dp[row][col], dp[row - 1][col] + 1)
                if col > 0:
                    dp[row][col] = min(dp[row][col], dp[row][col - 1] + 1)
    
    for row in reversed(range(len(grid))):
        for col in reversed(range(len(grid[0]))):
            if row < len(grid) - 1:
                dp[row][col] = min(dp[row][col], dp[row + 1][col] + 1)
            if col < len(grid[0]) - 1:
                dp[row][col] = min(dp[row][col], dp[row][col + 1] + 1)

    return max(max(row) for row in dp)

grid = [[1,1,1],
        [1,1,1],
        [1,1,1]]

print(maxDistance(grid))