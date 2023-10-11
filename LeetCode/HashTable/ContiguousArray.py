# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

def findMaxLength(nums):
    hashMap = {0: -1}
    cnt = maxLen = 0
    for i in range(len(nums)):
        cnt += 1 if nums[i] == 1 else -1
        if cnt in hashMap:
            maxLen = max(maxLen, i - hashMap[cnt])
        else:
            hashMap[cnt] = i
    return maxLen

nums = [0,1,1,1,1,1,1,1,0,0]
nums = [0,0,1,0,0,0,1,1]

print(findMaxLength(nums))