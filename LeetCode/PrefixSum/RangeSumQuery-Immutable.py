# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

    # NumArray(int[] nums) Initializes the object with the integer array nums.
    # int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
    # (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    def __init__(self, nums):
        self.prefixSum = self.dp(nums)

    def dp(self, nums):
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] += dp[i - 1] + nums[i - 1]

        return dp

    def sumRange(self, left, right):
        return self.prefixSum[right + 1] - self.prefixSum[left]

nums = [-2, 0, 3, -5, 2, -1]

numArray = NumArray(nums)

print(numArray.prefixSum)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))