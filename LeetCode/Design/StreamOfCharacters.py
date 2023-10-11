# Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array 
# of strings words.

# For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your 
# algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

# Implement the StreamChecker class:

    # StreamChecker(String[] words) Initializes the object with the strings array words.
    # boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream 
    # forms a word that is in words.


from collections import deque

class StreamChecker:

    def __init__(self, words: list[str]):
        self.root = {}
        self.suffix = deque([])

        for word in set(words):
            node = self.root
            for char in word[::-1]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word


    def query(self, letter: str) -> bool:
        self.suffix.appendleft(letter)
        node = self.root

        for char in self.suffix:
            if '#' in node:
                return True
            if char not in node:
                return False
            node = node[char]
        
        return '#' in node


SC = StreamChecker(["cd", "f", "kl"])

print(SC.query('a'))
print(SC.query('b'))
print(SC.query('c'))
print(SC.query('d'))
print(SC.query('e'))
print(SC.query('f'))
print(SC.query('g'))
print(SC.query('h'))
print(SC.query('i'))
print(SC.query('j'))
print(SC.query('k'))
print(SC.query('l'))