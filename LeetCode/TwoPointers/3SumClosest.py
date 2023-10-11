# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is 
# closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    diff = float('inf')

    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            tripletSum = nums[i] + nums[j] + nums[k]
            if abs(target - tripletSum) < abs(diff):
                diff = target - tripletSum
            if tripletSum < target:
                j += 1
            else:
                k -= 1
        if diff == 0:
            break
    return target - diff

nums = [-1,2,1,-4]
target = 1

print(threeSumClosest(nums, target))