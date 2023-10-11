# # You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint 
# # stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police 
# # if two adjacent houses were broken into on the same night.
# # Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without 
# # alerting the police.

# def rob(nums):
#     profit = [0] * (len(nums) + 1)
#     profit[1] = nums[0]
#     for i in range(2, len(nums) + 1):
#         profit[i] = max(profit[i - 2] + nums[i - 1], profit[i - 1])
#     return profit[-1]


# nums = [2,1,1,2]
# print(rob(nums))    

def dp(n):
    if n == 0:
        return nums[0]
    if n == 1:
        return max(nums[0], nums[1])
    if n not in memo:
        memo[n] = max(dp(n-2) + nums[n], dp(n-1))
    return memo[n]

memo = {}
nums = [2,1,1,2]
print(dp(len(nums) - 1))