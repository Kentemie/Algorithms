# You are given a string s representing a list of words. Each letter in the word has one or more options.

    # If there is one option, the letter is represented as is.
    # If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options 
    # ["a", "b", "c"].
    
# For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original 
# list is ["ab", "ac"].

# Return all words that can be formed in this manner, sorted in lexicographical order.

from collections import defaultdict

def expand(s):
    letters = defaultdict(list)
    i = 0
    lvl = 0
    while i < len(s):
        if s[i] == '{':
            i += 1
            while s[i] != '}':
                if s[i] != ',':
                    letters[lvl].append(s[i])
                i += 1
            lvl += 1
            i += 1
        else:
            letters[lvl].append(s[i])
            lvl += 1
            i += 1

    for i in range(lvl):
        letters[i].sort()

    res = []

    def backTrack(curr, i):
        if len(curr) == lvl:
            res.append("".join(curr.copy()))
            return 
        for letter in letters[i]:
            curr.append(letter)
            backTrack(curr, i + 1)
            curr.pop()

    if letters:
        backTrack([], 0)
    
    return res
        

s = "{a,b}c{d,e}f"
# s = "abcd"
# s = ""
s = "{a,b}{z,x,y}"

print(expand(s))