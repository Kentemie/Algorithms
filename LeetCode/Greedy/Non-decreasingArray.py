# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def checkPossibility(nums):
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if cnt == 1:
                return False
            cnt += 1
            if i < 2 or nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return True

nums = [4,2,3]
nums = [4,2,1]
nums = [3,4,2,3]
nums = [1,1,1]
nums = [1,4,1,2]

print(checkPossibility(nums))