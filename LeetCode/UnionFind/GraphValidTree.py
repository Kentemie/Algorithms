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

        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        
        return True 


def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    
    DSU = UnionFind(n)
    
    for i, j in edges:
        if not DSU.union(i, j):
            return False

    return True

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]

print(validTree(n, edges))