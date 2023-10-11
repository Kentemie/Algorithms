# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the 
# elements in the subarray is strictly less than k.

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    prod = 1
    res = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        res += right - left + 1
    return res
        

nums = [10,5,2,6]
k = 100

nums = [1,2,3]
k = 0

print(numSubarrayProductLessThanK(nums, k))