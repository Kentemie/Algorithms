def trap(height):
    leftMax = [0] * len(height)
    rightMax = [0] * len(height)
    leftMax[0] = height[0]
    rightMax[len(height) - 1] = height[len(height) - 1]
    ans = 0

    for i in range(1, len(height)):
        leftMax[i] = max(leftMax[i - 1], height[i])
    
    for i in reversed(range(len(height) - 1)):
        rightMax[i] = max(rightMax[i + 1], height[i])

    for i in range(1, len(height) - 1):
        ans += min(leftMax[i], rightMax[i]) - height[i]

    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]

print(trap(height))