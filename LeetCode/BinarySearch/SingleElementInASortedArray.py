# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which
# appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

def singleNonDuplicate(nums):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + ((r - l) // 2)
        
        if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 == len(nums) or nums[mid] != nums[mid + 1]):
            return nums[mid]

        left_size = mid - 1 if nums[mid - 1] == nums[mid] else mid
        
        if left_size % 2:
            r = mid - 1
        else:
            l = mid + 1

nums = [1,1,2,3,3,4,4,8,8]

print(singleNonDuplicate(nums))