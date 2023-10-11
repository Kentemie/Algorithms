# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there 
# is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

def DFS(node):
    if node in visited:
        return 0
    visited.add(node)
    for nei in graph[node]:
        DFS(nei)
    return 1

# n = 5
# edges = [[0,1],[1,2],[3,4]]

# n = 5
# edges = [[0,1],[1,2],[2,3],[3,4]]

n = 2
edges = [[1,0]]

graph = [[] for _ in range(n)]
visited = set()
cnt = 0

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for i in range(n):
    cnt += DFS(i)

print(cnt)