# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

def DFS(row, col):
    if not (0 <= row < n and 0 <= col < m and grid[row][col] != 2 and grid[row][col]):
        return 0
    
    grid[row][col] = 2

    return 1 + DFS(row + 1, col) + DFS(row - 1, col) + DFS(row, col + 1) + DFS(row, col - 1)

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

n = len(grid)
m = len(grid[0])

print(max(DFS(i, j) for i in range(n) for j in range(m)))