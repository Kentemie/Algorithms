# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and 
# columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

# A chess knight has eight possible moves it can . Each move is two cells in a cardinal direction, then one cell in an 
# orthogonal direction.

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would 
# go off the chessboard) and moves there.

# The knight continues moving until it has made exactly k moves or has moved off the chessboard.

# Return the probability that the knight remains on the board after it has stopped moving.

n = 3
k = 2
row = 0
column = 0

dp = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]
directions = [(2,1), (2,-1), (-2,-1), (-2,1), (1,2), (-1,2), (1,-2), (-1,-2)]

def knightProbability(i, j, k):
    if k == 0:
        if i == row and j == column:
            return 1
        else:
            return 0
    if dp[k][i][j] != -1:
        return dp[k][i][j]
    dp[k][i][j] = 0
    for move in directions:
        prev_i = i - move[0]
        prev_j = j - move[1]
        if 0 <= prev_i < n and 0 <= prev_j < n:
            dp[k][i][j] += knightProbability(prev_i, prev_j, k - 1)
    dp[k][i][j] /= 8
    return dp[k][i][j]

total = sum(knightProbability(i, j, k) for i in range(n) for j in range(n))

print(total)