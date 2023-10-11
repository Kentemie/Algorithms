# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
#     Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#     Each vowel 'a' may only be followed by an 'e'.
#     Each vowel 'e' may only be followed by an 'a' or an 'i'.
#     Each vowel 'i' may not be followed by another 'i'.
#     Each vowel 'o' may only be followed by an 'i' or a 'u'.
#     Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

def countVowelPermutation(i, vowel):
    total = 1
    if (i, vowel) in memo:
        return memo[(i, vowel)]
    if i > 1:
        if vowel == 'a':
            total = (countVowelPermutation(i - 1, 'e') + countVowelPermutation(i - 1, 'i') + countVowelPermutation(i - 1, 'u')) % MOD
        elif vowel == 'e':
            total = (countVowelPermutation(i - 1, 'a') + countVowelPermutation(i - 1, 'i')) % MOD
        elif vowel == 'i':
            total = (countVowelPermutation(i - 1, 'e') + countVowelPermutation(i - 1, 'o')) % MOD
        elif vowel == 'o':
            total = (countVowelPermutation(i - 1, 'i')) % MOD
        else: 
            total = (countVowelPermutation(i - 1, 'o') + countVowelPermutation(i - 1, 'i')) % MOD
    memo[(i, vowel)] = total
    return memo[(i, vowel)]


n = 144
MOD = 10 ** 9 + 7
memo = {}

print(sum(countVowelPermutation(n, vowel) for vowel in 'aeiou') % MOD)