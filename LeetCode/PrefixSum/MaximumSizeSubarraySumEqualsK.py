# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there 
# is not one, return 0 instead.

def maxSubArrayLen(nums, k):
    indices = {}
    longestSubArray = prefixSum = 0
    
    for i in range(len(nums)):
        prefixSum += nums[i]
        if prefixSum == k:
            longestSubArray = i + 1
        if prefixSum - k in indices:
            longestSubArray = max(longestSubArray, i - indices[prefixSum - k])
        if prefixSum not in indices:
            indices[prefixSum] = i

    return longestSubArray

nums = [1,-1,5,-2,3]
k = 3

print(maxSubArrayLen(nums, k))