# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
# substrings respectively, such that:
#     s = s1 + s2 + ... + sn
#     t = t1 + t2 + ... + tm
#     |n - m| <= 1
#     The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.


def isInterleave(s1, s2, s3):
    s3Len = len(s3)
    s2Len = len(s2)
    s1Len = len(s1)

    if s3Len != s2Len + s1Len:
        return False
    
    dp = [[False] * (s2Len + 1) for _ in range(s1Len + 1)]
    # dp = [False for _ in range(s2Len + 1)]

    for row in range(s1Len + 1):
        for col in range(s2Len + 1):
            if row == 0 and col == 0:
                dp[row][col] = True
                # dp[col] = True
            elif row == 0:
                dp[row][col] = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                # dp[col] = dp[col - 1] and s2[col - 1] == s3[row + col - 1]
            elif col == 0:
                dp[row][col] = dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]
                # dp[col] = dp[col] and s1[row - 1] == s3[row + col - 1]
            else:
                dp[row][col] = (dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]) or (dp[row - 1][col] and s1[row - 1] == s3[row + col - 1])
                # dp[col] = (dp[col - 1] and s2[col - 1] == s3[row + col - 1]) or (dp[col] and s1[row - 1] == s3[row + col - 1])
    return dp[-1][-1]
    # return dp[-1]

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

print(isInterleave(s1, s2, s3))