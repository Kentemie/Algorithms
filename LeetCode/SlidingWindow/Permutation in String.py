# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

def checkInclusion(s1, s2):
    count_s1 = [0] * 26 
    count_s2 = [0] * 26 

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1
    
    for i, char in enumerate(s2):
        count_s2[ord(char) - ord('a')] += 1
        
        if i >= len(s1):
            count_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        if count_s1 == count_s2:
            return True
        
    return False


s1 = "ab"
s2 = "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

print(checkInclusion(s1, s2))