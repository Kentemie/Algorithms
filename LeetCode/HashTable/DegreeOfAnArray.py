# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any 
# one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

from collections import defaultdict

def findShortestSubArray(nums):
    indexMapping = defaultdict(list)
    arrayDegree = 0
    for i in range(len(nums)):
        indexMapping[nums[i]].append(i)
        arrayDegree = max(arrayDegree, len(indexMapping[nums[i]]))
    minLen = float("inf")
    for _, indices in indexMapping.items():
        if len(indices) != arrayDegree:
            continue
        minLen = min(minLen, indices[-1] - indices[0] + 1)
    return minLen 

nums = [1,2,2,3,1]
nums = [1,2,2,3,1,4,2]

print(findShortestSubArray(nums))