# You are given two strings s and sub. You are also given a 2D character array mappings where mappings[i] = [oldi, newi] 
# indicates that you may perform the following operation any number of times:

    # Replace a character oldi of sub with newi.

# Each character in sub cannot be replaced more than once.

# Return true if it is possible to make sub a substring of s by replacing zero or more characters according to mappings.
# Otherwise, return false.

# A substring is a contiguous non-empty sequence of characters within a string.

from collections import defaultdict

def matchReplacement(s, sub, mappings):
    mapping = defaultdict(set)
    n = len(s)
    m = len(sub)
    
    for map in mappings:
        mapping[map[0]].add(map[1])

    for i in range(n - m + 1):
        cnt = 0
        for j in range(m):
            if s[i + j] == sub[j] or s[i + j] in mapping[sub[j]]:
                cnt += 1
            else:
                break
        if cnt == m:
            return True
    
    return False

# s = "fool3e7bar"
# sub = "leet"
# mappings = [["e","3"],["t","7"],["t","8"]]

# s = "fooleetbar"
# sub = "f00l"
# mappings = [["o","0"]]

s = "Fool33tbaR"
sub = "leetd"
mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]

print(matchReplacement(s, sub, mappings))