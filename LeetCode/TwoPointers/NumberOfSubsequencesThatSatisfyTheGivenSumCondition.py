# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it 
# is less or equal to target. Since the answer may be too large, return it modulo 10^9 + 7.


    # To understand why there are 2^n subsequences in an array of size n, let's consider the number of choices we have 
    # for each element in the array. For each element, we can either include it in a subsequence or exclude it. This 
    # means that for each element, we have two choices: either include it or exclude it.

    # Since we have n elements in the array, and for each element we have two choices, the total number of possible
    # subsequences is calculated by multiplying the number of choices for each element together. Thus, the total 
    # number of subsequences is 2 * 2 * 2 * ... * 2 (n times), which can be written as 2^n.

def numSubseq(nums, target):
    nums.sort()
    MOD = 10 ** 9 + 7

    res = 0
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] + nums[right] <= target:
            res = (res + pow(2, right - left, MOD)) % MOD
            left += 1
        else:
            right -= 1

    return res

nums = [3,5,6,7]
target = 9

nums = [3,3,6,8]
target = 10

print(numSubseq(nums, target))