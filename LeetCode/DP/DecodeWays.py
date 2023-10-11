# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#     'A' -> "1"
#     'B' -> "2"
#     ...
#     'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping 
# above (there may be multiple ways). For example, "11106" can be mapped into:
#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.

# def numDecodings(idx): 
#     if idx in memo:
#         return memo[idx]
#     if idx == len(s):
#         return 1
#     if s[idx] == '0':
#         return 0
#     if idx == len(s) - 1:
#         return 1
#     res = numDecodings(idx + 1)
#     if int(s[idx:idx + 2]) <= 26:
#         res += numDecodings(idx + 2)
#     memo[idx] = res
#     return res

# s = "12"
# memo = {}

# print(numDecodings(0))


def numDecodings(s):
    if s[0] == '0':
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(s) + 1):
        single = int(s[i - 1])
        double = int(s[i - 2 : i])
        if 1 <= single <= 9:
            dp[i] += dp[i - 1]
        if 10 <= double <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]

s = '12306'

print(numDecodings(s))