# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed 
# edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.
    
# For example, a topological sorting of the following graph is "5 4 2 3 1 0". There can be more than one topological sorting
# for a graph. For example, another topological sorting of the following graph is “4 5 2 0 3 1″. The first vertex in 
# topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.numOfVertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, node, visited, stack):
        visited[node] = True

        for nei in self.graph[node]:
            if not visited[nei]:
                self.topologicalSortUtil(nei, visited, stack)
        
        stack.append(node)

    def topologicalSort(self):
        visited = [False] * self.numOfVertices
        stack = []

        for node in range(self.numOfVertices):
            if not visited[node]:
                self.topologicalSortUtil(node, visited, stack)

        print(stack[::-1])

if __name__ == "__main__":
    graph = Graph(6)
    graph.addEdge(5, 2)
    graph.addEdge(5, 0)
    graph.addEdge(4, 0)
    graph.addEdge(4, 1)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)

    graph.topologicalSort()