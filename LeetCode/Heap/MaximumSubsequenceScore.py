# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a 
# subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

    # The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
    # It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).

# Return the maximum possible score.

# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.


from heapq import heappop, heappush

def maxScore(nums1, nums2, k):
    pairs = [(num1, num2) for num1, num2 in zip(nums1, nums2)]
    pairs.sort(key=lambda x: x[1], reverse=True)

    heap = []
    curr_sum = max_sum = 0

    for num1, num2 in pairs:
        curr_sum += num1
        heappush(heap, num1)

        if len(heap) > k:
            n1 = heappop(heap)
            curr_sum -= n1
        if len(heap) == k:
            max_sum = max(max_sum, curr_sum * num2)
    
    return max_sum

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1

nums1 = [2,1,14,12]
nums2 = [11,7,13,6]
k = 3

print(maxScore(nums1, nums2, k))