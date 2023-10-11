# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col 
# representing the number of rows and columns in the matrix, respectively.

# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given 
# a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith
# column (1-based coordinates) will be covered with water (i.e., changed to 1).

# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. 
# You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four 
# cardinal directions (left, right, up, and down).

# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

from collections import deque

def canCross(day):
    grid = [[0] * col for _ in range(row)]
    queue = deque()
    
    for r, c in cells[:day]:
        grid[r - 1][c - 1] = 1
    
    for c in range(col):
        if grid[0][c] == 0:
            queue.append((0, c))
            grid[0][c] = -1
        
    while queue:
        r, c = queue.popleft()
        if r == row - 1:
            return True
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + i, c + j
            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                grid[nr][nc] = -1
                queue.append((nr, nc))

    return False

def latestDayToCross(row, col):
    left, right = 0, row * col

    while left < right:
        mid = right - (right - left) // 2
        if canCross(mid):
            left = mid
        else:
            right = mid - 1

    return left

row = 3
col = 3
cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

print(latestDayToCross(row, col, cells))