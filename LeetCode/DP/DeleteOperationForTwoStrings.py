# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

# def minDistance(word1, word2):
#     dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

#     for col in range(1, len(word1) + 1):
#         for row in range(1, len(word2) + 1):
#             if word1[col - 1] == word2[row - 1]:
#                 dp[row][col] = dp[row - 1][col - 1] + 1
#             else:
#                 dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

#     return (len(word1) - dp[-1][-1]) + (len(word2) - dp[-1][-1])

# word1 = "sea"
# word2 = "eat"

# print(minDistance(word1, word2))


def dp(word1, word2):
    dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
    
    for i in range(1, len(word2) + 1):
        dp[i][0] = i
    for j in range(1, len(word1) + 1):
        dp[0][j] = j
    
    for row in range(1, len(word2) + 1):
        for col in range(1, len(word1) + 1):
            if word1[col - 1] == word2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

    return dp[-1][-1]

word1 = "leetcode"
word2 = "etco"
word1 = "delete"
word2 = "leet"

print(dp(word1, word2))