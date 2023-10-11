# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special 
# character '#').

# You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously 
# typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character 
# except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

# Here are the specific rules:

    # The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    # The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences 
    # have the same hot degree, use ASCII-code order (smaller one appears first).
    # If less than 3 hot sentences exist, return as many as you can.
    # When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

# Implement the AutocompleteSystem class:

    # AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
    # List<String> input(char c) This indicates that the user typed the character c.
        # Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
        # Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. 
        # If there are fewer than 3 matches, return them all.


from heapq import nsmallest

class TrieNode:

    def __init__(self):
        self.children = {}
        self.sentences = {}


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.dead = TrieNode()
        self.curr_node = self.root
        self.curr_sentence = []

        for sentence, freq in zip(sentences, times):
            self.insert(sentence, freq)

    def input(self, c):
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.insert(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []

        self.curr_node = self.curr_node.children[c]
        sentences = [(freq, sentence) for sentence, freq in self.curr_node.sentences.items()]
        result = nsmallest(3, sentences)

        return [item[1] for item in result]

    def insert(self, sentence, freq):
        node = self.root

        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] = node.sentences.get(sentence, 0) - freq



# obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
# print(obj.input('i'))
# print(obj.input(' '))
# print(obj.input('a'))
# print(obj.input('#'))
# print(obj.input('i'))
# print(obj.input(' '))
# print(obj.input('a'))
# print(obj.input('#'))
# print(obj.input('i'))
# print(obj.input(' '))
# print(obj.input('a'))
# print(obj.input('#'))

obj = AutocompleteSystem(["abc","abbc","a"], [3,3,3])
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))
print(obj.input('a'))
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))
print(obj.input('a'))
print(obj.input('b'))
print(obj.input('c'))
print(obj.input('#'))