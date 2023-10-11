# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) 
# in the given array.


def findAllConcatenatedWordsInADict(words):
    word_set = set(words)
    memo = {}

    def DFS(word):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if (prefix in word_set and suffix in word_set) or (prefix in word_set and DFS(suffix)):
                memo[word] = True
                return True
        memo[word] = False
        return False

    res = []

    for word in words:
        if DFS(word):
            res.append(word)

    return res



words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

print(findAllConcatenatedWordsInADict(words))