# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed 
# edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a
# signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
#  If it is impossible for all the n nodes to receive the signal, return -1.

from heapq import heappop, heappush

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]
    dist = [float("inf")] * (n + 1)
    priority_queue = [(0, k)]

    for u, v, w in times:
        graph[u].append((v, w))
    
    dist[k] = 0

    while priority_queue:
        _, u = heappop(priority_queue)
        for v, w in graph[u]:
            if dist[v] > w + dist[u]:
                dist[v] = w + dist[u]
                heappush(priority_queue, (dist[v], v))
    t = max(dist[1:])
    return t if t != float("inf") else -1


# from collections import defaultdict

# def networkDelayTime2(times, n, k):
#     graph = defaultdict(list)
#     for u, v, w in times:
#         graph[u].append((v, w))
    
#     visited = set()
#     minHeap = [(0, k)]
#     time = 0

#     while minHeap:
#         weight, u = heappop(minHeap)      
#         if u in visited:
#             continue

#         visited.add(u)
#         time = max(time, weight)

#         for v, w in graph[u]:
#             if v not in visited:
#                 heappush(minHeap, (w + weight, v))
        
#     return time if len(visited) == n else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

times = [[1,2,1]]
n = 2
k = 2

# times = [[1,2,1],[2,3,2],[1,3,4]]
# n = 3
# k = 1

print(networkDelayTime(times, n, k))