# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

def LCS(s1, s2):
    dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    
    for i in range(1, len(s2) + 1):
        dp[i][0] = dp[i - 1][0] + ord(s2[i - 1])
    for j in range(1, len(s1) + 1):
        dp[0][j] = dp[0][j - 1] + ord(s1[j - 1])

    for row in range(1, len(s2) + 1):
        for col in range(1, len(s1) + 1):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = min(dp[row - 1][col] + ord(s2[row - 1]), dp[row][col - 1] + ord(s1[col - 1]))

    return dp[-1][-1]


s1 = "sea"
s2 = "eat"
# s1 = "delete"
# s2 = "leet"

print(LCS(s1, s2))