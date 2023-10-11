# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
# Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

    # lefti is the x coordinate of the left edge of the ith building.
    # righti is the x coordinate of the right edge of the ith building.
    # heighti is the height of the ith building.

# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each 
# key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a 
# y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost 
# and rightmost buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, 
# [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in 
# the final output as such: [...,[2 3],[4 5],[12 7],...]


# Time complexity: O(n^2)
def getSkyline(buildings):
    positions = sorted(list(set([x for building in buildings for x in building[:2]])))

    edge_idx_map = { x: idx for idx, x in enumerate(positions) }

    heights = [0] * len(positions)

    for left, right, height in buildings:
        left_idx = edge_idx_map[left]
        right_idx = edge_idx_map[right]

        for i in range(left_idx, right_idx):
            heights[i] = max(heights[i], height)

    result = []

    for i in range(len(positions)):
        curr_height = heights[i]
        curr_pos = positions[i]

        if not result or result[-1][1] != curr_height:
            result.append([curr_pos, curr_height])

    return result


buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[0,2,3],[2,5,3]]
buildings = [[2,9,10],[9,12,15]]
buildings = [[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]]

print(getSkyline(buildings))