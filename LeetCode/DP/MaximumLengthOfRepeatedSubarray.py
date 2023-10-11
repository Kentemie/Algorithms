# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

# nums1 = [1,2,3,2,1]
# nums2 = [3,2,1,4,7]
# 3
# nums1 = [0,0,0,0,0]
# nums2 = [0,0,0,0,0]
# 5
nums1 = [0,1,1,1,1]
nums2 = [1,0,1,0,1]
# 2

dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
maxLen = 0
for i in range(1, len(nums1) + 1):
    for j in range(1, len(nums2) + 1):
        if nums1[i - 1] == nums2[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] + 1
            maxLen = max(maxLen, dp[i][j])

print(maxLen)