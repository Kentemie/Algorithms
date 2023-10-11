# You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you
# want to reach position (m - 1, n - 1) moving only down or right.

# Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very
# large, return it modulo 109 + 7.

def solve(i, j, rem, MOD, dp):
    if i == 0 and j == 0:
        rem = (rem + grid[i][j]) % k
        if rem % k == 0:
            return 1
        return 0
    if i < 0 or j < 0:
        return 0
    if dp[i][j][rem] != -1:
        return dp[i][j][rem]
    
    dp[i][j][rem % k] = (solve(i - 1, j, (rem + grid[i][j]) % k, MOD, dp) + solve(i, j - 1, (rem + grid[i][j]) % k, MOD, dp)) % MOD

    return dp[i][j][rem % k]

def numberOfPaths(grid, k):
    MOD = 10 ** 9 + 7
    dp = [[[-1] * (k + 1) for _ in range(len(grid[0]))] for _ in range(len(grid))]

    return solve(len(grid) - 1, len(grid[0]) - 1, 0, MOD, dp)


grid = [[5,2,4],
        [3,0,5],
        [0,7,2]]
k = 3

grid = [[0,0]]
k = 5

grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
k = 1

print(numberOfPaths(grid, k))