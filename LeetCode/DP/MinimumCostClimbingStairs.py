# # You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or 
# # two steps.
# # You can either start from the step with index 0, or the step with index 1.
# # Return the minimum cost to reach the top of the floor.

# # Bottom-Up Dynamic Programming

# def minCostClimbingStairs(costs):
#     minCosts = [0] * (len(costs) + 1)
    
#     for i in range(2, len(costs) + 1):
#         takeOneStep = minCosts[i-1] + costs[i-1]
#         takeTwoSteps = minCosts[i-2] + costs[i-2]
        
#         minCosts[i] = min(takeOneStep, takeTwoSteps)

#     return minCosts[-1] 

# costs = [1,100,1,1,1,100,1,1,100,1]

# print(minCostClimbingStairs(costs))


# # Bottom-Up, Constant Space

# def minCostClimbingStairs(costs):
#     oneStep = twoSteps = 0
    
#     for i in range(2, len(costs) + 1):
#         temp = oneStep
#         oneStep = min(oneStep + costs[i-1], twoSteps + costs[i-2])
#         twoSteps = temp
    
#     return oneStep

# costs = [1,100,1,1,1,100,1,1,100,1]

# print(minCostClimbingStairs(costs))


# Top-Down Dynamic Programming (Recursion + Memoization)

def minCost(i):
    if i <= 1:
        return 0
    if i in memo:
        return memo[i]

    oneStep = costs[i-1] + minCost(i-1)
    twoSteps = costs[i-2] + minCost(i-2)

    memo[i] = min(oneStep, twoSteps)

    return memo[i]

costs = [1,100,1,1,1,100,1,1,100,1]
memo = {}
print(minCost(len(costs)))