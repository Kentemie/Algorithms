# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost
# element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Try to think reversely, instead of finding for the correct prefix + suffix, find the max subarray inside the nums:

def minOperations(nums, x):
    n = len(nums)
    left, pref_sum = 0, 0
    max_window = -1
    target = sum(nums) - x

    for right in range(n):
        pref_sum += nums[right]

        if pref_sum == target:
            max_window = max(max_window, right - left + 1)
        
        while left <= right and pref_sum > target:
            pref_sum -= nums[left]
            left += 1

    return -1 if max_window == -1 else n - max_window

nums = [3,2,20,1,1,3]
x = 10

nums = [5,6,7,8,9]
x = 4

nums = [1,1,4,2,3]
x = 5

nums = [3914]
x = 3913

# nums = [10,1,10,10,10]
# x = 40

# nums = [8576]
# x = 8576

print(minOperations(nums, x))