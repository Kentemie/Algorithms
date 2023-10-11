# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and 
# an empty space, respectively.

def solveNQueens(n):
    col = set()
    posDiag = set()
    negDiag = set()
    res = []
    board = [['.'] * n for _ in range(n)]

    def isValid(r, c):
        return not((r + c) in posDiag or (r - c) in negDiag or c in col)
    
    def addQueen(r, c):
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = 'Q'

    def removeQueen(r, c):
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = '.'

    def createBoard(state):
        board = []
        for row in state:
            board.append("".join(row))
        return board
    
    def backTracking(row):
        if row == n:
            res.append(createBoard(board))
        for col in range(n):
            if isValid(row, col):
                addQueen(row, col)
                backTracking(row + 1)
                removeQueen(row, col)

    backTracking(0)
    
    return res

n = 4

print(solveNQueens(n))