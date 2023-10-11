# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def countSort(nums, n):
    maxElem = max(nums)
    minElem = min(nums)
    maxRange = maxElem - minElem + 1
    countArr = [0] * maxRange
    outputArr = [0] * n

    for num in nums:
        countArr[num - minElem] += 1

    startingIndex = 0

    for i, cnt in enumerate(countArr):
        countArr[i] = startingIndex
        startingIndex += cnt
    
    for num in nums:
        outputArr[countArr[num - minElem]] = num
        countArr[num - minElem] += 1

    for i in range(n):
        nums[i] = outputArr[i]

def threeSum(nums):
    n = len(nums)
    countSort(nums, n)
    res = []
    for i in range(n):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSum(i, n, res)
    return res

def twoSum(i, n, res):
    j, k = i + 1, n - 1
    while j < k:
        tripletSum = nums[i] + nums[j] + nums[k]
        if tripletSum > 0:
            k -= 1
        elif tripletSum < 0:
            j += 1
        else:
            res.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
            while j < k and nums[j] == nums[j - 1]:
                j += 1

nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [0,0,0]

print(threeSum(nums))