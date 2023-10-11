# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 
# and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from 
# node i to node graph[i][j]).

def allPathsSourceTarget(graph):
    res = []

    def backTrack(curr, i):
        curr.append(i)
        if i == len(graph) - 1:
            res.append(curr[:])
        neighbors = graph[i]
        for nei in neighbors:
            backTrack(curr, nei)
        curr.pop()

    backTrack([], 0)

    return res

graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]

print(allPathsSourceTarget(graph))