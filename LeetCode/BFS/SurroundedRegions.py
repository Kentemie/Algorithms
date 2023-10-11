from itertools import product
from collections import deque

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

def BFS(row, col):
    queue = deque([(row, col)])
    while queue:
        row, col = queue.popleft()
        
        if board[row][col] != 'O': 
            continue

        board[row][col] = 'S'
        if col < m - 1: queue.append((row, col + 1))
        if row < n - 1: queue.append((row + 1, col))
        if col > 0: queue.append((row, col - 1))
        if row > 0: queue.append((row - 1, col))


n = len(board)
m = len(board[0])

borders = list(product(range(n), [0, m - 1])) + list(product([0, n - 1], range(m)))

for row, col in borders:
    BFS(row, col)

for i in range(n):
    for j in range(m):
        if board[i][j] == 'O':
            board[i][j] = 'X'
        elif board[i][j] == 'S':
            board[i][j] = 'O'

for row in board:
    print(row)