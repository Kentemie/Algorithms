# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and 
# lower right corner (row2, col2).

# Implement the NumMatrix class:

    # NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    # int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
    # defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    # You must design an algorithm where sumRegion works on O(1) time complexity.

class NumMatrix:
    def __init__(self, matrix):
        self.matrix = self.integralImage(matrix)

    def integralImage(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        SAT = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                SAT[i][j] = matrix[i - 1][j - 1] + SAT[i - 1][j] + SAT[i][j - 1] - SAT[i - 1][j - 1]
        
        return SAT

    def sumRegion(self, row1, col1, row2, col2):
        return self.matrix[row2 + 1][col2 + 1] - (self.matrix[row2 + 1][col1] + self.matrix[row1][col2 + 1] - self.matrix[row1][col1])
    
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])

print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))