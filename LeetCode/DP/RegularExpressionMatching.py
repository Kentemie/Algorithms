# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    # '.' Matches any single character.​​​​
    # '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

def isMatch(s, p):
    # TOP-DOWN Memoization
    memo = {}

    def DP(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        _match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if (j + 1) < len(p) and p[j + 1] == '*':
            memo[(i, j)] = (DP(i, j + 2) or            # use *
                    _match and DP(i + 1, j))           # do not use * 
            return memo[(i, j)]
        if _match:
            memo[(i, j)] = DP(i + 1, j + 1)
            return memo[(i, j)]
        memo[(i, j)] = False
        return memo[(i, j)]
    
    return DP(0, 0)

s = "aa"
p = "a"

print(isMatch(s, p))