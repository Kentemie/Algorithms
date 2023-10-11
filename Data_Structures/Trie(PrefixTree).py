# A Trie is a special form of a Nary tree. Typically, a trie is used to store strings. Each Trie node represents a 
# string (a prefix). Each node might have several children nodes while the paths to different children nodes represent
# different characters. And the strings the child nodes represent will be the origin string represented by the node 
# itself plus the character on the path.

# In the example, the value we mark in each node is the string the node represents. For instance, we start from the
# root node and choose the second path 'b', then choose the first child 'a', and choose child 'd', finally we arrived
# at the node "bad". The value of the node is exactly formed by the letters in the path from the root to the node sequentially.

# It is worth noting that the root node is associated with the empty string.

# One important property of Trie is that all the descendants of a node have a common prefix of the string 
# associated with that node. That's why Trie is also called prefix tree.

# Let's look at the example again. For example, the strings represented by nodes in the subtree rooted at
# node "b" have a common prefix "b". And vice versa. The strings which have the common prefix "b" are all
# in the subtree rooted at node "b" while the strings with different prefixes will come to different branches.

# Trie is widely used in various applications, such as autocomplete, spell checker, etc. We will introduce the
# practical applications in later chapters.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    
obj = Trie()
obj.insert("apple")
param_2 = obj.search("app")
param_3 = obj.startsWith("app")

print(param_2, param_3)