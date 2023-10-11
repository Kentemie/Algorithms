# You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

    # Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.

# Return the total number of continuous subarrays.

# A subarray is a contiguous non-empty sequence of elements within an array.


from heapq import heappop, heappush

def continuousSubarrays(nums):
    maxHeap = []
    minHeap = []
    left = 0
    res = 0

    for right in range(len(nums)):
        
        while maxHeap and -1 * maxHeap[0][0] - nums[right] > 2:
            left = max(heappop(maxHeap)[1] + 1, left)
        
        while minHeap and nums[right] - minHeap[0][0] > 2:
            left = max(heappop(minHeap)[1] + 1, left)
        
        res += right - left + 1
        heappush(maxHeap, (-1 * nums[right], right))
        heappush(minHeap, (nums[right], right))
    
    return res

nums = [5,4,2,4]
nums = [5,4,2,4,10]
nums = [1,2,3]

print(continuousSubarrays(nums))