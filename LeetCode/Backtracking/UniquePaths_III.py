# You are given an m x n integer array grid where grid[i][j] could be:

    # 1 representing the starting square. There is exactly one starting square.
    # 2 representing the ending square. There is exactly one ending square.
    # 0 representing empty squares we can walk over.
    # -1 representing obstacles that we cannot walk over.

# Return the number of 4-directional walks from the starting square to the ending 
# square, that walk over every non-obstacle square exactly once.

def uniquePathsIII(grid):
    n = len(grid)
    m = len(grid[0])

    non_obstacles = 0
    initRow, initCol = 0, 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 0:
                non_obstacles += 1
            if grid[i][j] == 1:
                initRow, initCol = i, j

    paths = 0

    def backTrack(row, col, remain):
        nonlocal paths
        if remain == 1 and grid[row][col] == 2:
            paths += 1
            return
        
        temp = grid[row][col]
        grid[row][col] = -2
        remain -= 1

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nextRow, nextCol = row + i, col + j
            if not (0 <= nextRow < n and 0 <= nextCol < m):
                continue
            if grid[nextRow][nextCol] < 0:
                continue
            backTrack(nextRow, nextCol, remain)

        grid[row][col] = temp

    backTrack(initRow, initCol, non_obstacles) 

    return paths  



grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,0,2]]

print(uniquePathsIII(grid))