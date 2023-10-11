# Pascal's Triangle

# n = int(input())
# arr = []
# for i in range(n):
#     row = [0 for _ in range(i + 1)]
#     row[0], row[-1] = 1, 1
#     for j in range(1, len(row) - 1):
#         row[j] = arr[i - 1][j - 1] + arr[i - 1][j]  
#     arr.append(row)   
# print(arr)




# Check if Every Row and Column Contains All Numbers
# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

# matrix = [[1,2,3],[3,1,2],[2,3,1]]
# print(all(len(set(x)) == len(matrix) for x in matrix + list(zip(*matrix))))




# Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# res, curr = [], []
# n, m = len(mat), len(mat[0])
# for d in range(n + m - 1):
#     curr.clear()
#     i, j = 0 if d < m else d - m + 1, d if d < m else m - 1
#     while i < n and j > -1:
#         curr.append(mat[i][j])
#         i += 1
#         j -= 1

#     if d % 2 == 0:
#         res.extend(curr[::-1])
#     else:
#         res.extend(curr)

# print(res)




# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# def spiral_order(matrix):
#     if not matrix:
#         return []
#     n, m = len(matrix), len(matrix[0])
#     res = []

#     def traverse(top, left, bottom, right):
#         for i in range(left, right + 1):
#             res.append(matrix[top][i])
#         for j in range(top + 1, bottom + 1):
#             res.append(matrix[j][right])
#         if top != bottom:
#             for i in range(right - 1, left - 1, -1):
#                 res.append(matrix[bottom][i])
#         if left != right:
#             for j in range(bottom - 1, top, -1):
#                 res.append(matrix[j][left])
#     top, left, bottom, right = 0, 0, n - 1, m - 1
#     while top <= bottom and left <= right:
#         traverse(top, left, bottom, right)
#         top += 1
#         left += 1
#         bottom -= 1
#         right -= 1    
#     return res

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(spiral_order(matrix))




# Valid Sudoku

# def checkRow(board):
#     n = len(board)
#     m = len(board[0])
#     seen = set()
#     for i in range(n):
#         seen.clear()
#         for j in range(m):
#             if board[i][j] == ".":
#                 continue
#             else:
#                 if board[i][j] not in seen:
#                     seen.add(board[i][j])
#                 else:
#                     return False
#     return True

# def checkColumn(board):
#     n = len(board)
#     m = len(board[0])
#     seen = set()
#     for i in range(n):
#         seen.clear()
#         for j in range(m):
#             if board[j][i] == ".":
#                 continue
#             else:
#                 if board[j][i] not in seen:
#                     seen.add(board[j][i])
#                 else:
#                     return False
#     return True

# def checkBox(board):
#     n = len(board)
#     m = len(board[0])
#     boxes = [set() for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == ".":
#                 continue
#             idx = (i // 3) * 3 + j // 3
#             if board[i][j] in boxes[idx]:
#                 return False
#             boxes[idx].add(board[i][j])
#     return True


# board = [["5","3",".",".","7",".",".",".","."]
#          ,["6",".",".","1","9","5",".",".","."]
#          ,[".","9","8",".",".",".",".","6","."]
#          ,["8",".",".",".","6",".",".",".","3"]
#          ,["4",".",".","8",".","3",".",".","1"]
#          ,["7",".",".",".","2",".",".",".","6"]
#          ,[".","6",".",".",".",".","2","8","."]
#          ,[".",".",".","4","1","9",".",".","5"]
#          ,[".",".",".",".","8",".",".","7","9"]]

# if checkBox(board) and checkColumn(board) and checkRow(board):
#     print("YES")
# else:
#     print("NO")




# Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# m = len(matrix)
# n = len(matrix[0])
# setColToZero = False

# for i in range(m):
#     if matrix[i][0] == 0:
#         setColToZero = True
#     for j in range(1, n):
#         if matrix[i][j] == 0:
#             matrix[i][0] = 0
#             matrix[0][j] = 0

# for i in range(1, m):
#     for j in range(1, n):
#         if not matrix[i][0] or not matrix[0][j]:
#             matrix[i][j] = 0

# if matrix[0][0] == 0:
#     for j in range(n):
#         matrix[0][j] = 0

# if setColToZero:
#     for i in range(m):
#         matrix[i][0] = 0

# print(matrix)




# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# def rotate(arr, k):
#     n = len(arr)
#     k = k % n
#     for i in range((n - k) // 2):
#         arr[i], arr[n - k - 1 - i] = arr[n - k - 1 - i], arr[i]
#     for i in range(k // 2):
#         arr[n - k + i], arr[n - 1 - i] = arr[n - 1 - i], arr[n - k + i]
#     for i in range(n // 2):
#         arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]


# nums = [2147483647,-2147483648,33,219,0]
# k = 4
# rotate(nums, k)
# print(nums)




