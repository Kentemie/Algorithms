# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are 
# lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

def countVowelStrings(i, n):
    if n == 0:
        return 1
    if (i, n) in memo:
        return memo[(i, n)]
    
    total = 0
    
    for j in range(i, len(vowels)):
        total += countVowelStrings(j, n - 1)

    memo[(i, n)] = total

    return memo[(i, n)]

n = 50
vowels = ["a","e","i","o","u"]
memo = {}

print(countVowelStrings(0, n))
