# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

def longestConsecutive(nums):
    nums = set(nums)
    cnt = 0
    for num in nums:
        if num - 1 not in nums:
            currNum = num
            currCnt = 1
            while currNum + 1 in nums:
                currCnt += 1
                currNum += 1
            cnt = max(cnt, currCnt)
    return cnt

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

print(longestConsecutive(nums))