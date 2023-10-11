# There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n 
# cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array 
# roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

# There is a meeting for the representatives of each city. The meeting is in the capital city.

# There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

# A representative can use the car in their city to travel or change the car and ride with another representative. 
# The cost of traveling between two cities is one liter of fuel.

# Return the minimum number of liters of fuel to reach the capital city.

from math import ceil

roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
# roads = [[0,1],[0,2],[0,3]]
# seats = 5
# roads = []
# seats = 1
# roads = [[0,1],[1,3],[3,2],[2,5],[5,6],[5,7],[5,4]]
# seats = 2

fuel = 0

graph = [[] for _ in range(len(roads) + 1)]

for road in roads:
    graph[road[0]].append(road[1])
    graph[road[1]].append(road[0])

def DFS(node, parent):
    global fuel
    representatives = 1
    for child in graph[node]:
        if child == parent:
            continue
        representatives += DFS(child, node)
    if node != 0:
        fuel += ceil(representatives / seats)
    return representatives 

DFS(0, -1)

print(fuel)