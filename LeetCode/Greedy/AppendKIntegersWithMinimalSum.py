# You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to
# nums such that the resulting total sum is minimum.

# Return the sum of the k integers appended to nums.

from sortedcontainers import SortedSet

def minimalKSum(nums, k):
    kSum = k * (k + 1) // 2
    for num in SortedSet(nums):
        if k >= num:
            k += 1
            kSum += k - num
    return kSum

nums = [1,4,25,10,25]
k = 2

nums = [5,6]
k = 6

# nums = [1]
# k = 100000000

print(minimalKSum(nums, k))