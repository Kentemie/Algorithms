# You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.
# You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:
#     Choose one integer x from either the start or the end of the array nums.
#     Add multipliers[i] * x to your score.
#     Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
#     Remove x from nums.
# Return the maximum score after performing m operations.

nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]

n = len(nums)
m = len(multipliers)
memo = {}

def maxScore(op, left):
    if op == m:
        return 0
    if (op, left) in memo:
        return memo[(op, left)]

    l = nums[left] * multipliers[op] + maxScore(op+1, left+1)
    r = nums[(n-1)-(op-left)] * multipliers[op] + maxScore(op+1, left)
    memo[(op, left)] = max(l, r)

    return memo[(op, left)]

print(maxScore(0, 0))