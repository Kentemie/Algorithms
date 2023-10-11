# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain 
# color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.
# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, 
# and so on...
# Return the minimum cost to paint all houses.

# from functools import lru_cache

# @lru_cache(None)
# def minCost(n, color):
#     if n == len(costs) - 1:
#         return costs[n][color]
   
#     cost = float('inf')

#     for c in range(len(costs[0])):
#         if c != color:
#             cost = min(cost, minCost(n + 1, c))

#     return costs[n][color] + cost

# costs = [[1,5,3],[2,9,4]]
# total_cost = float('inf')

# for c in range(len(costs[0])):
#     total_cost = min(total_cost, minCost(0, c))

# print(total_cost)


# costs = [[1,5,3],[2,9,4]]
costs = [[1,3],[2,4]]

n = len(costs)
k = len(costs[0])

for i in range(1, n):
    first_min = second_min = None
    for j in range(k):
        cost = costs[i - 1][j]
        if first_min is None or cost < costs[i - 1][first_min]:
            second_min = first_min
            first_min = j
        elif second_min is None or cost < costs[i - 1][second_min]:
            second_min = j

    for j in range(k):
        if j == first_min:
            costs[i][j] += costs[i - 1][second_min]
        else:
            costs[i][j] += costs[i - 1][first_min]

print(min(costs[-1]))