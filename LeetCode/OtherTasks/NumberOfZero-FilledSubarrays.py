# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

def zeroFilledSubarray(nums):
    zeroes = res = 0

    for num in nums:
        if num == 0:
            zeroes += 1
        else:
            zeroes = 0
        res += zeroes

    return res


nums = [0,0,0,2,0,0]

print(zeroFilledSubarray(nums))