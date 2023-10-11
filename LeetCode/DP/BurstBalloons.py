# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
# You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds
# of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

def maxCoins(nums):
    nums = [1] + nums + [1]
    memo = {}

    def DP(l, r):
        if l > r:
            return 0
        if (l, r) in memo:
            return memo[(l, r)]
        
        memo[(l, r)] = 0

        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1] + DP(l, i - 1) + DP(i + 1, r)
            memo[(l, r)] = max(memo[(l, r)], coins)

        return memo[(l, r)]
    
    return DP(1, len(nums) - 2)

nums = [3,1,5,8]
nums = [1,5]

print(maxCoins(nums))