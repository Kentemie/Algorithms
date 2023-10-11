# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we 
# take them as side lengths of a triangle.

def triangleNumber(nums):
    nums.sort()
    cnt = 0
    for i in range(2, len(nums)):
        cnt += isValidTriangle(i)

    return cnt

def isValidTriangle(i):
    j, k = 0, i - 1
    cnt = 0
    while j < k:
        if nums[j] + nums[k] > nums[i]:
            cnt += k - j
            k -= 1
        else:
            j += 1
    return cnt


nums = [2,2,3,4]
nums = [4,2,3,4]

print(triangleNumber(nums)) 