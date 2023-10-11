# Algorithm for Dijkstra’s Algorithm:
    
    # Mark the source node with a current distance of 0 and the rest with infinity.
    # Set the non-visited node with the smallest current distance as the current node.
    # For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge 
    # connecting 0->1. If it is smaller than the current distance of Node, set it as the new current distance of N.
    # Mark the current node 1 as visited.
    # Go to step 2 if there are any nodes are unvisited.

# Dijkstra’s Shortest Path Algorithm using priority_queue (Heap)

from heapq import heappop, heappush

# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, numOfVertices):
        self.numOfVertices = numOfVertices
        self.adj = [[] for _ in range(numOfVertices)]

    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
    
    def shortestPath(self, src):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heappush(pq, (0, src))

        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float("inf")] * self.numOfVertices
        dist[src] = 0
        
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            _, u = heappop(pq)

            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heappush(pq, (dist[v], v))

        for i in range(self.numOfVertices):
            print(f"{i} \t\t {dist[i]}")

V = 9
g = Graph(V)

g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

g.shortestPath(0)