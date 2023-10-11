# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

def combine(n, k):
    res = []
    def backTracking(curr, k, j):
        if k == 0:
            res.append(list(curr))
            return 
        for i in range(j, n + 1):
            curr.append(i)
            backTracking(curr, k - 1, i + 1)
            curr.pop()
    backTracking([], k, 1)
    return res

n = 4
k = 2
# n = 1
# k = 1

print(combine(n, k))