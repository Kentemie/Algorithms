# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    n = len(nums)
    k %= n

    for i in range((n - k) // 2):
        nums[i], nums[n - k - 1 - i] = nums[n - k - 1 - i], nums[i]
    
    for i in range(k // 2):
        nums[n - k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[n - k + i]

    for i in range(n // 2):
        nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

    return nums

nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

print(rotate(nums, k))