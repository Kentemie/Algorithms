# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted 
# without changing the relative order of the remaining characters.

    # For example, "ace" is a subsequence of "abcde".

from collections import Counter

def countPalindromicSubsequence(s):
    res = set() # (mid, outer), at most 26^2 palindromes
    left = set()
    right = Counter(s)

    for i in range(len(s)):
        right[s[i]] -= 1
        if right[s[i]] == 0:
            right.pop(s[i])
        for j in range(26):
            char = chr(97 + j)
            if char in left and char in right:
                res.add(char + s[i] + char) # res.add((s[i], char))
        left.add(s[i])
    
    return len(res)

# def countPalindromicSubsequence(s):
#     res = 0 

#     for i in range(26):
#         char = chr(i + 97)
#         i, j = s.find(char), s.rfind(char)
#         if i != -1:
#             res += len(set(s[i + 1: j]))

#     return res


s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")

s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

s = "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"
# 161

# print(countPalindromicSubsequence(s))