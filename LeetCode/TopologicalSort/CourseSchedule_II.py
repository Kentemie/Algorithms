# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any
# of them. If it is impossible to finish all courses, return an empty array.

from collections import defaultdict

def topologicalSort(numCourses, prerequisites):
    def DFS(node):
        nonlocal is_possible
        
        if not is_possible:
            return 
        
        color[node] = 2

        if node in graph: 
            for nei in graph[node]:
                if color[nei] == 1:
                    DFS(nei)
                elif color[nei] == 2:
                    is_possible = False 
        
        color[node] = 3
        res.append(node)


    graph = defaultdict(list)
    res = []
    is_possible = True

    color = {k: 1 for k in range(numCourses)}

    for prerequisite in prerequisites:
        graph[prerequisite[0]].append(prerequisite[1])

    for node in range(numCourses):
        if color[node] == 1:
            DFS(node)

    return res if is_possible else []

# numCourses = 2
# prerequisites = [[1,0]]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# numCourses = 1
# prerequisites = []

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

print(topologicalSort(numCourses, prerequisites))