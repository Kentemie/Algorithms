# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from 
# node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

# You are also given two integers node1 and node2.

# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance 
# from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with 
# the smallest index, and if no possible answer exists, return -1.

# Note that edges may contain cycles.

from collections import deque

def BFS(startNode, edges):
    n = len(edges)
    queue = deque([startNode])
    visited = set()
    dist = [float('inf')] * n
    dist[startNode] = 0

    while queue:
        node = queue.pop()
        
        if node in visited:
            continue
        
        visited.add(node)
        neighbor = edges[node]
        
        if neighbor != -1 and neighbor not in visited:
            dist[neighbor] = 1 + dist[node]
            queue.append(neighbor)

    return dist

edges = [2,2,3,-1]
node1 = 0
node2 = 1

dist1 = BFS(node1, edges)
dist2 = BFS(node2, edges)

print(dist1)
print(dist2)

minDistNode = -1
minDistSoFar = float('inf')

for currNode in range(len(edges)):
    if minDistSoFar > max(dist1[currNode], dist2[currNode]):
        minDistNode = currNode
        minDistSoFar = max(dist1[currNode], dist2[currNode])

print(minDistNode)