# Application of Kahn’s algorithm for Topological Sort:   

    # 1. Course sequencing: Courses at universities frequently have prerequisites for other courses. The courses can be 
    # scheduled using Kahn’s algorithm so that the prerequisites are taken before the courses that call for them.

    # 2. Management of software dependencies: When developing software, libraries and modules frequently rely on other 
    # libraries and modules. The dependencies can be installed in the proper order by using Kahn’s approach.

    # 3. Scheduling tasks: In project management, activities frequently depend on one another. The tasks can be scheduled 
    # using Kahn’s method so that the dependent tasks are finished before the tasks that depend on them.

    # 4. Data processing: In data processing pipelines, the outcomes of some processes may be dependent. The stages can 
    # be carried out in the right order by using Kahn’s algorithm.

    # 5. Circuit design: In the creation of an electronic circuit, some components may be dependent on the output of 
    # others. The components can be joined in the right order by using Kahn’s technique.

from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.numOfVertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        inDegree = [0] * (self.numOfVertices)

        for u in self.graph:
            for v in self.graph[u]:
                inDegree[v] += 1

        queue = deque()

        for v in range(self.numOfVertices):
            if inDegree[v] == 0:
                queue.append(v)
        
        cnt = 0
        topOrder = []

        while queue:
            u = queue.popleft()
            topOrder.append(u)

            for v in self.graph[u]:
                inDegree[v] -= 1

                if inDegree[v] == 0:
                    queue.append(v)
                
            cnt += 1

        if cnt != self.numOfVertices:
            print("There exists a cycle in the graph")
        else:
            print(self.graph)
            print(topOrder)


g = Graph(6)

g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()