# You have n dice, and each die has k faces numbered from 1 to k.
# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the 
# sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 10^9 + 7.

from functools import lru_cache

n = 30
k = 30
target = 500
MOD = 10 ** 9 + 7

@lru_cache(None)
def numRollsToTarget(n, target):
    if n == 0:
        return target == 0
    
    total = 0

    for num in range(1, min(k + 1, target + 1)):
        total = (total + numRollsToTarget(n - 1, target - num)) % MOD

    return total

print(numRollsToTarget(n, target))