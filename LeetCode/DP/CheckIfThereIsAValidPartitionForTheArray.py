# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

    # The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
    # The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
    # The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. 
    # For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.

# Return true if the array has at least one valid partition. Otherwise, return false.


def validPartition(nums):
    memo = {}

    def DFS(i):
        if i == len(nums):
            return True
        if i in memo:
            return memo[i]
        
        res = False

        if i < len(nums) - 1 and nums[i] == nums[i + 1]:
            res = DFS(i + 2)
        if i < len(nums) - 2:
            if (nums[i] == nums[i + 1] == nums[i + 2] or 
                nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1):
                res = res or DFS(i + 3)

        memo[i] = res

        return res
    
    return DFS(0)


nums = [4,4,4,5,6]

print(validPartition(nums))