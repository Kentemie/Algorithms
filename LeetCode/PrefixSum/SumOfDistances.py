# You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the
# sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

# Return the array arr.

from collections import defaultdict

def distance(nums):
    indexMapping = defaultdict(list)
    arr = [0] * len(nums)
    for i in range(len(nums)):
        indexMapping[nums[i]].append(i)
    for _, indices in indexMapping.items():
        n = len(indices)
        prefSum = 0
        leftCnt = 0
        rightCnt = n - 1
        for j in range(n):
            if j == 0:
                prefSum = sum(indices[1:]) - rightCnt * indices[j]
                rightCnt -= 1
            else:
                diff = indices[j] - indices[j - 1]
                prefSum -= rightCnt * diff
                prefSum += leftCnt * diff
                rightCnt -= 1
                leftCnt += 1
            arr[indices[j]] = prefSum
    return arr

# nums = [1,3,1,1,2]
nums = [2,1,3,1,2,3,3,2,2]
# nums = [0,5,3]

print(distance(nums))