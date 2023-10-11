# Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.

def longestRepeatingSubstring(s):
    hashing = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1] in hashing:
                hashing[s[i:j + 1]] += 1
            else:
                hashing[s[i:j + 1]] = 1
    return hashing

# s = "abcd"
# 0
# s = "abbaba"
# 2
s = "aabcaabdaab"
# 3

hashing = longestRepeatingSubstring(s)
longestSubs = 0

for key in hashing.keys():
    if len(key) > 1 and hashing[key] > 1:
        longestSubs = max(longestSubs, len(key))

print(longestSubs)