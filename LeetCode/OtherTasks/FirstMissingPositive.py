# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

def firstMissingPositive(nums):
    n = len(nums)
        
    # Base case.
    if 1 not in nums:
        return 1
    
    # Replace negative numbers, zeros,
    # and numbers larger than n by 1s.
    # After this convertion nums will contain 
    # only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    for i in range(n):
        idx = abs(nums[i])
        if idx == n:
            nums[0] = -abs(nums[0])
        else:
            nums[idx] = -abs(nums[idx])

    for i in range(1, n):
        if nums[i] > 0:
            return i
    
    if nums[0] > 0:
        return n
    
    return n + 1

nums = [7,8,9,11,12]

nums = [1,2,0]

nums = [3,4,-1,1]

print(firstMissingPositive(nums))