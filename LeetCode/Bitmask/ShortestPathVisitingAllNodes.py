# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list
# of all the nodes connected with node i by an edge.

# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple
# times, and you may reuse edges.


def shortestPathLength(graph):
    n = len(graph)
    memo = {}
    ending_mask = (1 << n) - 1
    
    def DFS(node, mask):
        if (node, mask) in memo:
            return memo[(node, mask)]
        if mask & (mask - 1) == 0:
            return 0
        
        memo[(node, mask)] = float("inf")

        for nei in graph[node]:
            if mask & (1 << nei):
                node_was_already_visited = 1 + DFS(nei, mask)
                node_was_not_visited = 1 + DFS(nei, mask ^ (1 << node))
                memo[(node, mask)] = min(memo[(node, mask)], node_was_already_visited, node_was_not_visited)

        return memo[(node, mask)]
    
    return min(DFS(node, ending_mask) for node in range(n))

graph = [[1,2,3],[0],[0],[0]]
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]

print(shortestPathLength(graph))