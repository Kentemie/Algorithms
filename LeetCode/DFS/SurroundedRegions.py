# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

from itertools import product

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

def DFS(row, col):
    if board[row][col] != 'O': return 
    board[row][col] = 'S'
    if col < m - 1: DFS(row, col + 1)
    if row < n - 1: DFS(row + 1, col)
    if col > 0: DFS(row, col - 1)
    if row > 0: DFS(row - 1, col)

n = len(board)
m = len(board[0])

borders = list(product(range(n), [0, m - 1])) + list(product([0, n - 1], range(m)))

for row, col in borders:
    DFS(row, col)

for i in range(n):
    for j in range(m):
        if board[i][j] == 'O':
            board[i][j] = 'X'
        elif board[i][j] == 'S':
            board[i][j] = 'O'

for row in board:
    print(row)