# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the 
# original letters exactly once.

def findAnagrams(s, p):
    pCount = [0] * 26
    sCount = [0] * 26

    for i in range(len(p)):
        pCount[ord(p[i]) - ord('a')] += 1

    res = []

    for i in range(len(s)):
        sCount[ord(s[i]) - ord('a')] += 1
        if i >= len(p):
            sCount[ord(s[i - len(p)]) - ord('a')] -= 1
        if pCount == sCount:
            res.append(i - len(p) + 1)
    
    return res

s = "cbaebabacd"
p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

s = "abab"
p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

print(findAnagrams(s, p)) 