# # Given an integer array nums, return the length of the longest strictly increasing subsequence.
# # A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the 
# # remaining elements.

# nums = [10,9,2,5,3,7,101,18]

# dp = [1] * len(nums)

# for i in range(1, len(nums)):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[j] + 1, dp[i])

# print(max(dp))


# Time complexity: O(N^2)
# Space complexity: O(N)

# def lengthOfLIS(nums):
#     subs = [nums[0]]
#     for num in nums[1:]:
#         if num > subs[-1]:
#             subs.append(num)
#         else:
#             i = 0
#             while num > subs[i]:
#                 i += 1
#             subs[i] = num
#     return len(subs)

# nums = [10,9,2,5,3,7,101,18]

# print(lengthOfLIS(nums))


# Time complexity: O(N⋅log⁡(N))
# Space complexity: O(N)

from bisect import bisect_left

def lengthOfLIS(nums):
    subs = []
    
    for num in nums:
        i = bisect_left(subs, num)
        
        if i == len(subs):
            subs.append(num)
        else:
            subs[i] = num

    return len(subs)

nums = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(nums))