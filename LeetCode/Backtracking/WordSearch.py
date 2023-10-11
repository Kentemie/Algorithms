# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or 
# vertically neighboring. The same letter cell may not be used more than once.

def exist(board, word):
    res = False
    dp = [[False] * len(board[0]) for _ in range(len(board))]

    def backTrack(row, col, i):
        nonlocal res
        if i == len(word):
            res = True
        if not res:
            if word[i] == board[row][col] and not dp[row][col]:
                dp[row][col] = True
                if len(word) == 1:
                    backTrack(row, col, i + 1)
                if col < len(board[0]) - 1:
                    backTrack(row, col + 1, i + 1)
                if row < len(board) - 1:
                    backTrack(row + 1, col, i + 1)
                if col > 0:
                    backTrack(row, col - 1, i + 1)
                if row > 0:
                    backTrack(row - 1, col, i + 1)
                dp[row][col] = False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if res:
                return res
            if word[0] == board[i][j]:
                backTrack(i, j, 0)
    return res

# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]

# word = "ABCCED"

# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]

# word = "SEE"

# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]

# word = "ABCB"

board = [["a"]]

word = "a"

print(exist(board, word))