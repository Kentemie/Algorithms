# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

def maxDotProduct(nums1, nums2):
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    
    for i in range(len(nums1) + 1):
        dp[i][0] = float('-inf')
    for j in range(len(nums2) + 1):
        dp[0][j] = float('-inf')

    for row in range(1, len(nums1) + 1):
        for col in range(1, len(nums2) + 1):
            val = nums1[row - 1] * nums2[col - 1] + max(dp[row - 1][col - 1], 0)
            dp[row][col] = max(val, dp[row - 1][col], dp[row][col - 1])
    
    return dp[-1][-1]

# nums1 = [2,1,-2,5]
# nums2 = [3,0,-6]
# 18
nums1 = [3,-2]
nums2 = [2,-6,7]
# 21

print(maxDotProduct(nums1, nums2))