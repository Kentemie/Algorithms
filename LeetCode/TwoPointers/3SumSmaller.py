# Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 
# 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

def threeSumSmaller(nums, target):
    nums.sort()
    cnt = 0
    for i in range(len(nums)):
        cnt += twoSumSmaller(i, target - nums[i])
    
    return cnt

def twoSumSmaller(i, target):
    j = i + 1
    k = len(nums) - 1
    cnt = 0
    while j < k:
        if nums[j] + nums[k] < target:
            cnt += k - j
            j += 1
        else:
            k -= 1
    return cnt

nums = [-2,0,1,3]
target = 2

# nums = []
# target = 0

# nums = [0]
# target = 0

print(threeSumSmaller(nums, target))