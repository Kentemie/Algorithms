# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s, t):
    source_len, target_len = len(s), len(t)
    
    if source_len == 0:
        return True
    
    dp = [[0] * (target_len + 1) for _ in range(source_len + 1)]

    for col in range(1, target_len + 1):
        for row in range(1, source_len + 1):
            if s[row - 1] == t[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else: 
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        if dp[source_len][col] == source_len:
            return True
        
    return False

# s = "acb"
# t = "ahbgdc"
#       a  h  b  g  d  c
#   [0, 0, 0, 0, 0, 0, 0]
# a [0, 1, 1, 1, 1, 1, 1]
# c [0, 1, 1, 1, 1, 1, 2]
# b [0, 1, 1, 2, 2, 2, 2]
# In the above graph, we show an example of the dp matrix. For instance, for the element of dp[2][3], it indicates that the 
# maximal number of deletions (i.e. matches) that we can have between the source prefix ac and the target prefix ahb is 1.

s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))