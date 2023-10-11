class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class T9:
    def __init__(self, dictionary):
        self.root = TrieNode()
        self.memo = set()
        self.mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        for word in dictionary:
            self.insert(word)

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_word = True


    def get_possible_words(self, digits):
        if not digits:
            return []
        
        res = []

        def backTrack(node, idx, path):
            if idx == len(digits):
                if node.is_word:
                    res.append("".join(path)) 
                return
        
            if (node, idx) in self.memo:
                return 

            for letter in self.mapping[digits[idx]]:
                if letter in node.children:
                    path.append(letter)
                    backTrack(node.children[letter], idx + 1, path)
                    path.pop()
            
            self.memo.add((node, idx))

        backTrack(self.root, 0, [])

        return res
    
dictionary = {'hello', 'world', 'test', 'tree', 'apple'}

t9 = T9(dictionary)
digits = '43556'
possible_words = t9.get_possible_words(digits)
print(possible_words)