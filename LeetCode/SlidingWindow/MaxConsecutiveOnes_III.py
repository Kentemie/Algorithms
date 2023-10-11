# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if 
# you can flip at most k 0's.

def longestOnes(nums, k):
    numOfZeroes = 0
    maxLen = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            numOfZeroes += 1
        while numOfZeroes > k:
            if nums[left] == 0:
                numOfZeroes -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)

    return maxLen

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

print(longestOnes(nums, k))