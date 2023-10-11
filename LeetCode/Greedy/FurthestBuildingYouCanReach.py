# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

    # If the current building's height is greater than or equal to the next building's height, you do not need a ladder 
    # or bricks.
    # If the current building's height is less than the next building's height, you can either use one ladder or 
    # (h[i+1] - h[i]) bricks.

# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

from heapq import heappop, heappush

def furthestBuilding(heights, bricks, ladders):
    bricksOrLadders = []
    for i in range(1, len(heights)):
        climb = heights[i] - heights[i - 1]
        if climb > 0:
            heappush(bricksOrLadders, climb)
            if len(bricksOrLadders) > ladders:
                bricks -= heappop(bricksOrLadders)
            if bricks < 0:
                return i - 1

    return len(heights) - 1


heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
# 4

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
# 7

heights = [14,3,19,3]
bricks = 17
ladders = 0
# 3

print(furthestBuilding(heights, bricks, ladders))