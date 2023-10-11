# Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k,
# return the kth missing number starting from the leftmost number of the array.

def missingElement(nums, k):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = right - (right - left) // 2

        if nums[mid] - nums[0] - mid < k:
            left = mid
        else:
            right = mid - 1

    return nums[0] + k + left


nums = [4,7,9,10]
k = 1

# nums = [4,7,9,10]
# k = 3

nums = [1,2,4]
k = 3

print(missingElement(nums, k))