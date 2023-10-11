# You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping
# substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in 
# any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

def minExtraChar(s, dictionary):
    WORD_KEY = "#"
    Trie = {}

    for word in dictionary:
        node = Trie
        for char in word:
            node = node.setdefault(char, {})
        node[WORD_KEY] = word

    memo = { len(s): 0 }

    def DFS(i):
        if i in memo:
            return memo[i]
        
        res = 1 + DFS(i + 1)
        curr = Trie

        for j in range(i, len(s)):
            if s[j] not in curr:
                break
            curr = curr[s[j]]
            if WORD_KEY in curr:
                res = min(res, DFS(j + 1))

        memo[i] = res
        return res

    return DFS(0)

s = "leetscode"
dictionary = ["leet","code","leetcode"]

# s = "sayhelloworld"
# dictionary = ["hello","world"]

# s = "dwmodizxvvbosxxw"
# dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]

# s = "vmo"
# dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","vmo","cehy","tskz","ds","kzbu"]

print(minExtraChar(s, dictionary))