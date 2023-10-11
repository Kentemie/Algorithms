# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them,
# the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

def maxChunksToSorted(arr):
    res = currMax = 0
    for i, num in enumerate(arr):
        currMax = max(currMax, num)
        if currMax == i:
            res += 1
    return res


arr = [4,3,2,1,0]
# 1
arr = [1,0,2,3,4]
# 4

print(maxChunksToSorted(arr))