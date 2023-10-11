# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

from collections import defaultdict, deque 

def canFinish(numCourses, prerequisites):

    graph = defaultdict(list)

    for prerequisite in prerequisites:
        graph[prerequisite[0]].append(prerequisite[1])

    inDegree = [0] * numCourses

    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    queue = deque()

    for v in range(numCourses):
        if inDegree[v] == 0:
            queue.append(v)

    cnt = 0
    res = []

    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph[u]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                queue.append(v)
        cnt += 1

    if cnt != numCourses:
        return []
    else:
        return res

numCourses = 2
prerequisites = [[1,0]]

numCourses = 2
prerequisites = [[1,0],[0,1]]

numCourses = 4
prerequisites = [[1,0],[1,2],[1,3]]

# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# numCourses = 1
# prerequisites = []

print(canFinish(numCourses, prerequisites))