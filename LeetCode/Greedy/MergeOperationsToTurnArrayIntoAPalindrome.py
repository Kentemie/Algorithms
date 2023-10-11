# You are given an array nums consisting of positive integers.

# You can perform the following operation on the array any number of times:

    # Choose any two adjacent elements and replace them with their sum.
        # For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].

# Return the minimum number of operations needed to turn the array into a palindrome.


def minimumOperations(nums):
    left, right = 0, len(nums) - 1
    res = 0
    while left < right:
        if nums[left] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] + nums[left + 1] < nums[right - 1] + nums[right]:
            nums[left + 1] += nums[left]
            left += 1
            res += 1
        else:
            nums[right - 1] += nums[right]
            right -= 1
            res += 1
    return res


nums = [4,3,2,1,2,3,1]