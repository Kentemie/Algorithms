# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


def solveSudoku(board):
    columns = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    sudokuIsSolved = False

    for i in range(9):
        for j in range(9):
            idx = (i // 3) * 3 + j // 3
            if board[i][j] != '.':
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[idx].add(board[i][j])

    def isValid(row, col, val):
        val = str(val)
        idx = (row // 3) * 3 + col // 3
        return not(val in columns[col] or val in rows[row] or val in boxes[idx]) 
    
    def addVal(row, col, val):
        val = str(val)
        idx = (row // 3) * 3 + col // 3
        rows[row].add(val)
        columns[col].add(val)
        boxes[idx].add(val)
        board[row][col] = val

    def removeVal(row, col, val):
        val = str(val)
        idx = (row // 3) * 3 + col // 3
        rows[row].remove(val)
        columns[col].remove(val)
        boxes[idx].remove(val)
        board[row][col] = '.'

    def addNextVals(row, col):
        if col == 8 and row == 8:
            nonlocal sudokuIsSolved
            sudokuIsSolved = True
        else:
            if col == 8:
                backTrack(row + 1, 0)
            else:
                backTrack(row, col + 1)

    def backTrack(row = 0, col = 0):
        if board[row][col] == '.':
            for val in range(1, 10):
                if isValid(row, col, val):
                    addVal(row, col, val)
                    addNextVals(row, col)
                    if not sudokuIsSolved:
                        removeVal(row, col, val)
        else:
            addNextVals(row, col)
                        
    backTrack()

    return board


res = solveSudoku(board)

for row in res:
    print(row)