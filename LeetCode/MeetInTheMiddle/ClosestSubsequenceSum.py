# You are given an integer array nums and an integer goal.

# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the 
# sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

# Return the minimum possible value of abs(sum - goal).

# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

def search(arr, x):
    l, r = 0, len(arr)

    while l < r:
        mid = (r + l) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    
    return l

def DFS(nums):
    arr = {0}

    for num1 in nums:
        arr |= { num1 + num2 for num2 in arr }

    return arr

def minAbsDifference(nums, goal):
    left = DFS(nums[:len(nums) // 2])
    right = sorted(DFS(nums[len(nums) // 2:]))

    min_diff = float("inf")

    for leftSum in left:
        target = goal - leftSum
        idx = search(right, target)

        if idx < len(right):
            min_diff = min(min_diff, abs(target - right[idx]))
        if idx > 0:
            min_diff = min(min_diff, abs(target - right[idx - 1]))

    return min_diff


nums = [9152249,8464156,-2493402,8990685,-7257152,-1050240,2243737,-82901,8939692]
goal = 26915229
# nums = [5,-7,3,5]
# goal = 6
# nums = [1,2,3]
# goal = -7
# nums = [3346,-3402,-9729,7432,2475,6852,5960,-7497,3229,6713,8949,9156,3945,-8686,1528,5022,-9791,-3782,-191,-9820,7720,-6067,-83,6793,340,7793,8742,8067]
# goal = -20357
nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,-8192,-16384,-32768,-65536,-131072,-262144,-524288]
goal = 1048574

print(minAbsDifference(nums, goal))