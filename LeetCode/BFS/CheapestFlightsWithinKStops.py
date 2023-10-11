# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei]
# indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If
# there is no such route, return -1.

from heapq import heappop, heappush
from collections import defaultdict

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    for flight in flights:
        graph[flight[0]].append((flight[1], flight[2]))

    PQ = [(0, src, 0)]
    stops = [float("inf")] * n

    while PQ:
        dist, u, remaining_stops = heappop(PQ)
        if remaining_stops > stops[u] or remaining_stops > k + 1:
            continue
        stops[u] = remaining_stops
        if u == dst:
            return dist
        for v, d in graph[u]:
            heappush(PQ, (dist + d, v, remaining_stops + 1))
        print(PQ)
    return -1


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 0

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1

n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1

print(findCheapestPrice(n, flights, src, dst, k))