# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

def LPS(i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if (i, j) in memo:
        return memo[(i, j)]
    if s[i] == s[j]:
        memo[(i, j)] = LPS(i + 1, j - 1) + 2
    else:
        memo[(i, j)] = max(LPS(i + 1, j), LPS(i, j - 1))
    return memo[(i, j)]

# s = "zzazz"
# 0
# s = "mbadm"
# 2
s = "leetcode"
# 5

n = len(s)
memo = {}
palindromeSubsLen = LPS(0, n - 1)

print(n - palindromeSubsLen)