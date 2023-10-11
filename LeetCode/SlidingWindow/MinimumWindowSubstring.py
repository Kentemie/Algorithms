# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

from collections import Counter, defaultdict

def minWindow(s, t):
    charsInSubs = Counter(t)
    # dictionary for counting characters in window
    charsInWindow = defaultdict(int)
    
    # array to keep track of the minimum substring
    res = [float('inf'), None, None]
    left = right = cnt = 0

    while right < len(s):
        charsInWindow[s[right]] += 1
        
        if s[right] in charsInSubs and charsInWindow[s[right]] == charsInSubs[s[right]]:
            cnt += 1
        
        while left <= right and cnt == len(charsInSubs):
            if right - left + 1 < res[0]:
                res = [right - left + 1, left, right]
            charsInWindow[s[left]] -= 1
            if s[left] in charsInSubs and charsInWindow[s[left]] < charsInSubs[s[left]]:
                cnt -= 1
            left += 1
        
        right += 1

    return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))