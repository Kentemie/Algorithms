# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the 
# following properties:

#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.

def searchMatrix(matrix, target):
    def search(left, right, top, bottom):
        if left > right or top > bottom:
            return False
        elif target < matrix[top][left] or target > matrix[bottom][right]:
            return False
        mid = left + (right - left) // 2
        row = top
        while row <= bottom and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True 
            row += 1
        return search(left, mid - 1, row, bottom) or search(mid + 1, right, top, row - 1)
    
    return search(0, len(matrix[0]) - 1, 0, len(matrix) - 1)

matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]

target = 20

print(searchMatrix(matrix, target))


# Search Space Reduction
# Time complexity : O(n+m)
# Space complexity : O(1)

# def searchMatrix(matrix, target):
#     row, col = 0, len(matrix[0]) - 1

#     while row < len(matrix) and col >= 0:
#         if matrix[row][col] == target:
#             return True
#         elif matrix[row][col] > target:
#             col -= 1
#         else:
#             row += 1

#     return False


# matrix = [[1,4,7,11,15],
#           [2,5,8,12,19],
#           [3,6,9,16,22],
#           [10,13,14,17,24],
#           [18,21,23,26,30]]

# target = 5

# print(searchMatrix(matrix, target))