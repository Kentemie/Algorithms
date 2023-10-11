# Given two positive integers m and n which are the height and width of a 0-indexed 2D-array board, a pair of positive 
# integers (r, c) which is the starting position of the knight on the board.

# Your task is to find an order of movements for the knight, in a manner that every cell of the board gets visited exactly
#  once (the starting cell is considered visited and you shouldn't visit it again).

# Return the array board in which the cells' values show the order of visiting the cell starting from 0 (the initial
#  place of the knight).

def tourOfKnight(m, n, r, c):
    board = [[-1] * n for _ in range(m)]

    def DFS(i, j, k):
        if k == m * n:
            return True 
        for r, c in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            nr, nc = i + r, j + c
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == -1:
                board[nr][nc] = k 
                if DFS(nr, nc, k + 1):
                    return True
                board[nr][nc] = -1
        return False
    
    board[r][c] = 0
    DFS(r, c, 1)
    return board

m = 1
n = 1
r = 0
c = 0

m = 3
n = 4
r = 0
c = 0

print(tourOfKnight(m, n, r, c))