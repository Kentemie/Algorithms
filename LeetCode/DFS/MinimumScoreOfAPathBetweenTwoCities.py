# You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads
# where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a 
# distance equal to distancei. The cities graph is not necessarily connected.

# The score of a path between two cities is defined as the minimum distance of a road in this path.

# Return the minimum possible score of a path between cities 1 and n.

# Note:

    # A path is a sequence of roads between two cities.
    # It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple
    # times along the path.

from collections import defaultdict

roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
n = 4
roads = [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]
n = 6


graph = defaultdict(list)

for road in roads:
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

visited = set()

def DFS(node):
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            DFS(child)

DFS(1)
ans = float('inf')
for i, j, dist in roads:
    if i in visited or j in visited:
        ans = min(ans, dist)

print(ans)