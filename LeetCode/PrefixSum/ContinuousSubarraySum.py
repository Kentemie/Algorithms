# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a subarray where:

    # its length is at least two, and
    # the sum of the elements of the subarray is a multiple of k.

# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

def checkSubarraySum(nums, k):
    hashMap = {0: 0}
    prefSum = 0
    for i in range(len(nums)):
        prefSum += nums[i]
        MOD = prefSum % k
        if MOD not in hashMap:
            hashMap[MOD] = i + 1
        elif hashMap[MOD] < i:
            # print(hashMap[MOD], i)
            return True
    return False

nums = [23,2,6,4,7]
k = 6

print(checkSubarraySum(nums, k))