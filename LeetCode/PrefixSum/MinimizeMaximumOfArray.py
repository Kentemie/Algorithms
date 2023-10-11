# You are given a 0-indexed array nums comprising of n non-negative integers.

# In one operation, you must:

#     Choose an integer i such that 1 <= i < n and nums[i] > 0.
#     Decrease nums[i] by 1.
#     Increase nums[i - 1] by 1.

# Return the minimum possible value of the maximum integer of nums after performing any number of operations.

from math import ceil

def minimizeArrayValue(nums):
    res = 0
    prefixSum = 0
    for i in range(len(nums)):
        prefixSum += nums[i]
        res = max(res, ceil(prefixSum / (i + 1)))
    return res

nums = [3,7,1,6]
# nums = [10,1]

print(minimizeArrayValue(nums))