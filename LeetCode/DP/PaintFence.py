# You are painting a fence of n posts with k different colors. You must paint the posts following these rules:
    # Every post must be painted exactly one color.
    # There cannot be three or more consecutive posts with the same color.
# Given the two integers n and k, return the number of ways you can paint the fence.

from functools import lru_cache

@lru_cache(None)
def numWays(i):
    if i == 1:
        return k
    if i == 2:
        return k * k
    return (numWays(i - 1) + numWays(i - 2)) * (k - 1)


n = 7
k = 2
# 42

print(numWays(n))