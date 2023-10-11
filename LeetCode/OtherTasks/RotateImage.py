# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate
# another 2D matrix and do the rotation.

def rotate(matrix):
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save the top left
            topLeft = matrix[top][left + i]
            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left into top right
            matrix[top + i][right] = topLeft
        left += 1
        right -= 1

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]

rotate(matrix)

for row in matrix:
    print(row)