# Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. 
# The two subsequences are disjoint if they do not both pick a character at the same index.

# Return the maximum possible product of the lengths of the two palindromic subsequences.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the
# order of the remaining characters. A string is palindromic if it reads the same forward and backward.

def maxProduct(s):

    def backTrack(i, curr1, curr2):
        if i == len(s):
            if curr1 == curr1[::-1] and curr2 == curr2[::-1]:
                return len(curr1) * len(curr2)
            else:
                return 0
        
        if (i, curr1, curr2) in memo:
            return memo[(i, curr1, curr2)]
        
        best = backTrack(i + 1, curr1, curr2)
        best = max(best, backTrack(i + 1, curr1 + s[i], curr2))
        best = max(best, backTrack(i + 1, curr1, curr2 + s[i]))
        memo[(i, curr1, curr2)] = best

        return memo[(i, curr1, curr2)]
    
    memo = {}
    return backTrack(0, "", "")


s = "leetcodecom"

print(maxProduct(s))