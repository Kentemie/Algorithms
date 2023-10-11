# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. 
# You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all
# apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting 
# the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an 
# apple; otherwise, it does not have any apple.

def minTime(n, edges, hasApple):

    def DFS(node, parent, nodes, hasApple):
        childTime, totalTime = 0, 0

        for child in nodes[node]:
            if child == parent:
                continue
            childTime = DFS(child, node, nodes, hasApple)
            if childTime or hasApple[child]:
                totalTime += childTime + 2

        return totalTime

    nodes = [[] for _ in range(n)]

    for edge in edges:
        nodes[edge[0]].append(edge[1])
        nodes[edge[1]].append(edge[0])

    return DFS(0, -1, nodes, hasApple)


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]

print(minTime(n, edges, hasApple))