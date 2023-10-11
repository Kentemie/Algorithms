# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, 
# each subarray has their values changed to become the maximum value of that subarray.

def dp(i, j, maxElem):
    if i == len(arr):
        return j * maxElem
    if (i, j, maxElem) in memo:
        return memo[(i, j, maxElem)]
    if j < k:
        do_something = dp(i + 1, j + 1, max(maxElem, arr[i]))
    else: 
        do_something = 0
    
    do_nothing = dp(i + 1, 1, arr[i]) + maxElem * j
    
    memo[(i, j, maxElem)] = max(do_nothing, do_something)

    return memo[(i, j, maxElem)]


arr = [1,15,7,9,2,5,10]
k = 3

memo = {}

print(dp(1, 1, arr[0]))