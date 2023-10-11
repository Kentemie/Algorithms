# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a 
# beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

    # perm[i] is divisible by i.
    # i is divisible by perm[i].

# Given an integer n, return the number of the beautiful arrangements that you can construct.

def countArrangement(n):
    count = 0
    seen = [False] * (n + 1)
    
    def backtracking(pos, seen):
        nonlocal count
        if pos > n:
            count += 1
        for i in range(1, n + 1):
            if not seen[i] and (pos % i == 0 or i % pos == 0):
                seen[i] = True
                backtracking(pos + 1, seen)
                seen[i] = False

    backtracking(1, seen)
    return count 

n = 4

print(countArrangement(n))