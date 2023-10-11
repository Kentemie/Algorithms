# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between
# two different cities (this network form a tree). Last year, The ministry of transport decided to orient the 
# roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number
# of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

def minReorder(n, connections):
    edges = { (a, b) for a, b in connections }
    graph = { city: [] for city in range(n) }
    visited = set()
    changes = 0

    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    def DFS(node):
        nonlocal changes
        for nei in graph[node]:
            if nei in visited:
                continue
            if (nei, node) not in edges:
                changes += 1
            visited.add(nei)
            DFS(nei)
            
    visited.add(0)
    DFS(0)

    return changes

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

print(minReorder(n, connections))