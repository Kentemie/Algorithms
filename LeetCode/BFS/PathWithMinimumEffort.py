# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where 
# heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you
# hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right,
# and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

from heapq import heappop, heappush

def minimumEffortPath(heights):
    n = len(heights)
    m = len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    priority_queue = [(0, 0, 0)]
    difference_matrix = [[float("inf")] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    difference_matrix[0][0] = 0

    while priority_queue:
        _, r, c = heappop(priority_queue)
        visited[r][c] = True
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc]:
                continue

            current_difference = abs(heights[nr][nc] - heights[r][c])
            max_difference = max(current_difference, difference_matrix[r][c])

            if difference_matrix[nr][nc] > max_difference:
                difference_matrix[nr][nc] = max_difference
                heappush(priority_queue, (max_difference, nr, nc))

    return difference_matrix[-1][-1]

heights = [[1,2,1,1,1],
           [1,2,1,2,1],
           [1,2,1,2,1],
           [1,2,1,2,1],
           [1,1,1,2,1]]
# 0

heights = [[1,2,3],
           [3,8,4],
           [5,3,5]]
# 1

heights = [[1,2,2],
           [3,8,2],
           [5,3,5]]
# 2

print(minimumEffortPath(heights))