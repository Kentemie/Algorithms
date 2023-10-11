# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

def numberOfSubstrings(s):
    ABC = {'a': 1, 'b': 1, 'c': 1}
    atLeast = {}
    res = left = cnt = 0

    for right in range(len(s)):
        atLeast[s[right]] = atLeast.get(s[right], 0) + 1
        if atLeast[s[right]] == 1:
            cnt += 1
        while cnt == len(ABC):
            res += len(s) - right
            atLeast[s[left]] -= 1
            if atLeast[s[left]] == 0:
                cnt -= 1
            left += 1

    return res

s = "abcabc"
s = "aaacb"
s = "abc"

print(numberOfSubstrings(s))