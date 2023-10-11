# There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and 
# exactly n - 1 edges.

# You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given
# a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# A good path is a simple path that satisfies the following conditions:

# The starting node and the ending node have the same value.
# All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting
# node's value should be the maximum value along the path).
# Return the number of distinct good paths.

# Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A 
# single node is also considered as a valid path.

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


def numberOfGoodPaths(vals, edges):
    n = len(vals)
    adjacency = [[] for _ in range(n)]

    for x, y in edges:
        adjacency[x].append(y)        
        adjacency[y].append(x)

    valuesToNodes = {}

    for node, val in enumerate(vals):
        valuesToNodes.setdefault(val, []).append(node)
    
    dsu = UnionFind(len(vals))
    goodPaths = 0

    for _, nodes in sorted(valuesToNodes.items()):
        for node in nodes:
            for nei in adjacency[node]:
                if vals[node] >= vals[nei]:
                    dsu.union(node, nei)

        groups = {}

        for node in nodes:
            u = dsu.find(node)
            groups[u] = groups.get(u, 0) + 1

        for size in groups.values():
            goodPaths += (size * (size + 1)) // 2

    return goodPaths



vals = [1,2,4,2,3,4,2,3,3]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8]]

vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]
# 6

vals = [1,1,2,2,3]
edges = [[0,1],[1,2],[2,3],[2,4]]
# 7

vals = [1]
edges = []
# 1

print(numberOfGoodPaths(vals, edges))