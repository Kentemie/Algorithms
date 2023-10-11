# Given two strings s and t, return the number of distinct subsequences of s which equals t.

from functools import lru_cache

@lru_cache(None)
def numDistinct(i, j):
    if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
        return int(j == len(t))
    
    res = numDistinct(i + 1, j)

    if s[i] == t[j]:
        res += numDistinct(i + 1, j + 1)
    
    return res

s = "rabbbit"
t = "rabbit"

print(numDistinct(0, 0))