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


def findCircleNum(isConnected):
    numOfProv = len(isConnected) 
    DSU = UnionFind(len(isConnected))
    
    for i, city in enumerate(isConnected):
        for j in range(len(city)):
            if city[j] == 1 and DSU.find(i) != DSU.find(j):
                numOfProv -= 1
                DSU.union(i, j)
    
    return numOfProv


isConnected = [[1,1,0],[1,1,0],[0,0,1]]

print(findCircleNum(isConnected))