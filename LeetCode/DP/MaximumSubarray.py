# Divide and Conquer

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def findBestSubarray(nums, left, right):
    if left > right:
        return float('-inf')
    
    mid = (left + right) // 2
    curr = bestLeftSum = bestRightSum = 0

    for i in range(mid-1, left-1, -1):
        curr += nums[i]
        bestLeftSum = max(curr, bestLeftSum)
    
    curr = 0
    
    for i in range(mid+1, right+1):
        curr += nums[i]
        bestRightSum = max(curr, bestRightSum)

    bestCombinedSum = nums[mid] + bestLeftSum + bestRightSum

    leftHalf = findBestSubarray(nums, left, mid-1)
    rightHalf = findBestSubarray(nums, mid+1, right)

    return max(bestCombinedSum, leftHalf, rightHalf)

nums = [-1]

print(findBestSubarray(nums, 0, len(nums)-1))