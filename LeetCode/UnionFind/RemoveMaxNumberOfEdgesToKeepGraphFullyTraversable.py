# Alice and Bob have an undirected graph of n nodes and three types of edges:

    # Type 1: Can be traversed by Alice only.
    # Type 2: Can be traversed by Bob only.
    # Type 3: Can be traversed by both Alice and Bob.

# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, 
# find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by 
# both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.


class UnionFind:
    def __init__(self, size):
        self.components = size
        self.root = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return 0

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

        self.components -= 1
        return 1
        
    def is_connected(self):
        return self.components == 1

def maxNumEdgesToRemove(n, edges):
    alice = UnionFind(n)
    bob = UnionFind(n)

    edges_required = 0

    for type, u, v in edges:
        if type == 3:
            edges_required += (alice.union(u, v) | bob.union(u, v))

    for type, u, v in edges:
        if type == 1:
            edges_required += alice.union(u, v)
        elif type == 2:
            edges_required += bob.union(u, v)

    if alice.is_connected() and bob.is_connected():
        return len(edges) - edges_required
    
    return -1


n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. 
# Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. 
# Therefore it's impossible to make the graph fully traversable.

print(maxNumEdgesToRemove(n, edges))