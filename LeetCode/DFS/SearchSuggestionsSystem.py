# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed.
# Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix
# return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

def suggestedProducts(products, searchWord):
    Trie = {}
    WORD_KEY = "$"
    res = []
    curr = []

    for product in products:
        node = Trie
        for char in product:
            node = node.setdefault(char, {})
        node[WORD_KEY] = product

    def DFS(node):
        if len(curr) == 3:
            return
        isWord = node.get(WORD_KEY)
        if isWord:
            curr.append(isWord)
        for i in range(26):
            char = chr(i + 97)
            if char in node:
                DFS(node[char])

    def search(word):
        TrieNode = Trie
        for char in word:
            if char not in TrieNode:
                return
            TrieNode = TrieNode[char]
        DFS(TrieNode)

    for i in range(len(searchWord)):
        search(searchWord[:i + 1])
        res.append(curr)
        curr = []

    return res


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

products = ["havana"]
searchWord = "havana"

print(suggestedProducts(products, searchWord))