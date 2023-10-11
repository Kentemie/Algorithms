# Given a string s, return the number of palindromic substrings in it.

# def countSubstrings(s):
#     ans = 0
#     for i in range(len(s)):
#         ans += countPalindromesAroundCenter(i, i)
#         ans += countPalindromesAroundCenter(i, i + 1)
#     return ans

# def countPalindromesAroundCenter(left, right):
#     ans = 0
#     while left >= 0 and right < len(s):
#         if s[left] != s[right]:
#             break
#         left -= 1
#         right += 1
#         ans += 1
    
#     return ans 

# s = "aab"
# # 4
# s = "aaa"
# # 6
# print(countSubstrings(s))


def countSubstrings(s):
    dp = [[False] * len(s) for _ in range(len(s))]
    ans = 0

    for i in range(len(s)):
        dp[i][i] = True
        ans += 1
    
    for i in range(len(s) - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        ans += dp[i][i + 1]

    for k in range(3, len(s) + 1):
        for i in range(len(s) - k + 1):
            j = i + k - 1
            dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            ans += dp[i][j]

    return ans

s = "aaa"

print(countSubstrings(s))