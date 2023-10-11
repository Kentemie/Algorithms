# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsetsWithDup(nums):
    res = []
    nums.sort()
    def backTracking(curr, i):
        res.append(curr[:])
        for j in range(i, len(nums)):
            if i != j and nums[j] == nums[j - 1]:
                continue
            curr.append(nums[j])
            backTracking(curr, j + 1)
            curr.pop()
    backTracking([], 0)
    return res

nums = [1,2,2]
# [[], [1], [1,2], [1,2,2], [2], [2,2]]
print(subsetsWithDup(nums))