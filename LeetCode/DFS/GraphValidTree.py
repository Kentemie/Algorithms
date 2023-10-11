# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi]
# indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    
    graph = [[] for _ in range(n)]
    seen = set()

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    def DFS(node):
        if node in seen:
            return
        seen.add(node)
        for nei in graph[node]:
            DFS(nei)

    DFS(0)

    return len(seen) == n

n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

print(validTree(n, edges))