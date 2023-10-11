# def LongestCommonSubsequence(text1, text2):
    # text1_len, text2_len = len(text1), len(text2)

    # dp = [[0] * (text1_len + 1) for _ in range(text2_len + 1)]

    # for col in range(1, text1_len + 1):
    #     for row in range(1, text2_len + 1):
    #         if text2[row - 1] == text1[col - 1]:
    #             dp[row][col] = dp[row - 1][col - 1] + 1
    #         else:
    #             dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # return dp[-1][-1]


# text1 = "aef"
# text2 = "abcdef" 

# print(LongestCommonSubsequence(text1, text2))


def LCS(i, j):
    if i >= len(text1) or j >= len(text2):
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if text1[i] == text2[j]:
        memo[(i, j)] = 1 + LCS(i + 1, j + 1)
    else:
        memo[(i, j)] = max(LCS(i + 1, j), LCS(i, j + 1))

    return memo[(i, j)]

memo = {}

text1 = "abcde"
text2 = "ace" 
# 3
text1 = "abc"
text2 = "abc"
# 3
# text1 = "abc"
# text2 = "def"
# 0

print(LCS(0, 0))
