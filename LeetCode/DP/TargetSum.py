# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and 
# then concatenate all the integers.

    # For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
    # expression "+2-1".

# Return the number of different expressions that you can build, which evaluates to target.


from functools import lru_cache

@lru_cache(None)
def dp(i, currSum):
    if i == len(nums):
        if currSum == target:
            return 1
        return 0
    return dp(i + 1, currSum + nums[i]) + dp(i + 1, currSum - nums[i])

nums = [1,1,1,1,1]
target = 3

print(dp(0, 0))