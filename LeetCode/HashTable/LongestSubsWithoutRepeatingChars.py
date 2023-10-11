# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    indexMapping = {}
    res = 0
    j = 0

    for i in range(len(s)):
        if s[i] in indexMapping:
            j = max(indexMapping[s[i]], j)
        res = max(res, i - j)
        indexMapping[s[i]] = i

    return res

s = "abcabcbb"
# 3

s = "bbbbb"
# 1

s = "pwwkew"
# 3

print(lengthOfLongestSubstring(s))