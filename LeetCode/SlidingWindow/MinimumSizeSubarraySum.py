# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

def minSubArrayLen(target, nums):
    left = prefSum = 0 
    minLen = float("inf")
    
    for i in range(len(nums)):
        prefSum += nums[i]
        while prefSum >= target:
            minLen = min(minLen, (i - left + 1))
            prefSum -= nums[left]
            left += 1

    return minLen if minLen != float("inf") else 0

target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(target, nums))