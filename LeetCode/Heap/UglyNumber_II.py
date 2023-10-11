# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

from heapq import heappop, heappush

def nthUglyNumber(n):
    seen = set()
    uglyNums = [1]

    while n:
        res = heappop(uglyNums)
        n -= 1
        for factor in [2, 3, 5]:
            new_ugly = res * factor
            if new_ugly not in seen:
                heappush(uglyNums, new_ugly)
                seen.add(new_ugly)

    return res 

n = 1690

print(nthUglyNumber(n))