# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    # '?' Matches any single character.
    # '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

def isMatch(s, p):
    memo = {}

    def removeDuplicateStars(p):
        new_pattern = []
        for char in p:
            if not new_pattern or char != '*':
                new_pattern.append(char)
            elif new_pattern[-1] != '*':
                new_pattern.append(char)
        return "".join(new_pattern)
    
    def DP(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j >= len(new_p):
            return i >= len(s)
        if i < len(s) and (s[i] == new_p[j] or new_p[j] == '?'):
            memo[(i, j)] = DP(i + 1, j + 1)
            return memo[(i, j)]
        if new_p[j] == '*':
            memo[(i, j)] = (i < len(s) and DP(i + 1, j)) or DP(i, j + 1)
            return memo[(i, j)]
        memo[(i, j)] = False 
        return memo[(i, j)]

    new_p = removeDuplicateStars(p)

    return DP(0, 0)

s = "adceb"
p = "*a*b"

print(isMatch(s, p))


# def isMatch(s, p):
#     s_len = len(s)
#     p_len = len(p)
    
#     if s == p or set(p) == {'*'}:
#         return True
#     if s == '' or p == '':
#         return False
    
#     dp = [[False] * (s_len + 1) for _ in range(p_len + 1)]
#     dp[0][0] = True

#     for p_idx in range(1, p_len + 1):
#         if p[p_idx - 1] == '*':
#             s_idx = 1
#             while not dp[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
#                 s_idx += 1
#             dp[p_idx][s_idx - 1] = dp[p_idx - 1][s_idx - 1]
#             while s_idx < s_len + 1:
#                 dp[p_idx][s_idx] = True
#                 s_idx += 1
#         elif p[p_idx - 1] == '?':
#             for s_idx in range(1, s_len + 1):
#                 dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1]
#         else:
#             for s_idx in range(1, s_len + 1):
#                 dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1] and s[s_idx - 1] == p[p_idx - 1]

#     return dp[-1][-1]

# s = "abceb"
# p = "*a*b"

# print(isMatch(s, p))