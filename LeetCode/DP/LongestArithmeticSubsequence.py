# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

# Note that:

    # A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of 
    # the remaining elements.
    # A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

def longestArithSeqLength(nums):
    dp = {}

    for i in range(1, len(nums)):
        for j in range(i):
            dp[(i, nums[i] - nums[j])] = dp.get((j, nums[i] - nums[j]), 1) + 1

    return max(dp.values())


nums = [3,6,9,12]
nums = [9,4,7,2,10]
nums = [20,1,15,3,10,5,8]

print(longestArithSeqLength(nums))