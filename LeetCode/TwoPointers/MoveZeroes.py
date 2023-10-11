# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(nums) -> None:
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1

nums = [0,1,0,3,12]

moveZeroes(nums)

print(nums)