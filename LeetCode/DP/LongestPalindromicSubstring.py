# Given a string s, return the longest palindromic substring in s.


# # Naive approach for Longest Palindromic Substring:
# # Time complexity: O(N3). Three nested loops are needed to find the longest palindromic substring in this approach.
# # Auxiliary complexity: O(1). As no extra space is needed.

# def LPS(ss):

#     n = len(ss)
#     maxLength = 1
#     start = 0

#     for i in range(n):
#         for j in range(i, n):
#             flag = True

#             # Check palindrome
#             for k in range(0, ((j - i) // 2) + 1):
#                 if ss[i + k] != ss[j - k]:
#                     flag = not flag
#                     break

#             # Palindrome
#             if flag and (j - i + 1) > maxLength:
#                 start = i
#                 maxLength = j - i + 1

#     return start, maxLength

# ss = "cbbd"

# start, maxlen = LPS(ss)

# print(ss[start:start + maxlen])




# # Dynamic Programming approach for Longest Palindromic Substring:

# # Time complexity: O(N2). A nested traversal is needed.
# # Auxiliary Space: O(N2). A matrix of size N*N is needed to store the table.

# def LPS(ss):
#     n = len(ss)

#     table = [[False for _ in range(n)] for _ in range(n)]
    
#     maxLen = 1
#     start = 0

#     i = 0
#     while i < n:
#         table[i][i] = True
#         i += 1

#     i = 0
#     while i < n - 1:
#         if ss[i] == ss[i+1]:
#             table[i][i+1] = True
#             start = i
#             maxLen = 2
#         i += 1

#     k = 3
#     while k <= n:
#         i = 0
#         while i < n - k + 1:
#             j = i + k - 1
#             if table[i+1][j-1] and ss[i] == ss[j]:
#                 table[i][j] = True

#                 if k > maxLen:
#                     start = i
#                     maxLen = k
#             i += 1
#         k += 1
    
#     return start, maxLen

# ss = "babad"
# start, maxLen = LPS(ss)

# print(ss[start:start+maxLen])



# # The idea is to Fix a center and expand in both directions for longer palindromes and keep track of the longest palindrome seen so far.

# # Time complexity: O(n^2), where n is the length of the input string. 
# # Outer Loop that traverses through the entire string, and Inner Loop that is used to expand from i .
# # Auxiliary Space: O(1). 
# # No extra space is needed.

# def LPS(ss):
#     n = len(ss)
#     start = 0
#     maxLen = 1

#     for i in range(n):
#         left = i - 1
#         right = i + 1

#         while right < n and ss[right] == ss[i]:
#             right += 1

#         while left >= 0 and ss[left] == ss[i]:
#             left -= 1

#         while left >= 0 and right < n and ss[right] == ss[left]:
#             left -= 1
#             right += 1

#         length = right - left - 1

#         if length > maxLen:
#             maxLen = length
#             start = left + 1

#     return start, maxLen


# ss = "cbbd"
# start, maxLen = LPS(ss)
# print(ss[start:start+maxLen])



# Manacher's Algorithm

def longestPalindrome(s):
    modified_s = '#' + "#".join(s) + '#'
    n = len(modified_s)
    radius = 0
    center = 0
    palindromes_lengths = [0] * n

    for i in range(n):
        mirror_i = (2 * center) - i

        if i < radius:
            palindromes_lengths[i] = min(radius - i, palindromes_lengths[mirror_i])

        left = i - (1 + palindromes_lengths[i])
        right = i + (1 + palindromes_lengths[i])

        while left >= 0 and right < n and modified_s[left] == modified_s[right]:
            palindromes_lengths[i] += 1
            left -= 1
            right += 1

        if i + palindromes_lengths[i] > radius:
            center = i
            radius = i + palindromes_lengths[i]

    max_len_palindrome = max(palindromes_lengths)
    center_idx = palindromes_lengths.index(max_len_palindrome)
    start_idx = (center_idx - max_len_palindrome) // 2

    return s[start_idx : start_idx + max_len_palindrome]

s = "babad"

print(longestPalindrome(s))