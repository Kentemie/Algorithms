# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some 
# integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# import math

# def numSquares(n):
#     square_nums = [i ** 2 for i in range(int(math.sqrt(n)) + 1)]
#     dp = [float('inf')] * (n + 1)
#     dp[0] = 0

#     for i in range(1, n + 1):
#         for square in square_nums:
#             if i < square:
#                 break
#             dp[i] = min(dp[i], dp[i - square] + 1)
#     return dp[-1]

# n = 13

# print(numSquares(n))


# from functools import lru_cache

# @lru_cache(None)
# def dp(n):
#     if n == 0:
#         return 0
#     if n < 0:
#         return -1
#     minNum = float('inf')
#     for square in square_nums[::-1]:
#         res = dp(n - square)
#         if res != -1:
#             minNum = min(minNum, res + 1)
#     return minNum

# n = 9999

# square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

# print(square_nums)
# print(dp(n))


def is_divided_by(n, count):
    if count == 1:
        return n in square_nums
    
    for square in square_nums:
        if is_divided_by(n - square, count - 1):
            return True
    return False 

n = 9999

square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])

for count in range(1, n + 1):
    if is_divided_by(n, count):
        print(count)
        break