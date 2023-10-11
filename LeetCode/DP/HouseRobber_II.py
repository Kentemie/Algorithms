# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two 
# adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
# you can rob tonight without alerting the police.

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp1 = [0] * len(nums)
    dp2 = [0] * len(nums)

    def robTwice(i, n, dp, nums):
        dp[i] = nums[i]
        dp[i + 1] = max(dp[i], nums[i + 1])
        for j in range(i + 2, n):
            dp[j] = max(dp[j - 1], dp[j - 2] + nums[j])

    robTwice(0, len(nums) - 2, dp1, nums)
    robTwice(1, len(nums) - 1, dp2, nums)

    return max(dp1[-2], dp2[-1])


nums = [2,3,2]
# 3
# You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

print(rob(nums))