# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

def isUgly(n):
    if n <= 0:
        return False

    def keep_dividing_when_divisible(dividend, divisor):
        while dividend % divisor == 0:
            dividend //= divisor
        return dividend

    for factor in [2, 3, 5]:
        n = keep_dividing_when_divisible(n, factor)

    return n == 1

n = 84

print(isUgly(n))