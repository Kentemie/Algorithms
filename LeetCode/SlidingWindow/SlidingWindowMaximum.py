# You are given an array of integers nums, there is a sliding window of size k which is moving from the very
# left of the array to the very right. You can only see the k numbers in the window. Each time the sliding
# window moves right by one position.

# Return the max sliding window.

def maxSlidingWindow(nums, k):
    n = len(nums)

    leftMax = [0] * n
    leftMax[0] = nums[0]
    rightMax = [0] * n
    rightMax[n - 1] = nums[n - 1]
    res = []

    for i in range(1, n):
        if i % k == 0:
            leftMax[i] = nums[i]
        else:
            leftMax[i] = max(leftMax[i - 1], nums[i])
        
        j = n - i - 1
        if (j + 1) % k == 0:
            rightMax[j] = nums[j]
        else:
            rightMax[j] = max(rightMax[j + 1], nums[j])
        
    for i in range(n - k + 1):
        res.append(max(leftMax[i + k - 1], rightMax[i]))

    return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

nums = [1]
k = 1

print(maxSlidingWindow(nums, k))
