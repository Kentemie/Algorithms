# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and
# the following steps are taken:

    # If the character read is a letter, that letter is written onto the tape.
    # If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.

# Given an integer k, return the kth letter (1-indexed) in the decoded string.


def decodeAtIndex(s, k):
    size = 0

    for char in s:
        if char.isdigit():
            size *= int(char)
        else:
            size += 1
    
    for char in reversed(s):
        k %= size
        if k == 0 and char.isalpha():
            return char
        
        if char.isdigit():
            size //= int(char)
        else:
            size -= 1


s = "leet2code3"
k = 10

# s = "vzpp636m8y"
# k = 2920

s = "a2345678999999999999999"
k = 10**9

print(decodeAtIndex(s, k))