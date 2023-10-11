# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference 
# amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents
# the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

def minimizeMax(nums, p):
    nums.sort()
    n = len(nums)

    def countValidPairs(threshold):
        idx, cnt = 0, 0

        while idx < n - 1:
            if nums[idx + 1] - nums[idx] <= threshold:
                cnt += 1
                idx += 1
            idx += 1 

        return cnt

    left, right = 0, nums[-1] - nums[0]

    while left < right:
        mid = left + (right - left) // 2

        if countValidPairs(mid) >= p:
            right = mid
        else:
            left = mid + 1

    return left



nums = [10,1,2,7,1,3]
p = 2

print(minimizeMax(nums, p))