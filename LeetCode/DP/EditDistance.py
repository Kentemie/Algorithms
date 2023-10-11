# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character

# def minDistance(word1, word2):
#     dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
    
#     for i in range(1, len(word2) + 1):
#         dp[i][0] = i
#     for j in range(1, len(word1) + 1):
#         dp[0][j] = j

#     for row in range(1, len(word2) + 1):
#         for col in range(1, len(word1) + 1):
#             if word1[col - 1] == word2[row - 1]:
#                 dp[row][col] = dp[row - 1][col - 1]
#             else:
#                 dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
#     return dp[-1][-1]

# word1 = "horse"
# word2 = "ros"
# word1 = "intention"
# word2 = "execution"

# print(minDistance(word1, word2))


from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if word1[i - 1] == word2[j - 1]:
        return dp(i - 1, j - 1)
    else:
        insert = dp(i, j - 1)
        delete = dp(i - 1, j)
        replace = dp(i - 1, j - 1)
        return min(insert, delete, replace) + 1


word1 = "intention"
word2 = "execution"

print(dp(len(word1), len(word2)))