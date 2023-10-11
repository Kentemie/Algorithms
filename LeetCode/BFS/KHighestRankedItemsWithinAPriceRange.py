# You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers 
# in the grid represent the following:

    # 0 represents a wall that you cannot pass through.
    # 1 represents an empty cell that you can freely move to and from.
    # All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.

# It takes 1 step to travel between adjacent grid cells.

# You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you 
# start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). 
# You are further given an integer k.

# You are interested in the positions of the k highest-ranked items whose prices are within the given price range. 
# The rank is determined by the first of these criteria that is different:

    # Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
    # Price (lower price has a higher rank, but it must be in the price range).
    # The row number (smaller row number has a higher rank).
    # The column number (smaller column number has a higher rank).

# Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than
# k reachable items within the price range, return all of them.

from collections import deque
from heapq import heappush, heappop

def BFS(row, col, k):
    n = len(grid)
    m = len(grid[0])

    heap = []
    queue = deque([(row, col, 0)])

    visited = set()
    visited.add((row, col))

    if pricing[0] <= grid[row][col] <= pricing[1]:
        heappush(heap, (0, grid[row][col], row, col))

    while queue:
        for _ in range(len(queue)):
            r, c, distance = queue.popleft()
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + i, c + j
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0 and (nr, nc) not in visited:

                    queue.append((nr, nc, distance + 1)) 
                    visited.add((nr, nc)) 


                    if pricing[0] <= grid[nr][nc] <= pricing[1]:
                        heappush(heap, (distance + 1, grid[nr][nc], nr, nc))

    res = []

    for _ in range(min(len(heap), k)):
        item = heappop(heap)
        res.append([item[2], item[3]])
        
    return res


# grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
# pricing = [2,5]
# start = [0,0]
# k = 3

# grid = [[1, 2,0,1],
#         [1,3,3,1],
#         [0,2,5,1]]
# pricing = [2,3]
# start = [2,3]
# k = 2

grid = [[1,1,1],[0,0,1],[2,3,4]]
pricing = [2,3]
start = [0,0]
k = 3

print(BFS(start[0], start[1], k))
