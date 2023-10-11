# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land).
# An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered
# water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this
# island in grid2.

# Return the number of islands in grid2 that are considered sub-islands.

def countSubIslands(grid1, grid2):
    n = len(grid1)
    m = len(grid1[0])
    visited = set()

    def DFS(row, col):
        if not (0 <= row < n and 0 <= col < m) or grid2[row][col] == 0 or (row, col) in visited:
            return True
        
        visited.add((row, col))
        res = True 
        if grid1[row][col] == 0:
            res = False

        res = DFS(row + 1, col) and res
        res = DFS(row - 1, col) and res
        res = DFS(row, col + 1) and res
        res = DFS(row, col - 1) and res

        return res
    
    cnt = 0
    for row in range(n):
        for col in range(m):
            if grid2[row][col] and (row, col) not in visited and DFS(row, col):
                cnt += 1
    
    return cnt

grid1 = [[1,1,1,0,0],
         [0,1,1,1,1],
         [0,0,0,0,0],
         [1,0,0,0,0],
         [1,1,0,1,1]]

grid2 = [[1,1,1,0,0],
         [0,0,1,1,1],
         [0,1,0,0,0],
         [1,0,1,1,0],
         [0,1,0,1,0]]

print(countSubIslands(grid1, grid2))