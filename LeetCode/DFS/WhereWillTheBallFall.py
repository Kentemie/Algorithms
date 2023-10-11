# You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

# Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

#     A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in 
#     the grid as 1.
#     A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in 
#     the grid as -1.

# We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball 
# gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

# Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball 
# from the ith column at the top, or -1 if the ball gets stuck in the box.

# def findBall(i, j):
#     if i == len(grid):
#         return j
#     if grid[i][j] > 0 and (j == len(grid[0]) - 1 or grid[i][j + 1] < 0):
#         return -1
#     if grid[i][j] < 0 and (j == 0 or grid[i][j - 1] > 0):
#         return -1
#     res = findBall(i + 1, j + grid[i][j])

#     return res 

# # grid = [[1,1,1,-1,-1],
# #         [1,1,1,-1,-1],
# #         [-1,-1,-1,1,1],
# #         [1,1,1,1,-1],
# #         [-1,-1,-1,-1,-1]]
# # [1,-1,-1,-1,-1]

# # grid = [[1]]
# # [-1]

# grid = [[1,1,1,1,1,1],
#         [-1,-1,-1,-1,-1,-1],
#         [1,1,1,1,1,1],
#         [-1,-1,-1,-1,-1,-1]]
# # [0,1,2,3,4,-1]

# ans = [-1] * len(grid[0])

# for j in range(len(ans)):
#     pos = findBall(0, j)
#     if pos >= 0:
#         ans[j] = pos

# print(ans)

def findBall(grid):
    res = [-1] * len(grid[0])
    for col in range(len(grid[0])):
        currCol = col
        for row in range(len(grid)):
            nextCol = currCol + grid[row][currCol]
            if (nextCol < 0) or (nextCol > len(grid[0]) - 1) or (grid[row][currCol] != grid[row][nextCol]):
                res[col] = -1
                break
            res[col] = nextCol
            currCol = nextCol
    
    return res



grid = [[1,1,1,1,1,1],
        [-1,-1,-1,-1,-1,-1],
        [1,1,1,1,1,1],
        [-1,-1,-1,-1,-1,-1]]

print(findBall(grid))