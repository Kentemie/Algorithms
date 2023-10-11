# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing 
# the order of the remaining elements.

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


s = 'bbbab'
memo = {}

print(LPS(0, len(s) - 1))