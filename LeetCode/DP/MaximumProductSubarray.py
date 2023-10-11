# Given an integer array nums, find a subarray that has the largest product, and return the product.

def maxProduct(nums):
    prevMax = prevMin = maxSoFar = nums[0]

    for i in range(1, len(nums)):
        currMax = max(prevMax * nums[i], prevMin * nums[i], nums[i])
        currMin = min(prevMax * nums[i], prevMin * nums[i], nums[i])
        prevMax, prevMin = currMax, currMin
        maxSoFar = max(maxSoFar, currMax)
    return maxSoFar

nums = [2,3,-2,4]
# 6
# [2,3] has the largest product 6.

print(maxProduct(nums))