# from itertools import product

# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# # def DFS(row, col, board):
# #     if board[row][col] != "O":
# #         return
# #     board[row][col] = "S"
# #     if col < len(board[0]) - 1: DFS(row, col + 1, board)
# #     if row < len(board) - 1: DFS(row + 1, col, board)
# #     if col > 0: DFS(row, col - 1, board)
# #     if row > 0: DFS(row - 1, col, board)

# def BFS(row, col, board):
#     from collections import deque
#     queue = deque([(row, col)])
#     while queue:
#         (row, col) = queue.popleft()
#         if board[row][col] != "O":
#             continue
#         board[row][col] = "S"
#         if col < len(board[0]) - 1: queue.append((row, col + 1))
#         if row < len(board) - 1: queue.append((row + 1, col))
#         if col > 0: queue.append((row, col - 1))
#         if row > 0: queue.append((row - 1, col))

# borders = list(product(range(len(board)), [0, len(board[0]) - 1])) + list(product([0, len(board) - 1], range(len(board[0]))))

# for row, col in borders:
#     BFS(row, col, board)

# print(board)

# for row in range(len(board)):
#     for col in range(len(board[0])):
#         if board[row][col] == "O":
#             board[row][col] = "X"
#         elif board[row][col] == "S":
#             board[row][col] = "O"

# print(board)




# Flood Fill
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as 
# the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all 
# of the aforementioned pixels with color.

# def floodFill(image, sr: int, sc: int, color: int):
#     row, col = len(image), len(image[0])
#     oldColor = image[sr][sc]
#     if oldColor == color: 
#         return image
#     def DFS(r, c):
#         if image[r][c] == oldColor:
#             image[r][c] = color
#             if r >= 1:
#                 DFS(r - 1, c)
#             if r + 1 < row:
#                 DFS(r + 1, c)
#             if c >= 1:
#                 DFS(r, c - 1)
#             if c + 1 < col:
#                 DFS(r, c + 1)
#     DFS(sr, sc)
#     return image

# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2
# print(floodFill(image, sr, sc, color))



# Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# # def DFS(row, col, grid):
# #     if grid[row][col] != "1":
# #         return
# #     grid[row][col] = "2"
# #     if col < len(grid[0]) - 1: DFS(row, col + 1, grid)
# #     if row < len(grid) - 1: DFS(row + 1, col, grid)
# #     if col > 0: DFS(row, col - 1, grid)
# #     if row > 0: DFS(row - 1, col, grid)
# # cnt = 0
# # for i in range(len(grid)):
# #     for j in range(len(grid[0])):
# #         if grid[i][j] == "1":
# #             DFS(i, j, grid)
# #             cnt += 1
# # print(cnt)


# from collections import deque

# queue = deque()
# cnt = 0

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == "1":
#             cnt += 1
#             grid[i][j] = "0"
#             queue.append((i, j))
#             while queue:
#                 row, col = queue.popleft()
#                 grid[row][col] = "0"
#                 if col < len(grid[0]) - 1 and grid[row][col + 1] == "1":
#                     queue.append((row, col + 1))
#                     grid[row][col + 1] = "0"
#                 if row < len(grid) - 1 and grid[row + 1][col] == "1":
#                     queue.append((row + 1, col))
#                     grid[row + 1][col] = "0"
#                 if col > 0 and grid[row][col - 1] == "1":
#                     queue.append((row, col - 1))
#                     grid[row][col - 1] = "0"
#                 if row > 0 and grid[row - 1][col] == "1":
#                     queue.append((row - 1, col))
#                     grid[row - 1][col] = "0"
                    
# print(cnt)




# Walls and Gates
# You are given an m x n grid rooms initialized with these three possible values.
# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is 
# less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

from collections import deque
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
queue = deque()
for i in range(len(rooms)):
    for j in range(len(rooms[0])):
        if rooms[i][j] == 0:
            queue.append((i, j, 0))
while queue:
    row, col, step = queue.popleft()
    for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if 0 <= row + i < len(rooms) and 0 <= col + j < len(rooms[0]):
            if rooms[row + i][col + j] == 2147483647:
                rooms[row + i][col + j] = step + 1
                queue.append((row + i, col + j, step + 1))
print(rooms) 




# 01 Matrix
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# from collections import deque
# mat = [[0,1,1],[1,1,1],[1,1,1]]
# queue = deque()
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if mat[i][j] == 0:
#             queue.append((i, j, 0))
#         else:
#             mat[i][j] = -1
# while queue:
#     row, col, step = queue.popleft()
#     for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         if 0 <= row + i < len(mat) and 0 <= col + j < len(mat[0]):
#             if mat[row + i][col + j] == -1:
#                 mat[row + i][col + j] = step + 1
#                 queue.append((row + i, col + j, step + 1))
# print(mat)

