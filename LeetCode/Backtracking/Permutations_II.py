# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

from collections import Counter

def permuteUnique(nums):
    res = []

    def backTracking(curr, counter):
        if len(curr) == len(nums):
            res.append(curr[:])
        for num in counter:
            if counter[num] > 0:
                curr.append(num)
                counter[num] -= 1
                backTracking(curr, counter)
                curr.pop()
                counter[num] += 1
    backTracking([], Counter(nums))

    return res

nums = [1,1,2]

print(permuteUnique(nums))