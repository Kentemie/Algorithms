# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 
# 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim
# infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

from heapq import heappop, heappush

def swimInWater(grid):
    n = len(grid)
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    minHeap = [(grid[0][0], 0, 0)] # (time/max-height, r, c)
    visited.add((0, 0))

    while minHeap:
        time, row, col = heappop(minHeap)

        if row == n - 1 and col == n - 1:
            return time
        for dr, dc in directions:
            nr, nc = dr + row, dc + col
            if not (0 <= nr < n and 0 <= nc < n) or (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))


grid = [[0,1,2,3,4],
        [24,23,22,21,5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10,9,8,7,6]]

grid = [[0,2],
        [1,3]]

print(swimInWater(grid))