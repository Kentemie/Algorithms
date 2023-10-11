# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) 
# on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

#     nums1[i] == nums2[j], and
#     the line we draw does not intersect any other connecting (non-horizontal) line.

# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

# def maxUncrossedLines(nums1, nums2):
#     dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]
#     for col in range(1, len(nums1) + 1):
#         for row in range(1, len(nums2) + 1):
#             if nums2[row - 1] == nums1[col - 1]:
#                 dp[row][col] = dp[row - 1][col - 1] + 1
#             else:
#                 dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
#     return dp[-1][-1]

# # nums1 = [1,4,2]
# # nums2 = [1,2,4]
# # 2
# # nums1 = [2,5,1,2,5]
# # nums2 = [10,5,2,1,5,2]
# # 3
# nums1 = [1,3,7,1,7,5]
# nums2 = [1,9,2,5,1]
# # 2

# print(maxUncrossedLines(nums1, nums2))


def maxUncrossedLines(i, j):
    if i <= 0 or j <= 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if nums1[i - 1] == nums2[j - 1]:
        memo[(i, j)] = 1 + maxUncrossedLines(i - 1, j - 1)
    else:
        memo[(i, j)] = max(maxUncrossedLines(i - 1, j), maxUncrossedLines(i, j - 1))
    return memo[(i, j)]

memo = {}

nums1 = [1,4,2]
nums2 = [1,2,4]

print(maxUncrossedLines(len(nums1), len(nums2)))