# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations 
# where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course 
# nextCoursei: course prevCoursei has to be taken before course nextCoursei.

# In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for
# the courses you are taking.

# Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

def minimumSemesters(n, relations):
    adj = { i: [] for i in range(1, n + 1) }
    in_degree = { i: 0 for i in range(1, n + 1) }
    
    for u, v in relations:
        adj[u].append(v)
        in_degree[v] += 1
    
    queue = []

    for u in adj:
        if in_degree[u] == 0:
            queue.append(u)

    min_num_of_steps = 0
    studied = 0

    while queue:
        min_num_of_steps += 1
        next_queue = []
        for u in queue:
            studied += 1
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    next_queue.append(v)
        queue = next_queue

    return min_num_of_steps if studied == n else -1

n = 3
relations = [[1,3],[2,3]]
# Output: 2
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 1 and 2.
# In the second semester, you can take course 3.

n = 3
relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they are prerequisites of each other.


print(minimumSemesters(n, relations))