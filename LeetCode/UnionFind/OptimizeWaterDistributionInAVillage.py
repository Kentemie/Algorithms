# There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

# For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), 
# or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each 
# pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections
# are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

# Return the minimum total cost to supply water to all houses.


class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

        return True


def minCostToSupplyWater(n, wells, pipes):
    edges = []

    for idx, weight in enumerate(wells):
        edges.append((weight, 0, idx + 1))

    for u, v, weight in pipes:
        edges.append((weight, u, v))

    edges.sort(key=lambda x: x[0])
    uf = UnionFind(n + 1)
    min_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            min_cost += weight

    return min_cost


n = 3
wells = [1,2,2]
pipes = [[1,2,1],[2,3,1]]

n = 2
wells = [1,1]
pipes = [[1,2,1],[1,2,2]]

n = 5
wells = [46012,72474,64965,751,33304]
pipes = [[2,1,6719],[3,2,75312],[5,3,44918]]

print(minCostToSupplyWater(n, wells, pipes))