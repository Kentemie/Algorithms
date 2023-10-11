# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with 
# a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, 
# and so on...
# Return the minimum cost to paint all houses.

# # Brute force with a Recursive Tree and Memoization
# # Time complexity: O(n).
# # Space complexity: O(n).

# costs = [[17,2,17],[16,16,5],[14,3,19]]

# def minCost(n, color):
#     if (n, color) in memo:
#         return memo[(n, color)]

#     total_cost = costs[n][color]

#     if n == len(costs) - 1:
#         pass
#     elif color == 0: # Red
#         total_cost += min(minCost(n + 1, 1), minCost(n + 1, 2))
#     elif color == 1: # Green
#         total_cost += min(minCost(n + 1, 0), minCost(n + 1, 2))
#     else: # Blue
#         total_cost += min(minCost(n + 1, 0), minCost(n + 1, 1))

#     memo[(n, color)] = total_cost

#     return total_cost


# memo = {}
# print(min(minCost(0, 0), minCost(0, 1), minCost(0, 2)))




# Dynamic Programming
# Time complexity: O(n).
# Space complexity: O(1).

costs = [[17,2,17],[16,16,5],[14,3,19]]

def minCost(costs):
    for i in reversed(range(len(costs) - 1)):
        costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
        costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
        costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])

    return min(costs[0])

print(minCost(costs))