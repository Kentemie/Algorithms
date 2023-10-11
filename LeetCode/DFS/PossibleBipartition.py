# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some 
# other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not 
# like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

def possibleBipartition(n, dislikes):
    def DFS(node, nodeColor):
        color[node] = nodeColor
        for neighbor in graph[node]:
            if color[neighbor] == color[node]:
                return False
            if color[neighbor] == -1:
                if not DFS(neighbor, 1 - nodeColor):
                    return False
        return True
    
    graph = [[] for _ in range(n + 1)]
    for dislike in dislikes:
        graph[dislike[0]].append(dislike[1])
        graph[dislike[1]].append(dislike[0])

    color = [-1] * (n + 1) 
    for i in range(1, n + 1):
        if color[i] == -1:
            if not DFS(i, 0):
                return False

    return True

n = 4
dislikes = [[1,2],[1,3],[2,4]]

print(possibleBipartition(n, dislikes))