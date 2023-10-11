# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such
# that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k 
# is satisfied.

# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the 
# remaining elements in their original order.

from collections import deque

def constrainedSubsetSum(nums, k):
    def clean(i):
        if queue and queue[0] == i - k:
            queue.popleft()
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
    
    queue = deque()
    res = float("-inf")

    for i in range(len(nums)):
        nums[i] += nums[queue[0]] if queue else 0
        clean(i)
        if nums[i] > 0:
            queue.append(i)
        res = max(res, nums[i])
        print(nums, queue)

    return res


nums = [10,2,-10,5,20]
k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].

nums = [-1,-2,-3]
k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.

nums = [10,-2,-10,-5,20]
k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].

print(constrainedSubsetSum(nums, k))