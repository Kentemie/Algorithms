# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    n = len(nums)
    k %= n

    for i in range((n - k) // 2):
        nums[i], nums[n - k - 1 - i] = nums[n - k - 1 - i], nums[i]
    for i in range(k // 2):
        nums[n - k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[n - k + i]
    for i in range(n // 2):
        nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

nums = [1,2,3,4,5,6,7]
k = 3

nums = [-1,-100,3,99]
k = 6

rotate(nums, k)
print(nums)