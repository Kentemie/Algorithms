# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

def atMost(nums, k):
    left = odd_num = 0
    res = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            odd_num += 1
        while odd_num > k:
            if nums[left] % 2 == 1:
                odd_num -= 1
            left += 1
        res += right - left + 1
    
    return res

def numberOfSubarrays(nums, k):
    return atMost(nums, k) - atMost(nums, k - 1)

nums = [1,1,2,1,1]
k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# nums = [2,4,6]
# k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.

print(numberOfSubarrays(nums, k))