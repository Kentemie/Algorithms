# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with 
# at least two elements. You may return the answer in any order.

def findSubsequences(nums):
    res = set()
    seq = []

    def backTrack(i):
        if i == len(nums):
            if len(seq) >= 2:
                res.add(tuple(seq))
            return 
        if not seq or seq[-1] <= nums[i]:
            seq.append(nums[i])
            backTrack(i + 1)
            seq.pop()
        backTrack(i + 1)
    
    backTrack(0)

    return res

# nums = [4,6,7,7]
# nums = [4,4,3,2,1]
nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]

print(findSubsequences(nums))