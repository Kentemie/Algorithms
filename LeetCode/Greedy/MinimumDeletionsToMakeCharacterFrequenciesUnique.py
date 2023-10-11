# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", 
# the frequency of 'a' is 2, while the frequency of 'b' is 1.

def minDeletions(s):
    frequency = [0] * 26

    for char in s:
        frequency[ord(char) - ord('a')] += 1
    frequency.sort(reverse=True)

    min_num_of_deletions = 0
    max_freq_allowed = len(s)

    for freq in frequency:
        if freq > max_freq_allowed:
            min_num_of_deletions += freq - max_freq_allowed
            freq = max_freq_allowed
        max_freq_allowed = max(0, freq - 1)

    return min_num_of_deletions



s = "ceabaacb"
s = "aaabbbcc"

print(minDeletions(s))