# Given an integer array nums of unique elements, return all possible subsets (the power set).
# A subset of an array is a selection of elements (possibly none) of the array.

# The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(nums):
    res = [[]]
    def backTracking(i, curr):
        for j in range(i, len(nums)):
            curr.append(nums[j])
            res.append(list(curr))
            backTracking(j + 1, curr)
            curr.pop()
    backTracking(0, [])
    return res

nums = [1,2,3]
# nums = [0]

print(subsets(nums))