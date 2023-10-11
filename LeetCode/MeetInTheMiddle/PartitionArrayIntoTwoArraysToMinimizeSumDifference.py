# You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the 
# absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

# Return the minimum possible absolute difference.

def search(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

def count_possible_sums(nums):
    possible_sums = {}
    m = len(nums)
    
    for i in range(1 << m):
        _sum = 0
        for j in range(m):
            if (i >> j) & 1:
                _sum += nums[j]
        possible_sums.setdefault(i.bit_count(), []).append(_sum)

    for key, value in possible_sums.items(): # counter of numbers used, possible sums
        possible_sums[key] = sorted(set(value))
    
    return possible_sums

def minimumDifference(nums):
    n = len(nums) // 2
    left_side = count_possible_sums(nums[:n])
    right_side = count_possible_sums(nums[n:])
    goal = sum(nums) // 2 # the best sum required for each, have to find sum nearest to this
    total = sum(nums)

    print(left_side)
    print(right_side)

    res = abs(sum(nums[:n]) - sum(nums[n:]))

    for k, left_sums in left_side.items(): # if taking k no. from left_sums 
        for left_sum in left_sums:
            if (n - k) not in right_side: # then have to take remaining N-k from right_sums.
                break
            right_sums = right_side[n - k]
            target = goal - left_sum
            idx = search(right_sums, target) # find index of value closest to target, present in right_sums, using binary search

            for j in [idx, idx - 1]:
                if 0 <= j < len(right_sums):
                    arr1 = left_sum + right_sums[j]
                    arr2 = total - arr1
                    res = min(res, abs(arr1 - arr2))
                
    return res

nums = [3,9,7,3]
nums = [2,-1,0,4,-2,-9]

print(minimumDifference(nums))