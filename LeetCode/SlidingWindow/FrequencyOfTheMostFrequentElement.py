# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment 
# the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

def maxFrequency(nums, k):
    nums.sort()
    res = windowSum = 0
    left = right = 0
    
    while right < len(nums):
        windowSum += nums[right]
        while nums[right] * (right - left + 1) > windowSum + k:
            windowSum -= nums[left]
            left += 1
        res = max(res, (right - left + 1))
        right += 1
    
    return res

nums = [1,6,6,13]
k = 5

nums = [1,2,4]
k = 5

nums = [3,9,6]
k = 2

nums = [1,1,1,2,2,4]
k = 2

print(maxFrequency(nums, k))