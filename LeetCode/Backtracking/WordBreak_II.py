# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary 
# word. Return all such possible sentences in any order.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordBreak(s, wordDict):
    WORD_KEY = '#'
    Trie = {}

    for word in wordDict:
        node = Trie
        for char in word:
            node = node.setdefault(char, {})
        node[WORD_KEY] = word

    result = []

    def backTrack(i, sentence):
        if i == len(s):
            result.append(" ".join(sentence))
        else:
            node = Trie
            for j in range(i, len(s)):
                if s[j] in node:
                    node = node[s[j]]

                    if WORD_KEY in node:
                        sentence.append(node[WORD_KEY])
                        backTrack(j + 1, sentence)
                        sentence.pop()
                else:
                    break

    backTrack(0, [])

    return result

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

print(wordBreak(s, wordDict))