# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.

def getMaxLen(nums):
    zeroes = []

    for idx, num in enumerate(nums):
        if num == 0:
            zeroes.append(idx)

    def findMaxPositiveSubarray(nums):
        negatives = []
        n = len(nums)
        
        for idx, num in enumerate(nums):
            if num < 0:
                negatives.append(idx)

        if len(negatives) % 2 == 0:
            return n
        
        return max(n - (n - negatives[-1]), n - negatives[0] - 1)
    
    res = 0
    i = 0

    for j in zeroes:
        res = max(res, findMaxPositiveSubarray(nums[i:j]))
        i = j + 1
    
    res = max(res, findMaxPositiveSubarray(nums[i:]))

    return res

nums = [0,1,-2,-3,-4]
nums = [1,-2,-3,4]
nums = [-1,-2,-3,0,1]

print(getMaxLen(nums))