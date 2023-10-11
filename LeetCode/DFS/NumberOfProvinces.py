# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
# and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
# connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

def DFS(node):
    if node in visited:
        return 0

    visited.add(node)

    for neighbor in graph[node]:
        DFS(neighbor)

    return 1

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]

n = len(isConnected)
graph = [[] for _ in range(n)]
visited = set()
cnt = 0

for i, city in enumerate(isConnected):
    for j in range(len(city)):
        if city[j] == 1:
            graph[i].append(j)
print(graph)

for i in range(n):
    cnt += DFS(i)

print(cnt)