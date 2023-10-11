# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any 
# subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

def splitArray(nums, k):
    left = max(nums)
    right = sum(nums)

    while left <= right:
        maxSumAllowed = (left + right) // 2
        currSum = 0
        splits = 1

        for num in nums:
            currSum += num
            if currSum > maxSumAllowed:
                currSum = num
                splits += 1
        
        if splits <= k:
            right = maxSumAllowed - 1
            minimumLargestSum = maxSumAllowed
        else:
            left = maxSumAllowed + 1

    return minimumLargestSum



nums = [7,2,5,10,8]
k = 2
# 18

nums = [1,2,3,4,5]
k = 2
# 9

print(splitArray(nums, k))