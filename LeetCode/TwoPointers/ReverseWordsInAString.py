# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should 
# only have a single space separating the words. Do not include any extra spaces.

def trim_spaces(s):
    left, right = 0, len(s) - 1

    while left <= right and s[left] == " ":
        left += 1

    while left <= right and s[right] == " ":
        right -= 1

    output = []

    while left <= right:
        if s[left] != " ":
            output.append(s[left])
        elif output[-1] != " ":
            output.append(s[left])
        left += 1

    return output

def reverse(rev_s, left, right):
    while left < right:
        rev_s[left], rev_s[right] = rev_s[right], rev_s[left]
        left, right = left + 1, right - 1

def reverse_each_word(rev_s):
    n = len(rev_s)
    start = end = 0
    while start < n:
        while end < n and rev_s[end] != " ":
            end += 1
        reverse(rev_s, start, end - 1)
        start = end + 1
        end += 1

def reverseWords(s):
    rev_s = trim_spaces(s)
    reverse(rev_s, 0, len(rev_s) - 1)
    reverse_each_word(rev_s)
    return "".join(rev_s)

s = "the sky is blue"

print(reverseWords(s))