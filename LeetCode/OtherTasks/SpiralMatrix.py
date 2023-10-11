# Given an m x n matrix, return all elements of the matrix in spiral order.

def spiralOrder(matrix):
    if not matrix:
        return []
    res = []
    n, m = len(matrix), len(matrix[0])

    def traverse(left, right, top, bottom):
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        for i in range(top + 1, bottom + 1):
            res.append(matrix[i][right])
        if top != bottom:
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom][i])
        if left != right:
            for i in range(bottom - 1, top, -1):
                res.append(matrix[i][left])

    top, left, bottom, right = 0, 0, n - 1, m - 1

    while top <= bottom and left <= right:
        traverse(left, right, top, bottom)
        top += 1
        left += 1
        bottom -= 1
        right -= 1

    return res

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(spiralOrder(matrix))