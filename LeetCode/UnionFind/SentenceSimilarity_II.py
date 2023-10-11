# We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as
# arr = ["I","am",happy","with","leetcode"].

# Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs
# where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

# Return true if sentence1 and sentence2 are similar, or false if they are not similar.

# Two sentences are similar if:

    # They have the same length (i.e., the same number of words)
    # sentence1[i] and sentence2[i] are similar.

# Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if
#  the words a and b are similar, and the words b and c are similar, then a and c are similar.


class UnionFind:

    def __init__(self):
        self.root = {}
        self.rank = {}

    def add_word(self, word):
        if word not in self.root:
            self.root[word] = word
            self.rank[word] = 0

    def is_word_present(self, word):
        return word in self.root

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:

            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        

def areSentencesSimilarTwo(sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2):
        return False
    
    uf = UnionFind()

    for pair in similarPairs:
        uf.add_word(pair[0])
        uf.add_word(pair[1])
        uf.union(pair[0], pair[1])

    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i]:
            continue
        if uf.is_word_present(sentence1[i]) and uf.is_word_present(sentence2[i]) and uf.find(sentence1[i]) == uf.find(sentence2[i]):
            continue
        return False
    
    return True


sentence1 = ["great","acting","skills"]
sentence2 = ["fine","drama","talent"]
similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]

sentence1 = ["I","love","leetcode"]
sentence2 = ["I","love","onepiece"]
similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]

sentence1 = ["I","love","leetcode"]
sentence2 = ["I","love","onepiece"]
similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]

print(areSentencesSimilarTwo(sentence1, sentence2, similarPairs))