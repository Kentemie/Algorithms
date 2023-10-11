# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarraySum(nums, k):
    hashmap = {0:1}
    prefSum = 0
    cnt = 0
    for num in nums:
        prefSum += num
        if prefSum - k in hashmap:
            cnt += hashmap[prefSum - k]
        if prefSum not in hashmap:
            hashmap[prefSum] = 1
        else:
            hashmap[prefSum] += 1
    return cnt

nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3

print(subarraySum(nums, k))