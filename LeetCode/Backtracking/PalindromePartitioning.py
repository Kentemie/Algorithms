# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible 
# palindrome partitioning of s.

def partition(s):
    def backTrack(start, curr):
        if start == len(s):
            res.append(list(curr))
        for end in range(start, len(s)):
            if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                dp[start][end] = True 
                curr.append(s[start:end + 1])
                backTrack(end + 1, curr)
                curr.pop()
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = []
    backTrack(0, [])
    return res

s = "aab"

print(partition(s))