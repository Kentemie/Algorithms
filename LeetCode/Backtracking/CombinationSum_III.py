# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    # Only numbers 1 through 9 are used.
    # Each number is used at most once.

# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the 
# combinations may be returned in any order.

k = 3
n = 7

k = 3
n = 9

# k = 4
# n = 1

def comb(k, n):
    res = []
    def backTracking(k, n, curr, i):
        if n == 0 and k == 0:
            res.append(list(curr))
        if n < 0:
            return 
        for num in range(i, 10):
            curr.append(num)
            backTracking(k - 1, n - num, curr, num + 1)
            curr.pop()
    backTracking(k, n, [], 1)
    return res


print(comb(k, n))