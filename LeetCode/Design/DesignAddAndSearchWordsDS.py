# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

    # WordDictionary() Initializes the object.
    # void addWord(word) Adds word to the data structure, it can be matched later.
    # bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may 
    # contain dots '.' where dots can be matched with any letter.


class WordDictionary:

    def __init__(self):
        self.Trie = {}
        self.word_key = '#'

    def addWord(self, word):
        node = self.Trie

        for char in word:
            node = node.setdefault(char, {})
        
        node[self.word_key] = word

    def search(self, word):
        
        def DFS(word, node):
            for i, char in enumerate(word):
                if char not in node:
                    if char == '.':
                        for possible_char in node:
                            if possible_char != self.word_key and DFS(word[i + 1:], node[possible_char]):
                                return True
                    return False
                else:
                    node = node[char]
            return self.word_key in node
        
        return DFS(word, self.Trie)


obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))