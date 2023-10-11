# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean
# touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
# heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east,
# and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow 
# from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from 
# cell (ri, ci) to both the Pacific and Atlantic oceans.

def pacificAtlantic(heights):
    n = len(heights)
    m = len(heights[0])
    
    Pacific = set()
    Atlantic = set()

    def DFS(row, col, reachable):
        reachable.add((row, col))

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newRow, newCol = row + i, col + j
            if not (0 <= newRow < n and 0 <= newCol < m):
                continue
            if (newRow, newCol) in reachable:
                continue
            if heights[newRow][newCol] < heights[row][col]:
                continue
            DFS(newRow, newCol, reachable)

    for i in range(n):
        DFS(i, 0, Pacific)
        DFS(i, m - 1, Atlantic)

    for j in range(m):
        DFS(0, j, Pacific)
        DFS(n - 1, j, Atlantic)
    
    return list(Pacific.intersection(Atlantic))

heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]

heights = [[1]]

print(pacificAtlantic(heights))