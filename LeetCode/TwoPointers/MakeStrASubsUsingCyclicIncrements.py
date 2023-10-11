# You are given two 0-indexed strings str1 and str2.

# In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character 
# cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

# Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

# Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the
# characters without disturbing the relative positions of the remaining characters.


def canMakeSubsequence(str1, str2):
    i, j = 0, 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j] or chr((ord(str1[i]) - 96) % 26 + 97) == str2[j]:
            i += 1
            j += 1
        else:
            i += 1
    
    if j == len(str2):
        return True

    return False

str1 = "ab"
str2 = "d"

str1 = "eao"
str2 = "ofa"

str1 = "abc"
str2 = "ad"

str1 = "zc"
str2 = "ad"

print(canMakeSubsequence(str1, str2))