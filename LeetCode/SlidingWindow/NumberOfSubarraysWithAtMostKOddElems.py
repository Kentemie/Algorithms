# Given an integer array nums, find number of distinct contiguous subarrays with at most k odd elements. Two subarrays
# are distinct when they have at least one different element.

def numOfSubarraysWithAtMostKOddElems(nums, k):
    left = right = odd_num = 0
    res = set()

    while right < len(nums):
        if nums[right] % 2 == 1:
            odd_num += 1
        
        while odd_num > k:
            if nums[left] % 2 == 1:
                odd_num -= 1
            left += 1
        
        for i in range(left, right + 1):
            res.add(tuple(nums[i : right + 1]))
        
        right += 1
    
    return len(res)

nums = [3, 2, 3, 4]
k = 1
# Output: 7 
# [3], [2], [4], [3, 2], [2, 3], [3, 4], [2, 3, 4]
# Note we did not count [3, 2, 3] since it has more than k odd elements.

nums = [1, 3, 9, 5]
k = 2
# Output: 7
# Explanation: [1], [3], [9], [5], [1, 3], [3, 9], [9, 5]

nums = [3, 2, 3, 2]
k = 1
# Output: 5
# Explanation: [3], [2], [3, 2], [2, 3], [2, 3, 2]
# [3], [2], [3, 2] - duplicates
# [3, 2, 3], [3, 2, 3, 2] - more than k odd elements

nums = [2, 2, 5, 6, 9, 2, 11, 9, 2, 11, 12]
k = 1
# Output: 18

print(numOfSubarraysWithAtMostKOddElems(nums, k))