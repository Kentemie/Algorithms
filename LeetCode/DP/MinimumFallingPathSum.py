# # Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# # A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally 
# # left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# # Bottom-Up Dynamic Programming

# matrix = [[1]]

# def minSum(matrix):
#     for row in reversed(range(len(matrix) - 1)):
#         for col in range(len(matrix)):
#             if col == 0: 
#                 matrix[row][col] += min(matrix[row+1][col], matrix[row+1][col+1])
#             elif col == (len(matrix) - 1): 
#                 matrix[row][col] += min(matrix[row+1][col], matrix[row+1][col-1])
#             else:
#                 matrix[row][col] += min(matrix[row+1][col-1], matrix[row+1][col], matrix[row+1][col+1])
#     return min(matrix[0])

# print(minSum(matrix))


# Top-Down with memoization

matrix = [[1]]

memo = {}
minFallingSum = float('inf')

def minSum(row, col):
    if col < 0 or col == len(matrix):
        return float('inf')
    if row == (len(matrix) - 1):
        return matrix[row][col]
    if (row, col) in memo:
        return memo[(row, col)]
    left = minSum(row+1, col-1)
    middle = minSum(row+1, col)
    right = minSum(row+1, col+1)

    min_sum = min(left, middle, right) + matrix[row][col]

    memo[(row, col)] = min_sum
    
    return min_sum

for col in range(len(matrix)):
    minFallingSum = min(minFallingSum, minSum(0, col))

print(minFallingSum)