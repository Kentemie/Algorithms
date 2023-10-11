# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

nums = [1,2,3]

def permute(nums):
    res = []
    def backTracking(curr=[]):
        if len(curr) == len(nums):
            res.append(curr[:])
        for i in range(len(nums)):
            if nums[i] not in curr:
                curr.append(nums[i])
                backTracking(curr)
                curr.pop()
    backTracking()

    return res

print(permute(nums))

# from itertools import permutations
# nums = [1,2,3]
# print(list(map(list, permutations(nums))))