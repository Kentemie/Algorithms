# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is 
# red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

    # redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
    # blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the
# edge colors alternate along the path, or -1 if such a path does not exist.


from collections import deque

def shortestAlternatingPaths(n, redEdges, blueEdges):
    red = [[] for _ in range(n)]
    blue = [[] for _ in range(n)]
    
    for src, dst in redEdges:
        red[src].append(dst)

    for src, dst in blueEdges:
        blue[src].append(dst)

    queue = deque([(0, 0, None)]) # node, length, previous edge`s color
    seen = set((0, None))
    res = [-1] * n
    res[0] = 0

    while queue:
        node, length, edge_color = queue.popleft()

        if res[node] == -1:
            res[node] = length
        
        if edge_color != "RED":
            for nei in red[node]:
                if (nei, "RED") not in seen:
                    seen.add((nei, "RED"))
                    queue.append((nei, length + 1, "RED"))
        
        if edge_color != "BLUE":
            for nei in blue[node]:
                if (nei, "BLUE") not in seen:
                    seen.add((nei, "BLUE"))
                    queue.append((nei, length + 1, "BLUE"))

    return res

n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []

print(shortestAlternatingPaths(n, redEdges, blueEdges))