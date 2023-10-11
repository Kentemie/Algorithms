# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2 # A
        j = half - i - 2 # B, we subtract 2 cause array indexing starts at 0

        ALeft = A[i] if i >= 0 else float("-inf")
        ARight = A[i + 1] if (i + 1) < len(A) else float("inf") 
        BLeft = B[j] if j >= 0 else float("-inf")
        BRight = B[j + 1] if (j + 1) < len(B) else float("inf") 

        # partition is correct
        if ALeft <= BRight and BLeft <= ARight:
            # odd
            if total % 2:
                return min(ARight, BRight)
            # even
            return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
        elif ALeft > BRight:
            r = i - 1
        else:
            l = i + 1

nums1 = [1,3,5,6,67]
nums2 = [2,102,113,204]

print(findMedianSortedArrays(nums1, nums2))