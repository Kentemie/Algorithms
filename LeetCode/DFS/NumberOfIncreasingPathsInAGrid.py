# You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

# Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. 
# Since the answer may be very large, return it modulo 109 + 7.

# Two paths are considered different if they do not have exactly the same sequence of visited cells.

def DFS(row, col):
    if dp[row][col]:
        return dp[row][col]
    ans = 1
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        pr, pc = row + i, col + j
        if (0 <= pr < n and 0 <= pc < m and grid[pr][pc] < grid[row][col]):
            ans += DFS(pr, pc) % MOD

    dp[row][col] = ans
    
    return ans


# grid = [[9,9,4],
#           [6,6,8],
#           [2,1,1]]

grid = [[3,4,5],
          [3,2,6],
          [2,2,1]]

# grid = [[0,1,2,3,4,5,6,7,8,9],
#           [19,18,17,16,15,14,13,12,11,10],
#           [20,21,22,23,24,25,26,27,28,29],
#           [39,38,37,36,35,34,33,32,31,30],
#           [40,41,42,43,44,45,46,47,48,49],
#           [59,58,57,56,55,54,53,52,51,50],
#           [60,61,62,63,64,65,66,67,68,69],
#           [79,78,77,76,75,74,73,72,71,70],
#           [80,81,82,83,84,85,86,87,88,89],
#           [99,98,97,96,95,94,93,92,91,90],
#           [100,101,102,103,104,105,106,107,108,109],
#           [119,118,117,116,115,114,113,112,111,110],
#           [120,121,122,123,124,125,126,127,128,129],
#           [139,138,137,136,135,134,133,132,131,130],
#           [0,0,0,0,0,0,0,0,0,0]]

# grid = [[1,1],[3,4]]

n = len(grid)
m = len(grid[0])
MOD = 10 ** 9 + 7

dp = [[0] * m for _ in range(n)]

res = 0

for i in range(n):
    for j in range(m):
        res += DFS(i, j)

print(res % MOD)