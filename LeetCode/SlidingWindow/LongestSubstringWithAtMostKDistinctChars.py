# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

def lengthOfLongestSubstringKDistinct(s, k):
    frequency = {}
    left = 0
    maxLen = 0

    for right in range(len(s)):
        frequency[s[right]] = right
        if len(frequency) > k:
            idx = min(frequency.values())
            del frequency[s[idx]]
            left = idx + 1
        maxLen = max(maxLen, (right - left + 1))

    return maxLen

s = "eceba"
k = 2

print(lengthOfLongestSubstringKDistinct(s, k))