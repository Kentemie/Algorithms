# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains 
# less than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear extra space.

def maximumGap(nums):
    # Radix Sort
    def countSort(nums, base):
        count_arr = [0] * 10
        output_arr = [0] * len(nums)

        for num in nums:
            digit = (num // base) % 10
            count_arr[digit] += 1
        
        starting_idx = 0
        for idx, cnt in enumerate(count_arr):
            count_arr[idx] = starting_idx
            starting_idx += cnt
        
        for num in nums:
            digit = (num // base) % 10
            output_arr[count_arr[digit]] = num
            count_arr[digit] += 1

        for i in range(len(nums)):
            nums[i] = output_arr[i]

    def radixSort(nums):
        base = 1
        max_elem = max(nums)

        while base <= max_elem:
            countSort(nums, base)
            base *= 10

        return nums
    
    if len(nums) < 2:
        return 0
    
    gap = 0
    radixSort(nums)

    for i in range(1, len(nums)):
        gap = max(gap, nums[i] - nums[i - 1])

    return gap
    

nums = [3,6,9,1]

print(maximumGap(nums))