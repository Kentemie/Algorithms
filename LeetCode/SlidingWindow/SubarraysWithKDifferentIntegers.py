# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

    # For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

# A subarray is a contiguous part of an array.


# Just need one more step to reach the following equation:
# exactly(K) = atMost(K) - atMost(K-1)

def atMost(nums, k):
    frequency = {}
    count = 0
    distinctCnt = 0
    left = 0

    for right in range(len(nums)):
        frequency[nums[right]] = frequency.get(nums[right], 0) + 1
        if frequency[nums[right]] == 1:
            distinctCnt += 1
        
        while distinctCnt > k:
            frequency[nums[left]] -= 1
            if frequency[nums[left]] == 0:
                distinctCnt -= 1
            left += 1
        
        count += right - left + 1

    return count

def subarraysWithKDistinct(nums, k):
    return atMost(nums, k) - atMost(nums, k - 1)

nums = [1,2,2,1,3]
k = 2
# 6

nums = [1,2,1,3,4]
k = 3
# 3

print(subarraysWithKDistinct(nums, k))