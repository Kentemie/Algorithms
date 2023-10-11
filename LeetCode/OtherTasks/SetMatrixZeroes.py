# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

def setZeroes(matrix):
    setColToZero = False
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        if matrix[i][0] == 0:
            setColToZero = True
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, m):
        for j in range(1, n):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0
    
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0
    
    if setColToZero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]

print(setZeroes(matrix))