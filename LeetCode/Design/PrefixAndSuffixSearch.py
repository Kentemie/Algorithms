# Design a special dictionary that searches the words in it by a prefix and a suffix.

# Implement the WordFilter class:

    # WordFilter(string[] words) Initializes the object with the words in the dictionary.
    # f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff.
    # If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

# To effectively search a word by it`s prefix and suffix, just for each suffix of the word, insert that suffix, followed by
# separator('#'), followed by the entire word as prefix, all into the trie.
    # For example, insert '#apple', 'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple' into 
    # the trie. Then for a query like prefix = "ap", suffix = "le", find the matched word by querying the trie for le#ap.

from pprint import pprint

class WordFilter:

    def __init__(self, words):
        self.root = {}
        self.separator = '#'

        for idx, word in enumerate(words):
            self.addWord(idx, word)
    
    def addWord(self, idx, word):
        for i in range(len(word)):
            node = self.root
            node['idx'] = idx
            word_to_insert = word[i:] + self.separator + word

            for char in word_to_insert:
                node = node.setdefault(char, {})
                node['idx'] = idx
    
    def f(self, pref, suff):
        node = self.root

        for char in (suff + self.separator + pref):
            if char not in node:
                return -1
            node = node[char]
        
        return node['idx']
            

obj = WordFilter(["apple", "app"])
print(obj.f("a", "e"))
pprint(obj.root)