# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how 
# much water it can trap after raining.

def trap(height):
    left, right = 0, len(height) - 1
    leftMax, rightMax = 0, 0
    ans = 0
    while left < right:
        if height[left] < height[right]:
            if leftMax >= height[left]:
                ans += leftMax - height[left]
            else:
                leftMax = height[left]
            left += 1
        else:
            if rightMax >= height[right]:
                ans += rightMax - height[right]
            else:
                rightMax = height[right]
            right -= 1 
    return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))