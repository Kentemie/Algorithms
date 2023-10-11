# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the 
# absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


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
        elif self.rank[rootY] > self.rank[rootX]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

        return True
    

# How to find MST using Kruskal’s algorithm?
    # Sort all the edges in non-decreasing order of their weight. 
    # Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed, include
    # this edge. Else, discard it. 
    # Repeat step #2 until there are (V-1) edges in the spanning tree.

def minCostConnectPointsKruskal(points):
    n = len(points)
    edges = [] 

    for i in range(n):
        for j in range(i + 1, n):
            val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append([i, j, val])

    edges.sort(key=lambda x: x[2])
    disjoint_set = UnionFind(n)

    minCost = 0
    i, num_of_edges = 0, 0

    while num_of_edges < n - 1:
        u, v, weight = edges[i]

        if disjoint_set.union(u, v):
            num_of_edges += 1
            minCost += weight

        i += 1
    
    return minCost


# Step 1: Determine an arbitrary vertex as the starting vertex of the MST.
# Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
# Step 3: Find edges connecting any tree vertex with the fringe vertices.
# Step 4: Find the minimum among these edges.
# Step 5: Add the chosen edge to the MST if it does not form any cycle.
# Step 6: Return the MST and exit

def minCostConnectPointsPrim(points):
    n = len(points)
    num_of_edges = 0
    min_cost = 0

    visited = [False] * n
    min_dist = [float("inf")] * n
    min_dist[0] = 0

    while num_of_edges < n:
        curr_min_edge = float("inf")
        curr_vertex = -1

        for vertex in range(n):
            if not visited[vertex] and curr_min_edge > min_dist[vertex]:
                curr_min_edge = min_dist[vertex]
                curr_vertex = vertex

        min_cost += curr_min_edge
        num_of_edges += 1
        visited[curr_vertex] = True

        for next_vertex in range(n):
            weight = abs(points[curr_vertex][0] - points[next_vertex][0]) + abs(points[curr_vertex][1] - points[next_vertex][1])
            if not visited[next_vertex] and min_dist[next_vertex] > weight:
                min_dist[next_vertex] = weight

    return min_cost



points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# points = [[3,12],[-2,5],[-4,1]]

print(minCostConnectPointsKruskal(points))
print(minCostConnectPointsPrim(points))