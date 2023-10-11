# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on 
# the current row, you may move to either index i or index i + 1 on the next row.

# def minimumTotal(triangle):
#     n = len(triangle)

#     def dp(i, j):
#         if i == n:
#             return 0
#         return triangle[i][j] + min(dp(i + 1, j), dp(i + 1, j + 1))
    
#     return dp(0, 0)


def minimumTotal(triangle):
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            smallest_above = float('inf')
            if col > 0:
                smallest_above = triangle[row - 1][col - 1]
            if col < row:
                smallest_above = min(smallest_above, triangle[row - 1][col])
            triangle[row][col] += smallest_above
    return min(triangle[-1])

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# triangle = [[-10]]

print(minimumTotal(triangle))