# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) 
# of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.

from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

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

def smallestStringWithSwaps(s, pairs):
    DSU = UnionFind(len(s))
    
    for i, j in pairs:
        DSU.union(i, j)
    
    mapping = defaultdict(list)

    for vertex in range(len(s)):
        root = DSU.find(vertex)
        mapping[root].append(vertex)

    smallestStr = [''] * len(s)

    for indices in mapping.values():
        chars = []
        
        for index in indices:
            chars.append(s[index])

        chars.sort()

        for index in range(len(indices)):
            smallestStr[indices[index]] = chars[index]
    
    return "".join(smallestStr)


s = "dcab"
pairs = [[0,3],[1,2],[0,2]]

print(smallestStringWithSwaps(s, pairs))