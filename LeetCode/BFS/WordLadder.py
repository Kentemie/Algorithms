# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
# beginWord -> s1 -> s2 -> ... -> sk such that:

#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord

# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest 
# transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

from collections import deque

def createNewWord(word):
    for i in range(26):
        for j in range(len(word)):
            newletter = chr(97 + i)
            yield word[:j] + newletter + word[j + 1:]

def BFS(beginWord, endWord, wordList):
    words = set(wordList)
    if endWord not in words:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, step = queue.popleft()
        if word == endWord:
            return step
        for newWord in createNewWord(word):
            if newWord in words:
                queue.append((newWord, step + 1))
                words.remove(newWord)
        
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

print(BFS(beginWord, endWord, wordList))