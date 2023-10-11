# You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 
# 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

# Return the number of pairs of different nodes that are unreachable from each other.

n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]

# n = 3
# edges = [[0,1],[0,2],[1,2]]

def DFS(node):
    cnt = 1
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            cnt += DFS(child)
    
    return cnt

graph = [[] for _ in range(n)]

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = [False] * n
remainingNodes = n
ans = 0

for i in range(n):
    if not visited[i]:
        numOfNodes = DFS(i)
        ans += numOfNodes * (remainingNodes - numOfNodes)
        remainingNodes -= numOfNodes

print(ans)
