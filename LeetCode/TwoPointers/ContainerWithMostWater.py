# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith 
# line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# shrinking window, left/right initially at endpoints, shift the pointer with min height

def maxArea(height):
    res = 0
    left, right = 0, len(height) - 1

    while left < right:
        width = right - left
        res = max(res, width * min(height[right], height[left]))
        if height[right] >= height[left]:
            left += 1
        else:
            right -= 1

    return res

height = [1,8,6,2,5,4,8,3,7]
height = [1,2,1]

print(maxArea(height))