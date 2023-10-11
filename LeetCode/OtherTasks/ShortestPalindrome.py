# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.


# Algorithm: 
    # Use get_longest_prefix_suffix function from KMP algorithm to find the common part of the concatenated s and 
    # rev_s (i.e. if s = "abcd" then concatenated new s will be "abcd#dcba", the common proper prefix that is also a proper suffix
    # is 'a') 

def shortestPalindrome(s):
    
    def get_longest_prefix_suffix(ss):
        n = len(ss)
        lps = [0] * n

        i, j = 1, 0

        while i < n:
            if ss[i] == ss[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j > 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
        
        return lps[-1]

    rev_s = s[::-1]
    new_s = s + '#' + rev_s

    lps = get_longest_prefix_suffix(new_s)

    return rev_s[:-lps] + s

s = "aacecaaa"
s = "abcd"
s = ""
s = "aabba"

print(shortestPalindrome(s))