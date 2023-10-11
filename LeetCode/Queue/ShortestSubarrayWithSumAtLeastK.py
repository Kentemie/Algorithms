# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with
# a sum of at least k. If there is no such subarray, return -1.

# A subarray is a contiguous part of an array.

from collections import deque 

def shortestSubarray(nums, k):
    def clean(i):
        nonlocal res
        # opt(y) = largest x with Px <= Py - K
        while queue and prefSum[i] <= prefSum[queue[-1]]:
            queue.pop()

        while queue and prefSum[i] - prefSum[queue[0]] >= k:
            res = min(res, i - queue.popleft())

    prefSum = [0]
    res = len(nums) + 1

    for num in nums:
        prefSum.append(prefSum[-1] + num)

    queue = deque()

    for i in range(len(prefSum)):
        clean(i)
        queue.append(i)
    
    return res if res != len(nums) + 1 else -1

k = 167
nums = [84,-37,5,27,40,95,32]

print(shortestSubarray(nums, k))