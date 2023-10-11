# https://medium.com/@tudorache.a.bogdan/string-searching-algorithm-knuth-morris-pratt-d18b9435d4e0


def get_longest_prefix_suffix(s):
    n = len(s)
    lps = [0] * n
    i, j = 1, 0

    while i < n:
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp(s1, s2):
    n, m = len(s1), len(s2)
    
    if n == m and s1 != s2:
        return -1
    if m > n:
        return kmp(s2, s1)
    
    lps = get_longest_prefix_suffix(s2)
    i = j = 0

    while i < n and j < m:
        if s1[i] == s[j]:
            i += 1
            j += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
    
    return -1 if j < m else i - m


s = "aacecaaa#aaacecaa"
s = "abcd#dbca"
print(get_longest_prefix_suffix(s))