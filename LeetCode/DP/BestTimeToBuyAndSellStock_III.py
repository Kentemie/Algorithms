# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Bidirectional Dynamic Programming

def maxProfit(prices):

    left_min = prices[0]
    right_max = prices[-1]

    left_profits = [0] * len(prices)
    right_profits = [0] * (len(prices) + 1)

    for l in range(1, len(prices)):
        left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
        left_min = min(left_min, prices[l])

        r = len(prices) - l - 1
        right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
        right_max = max(right_max, prices[r])

    max_profit = 0

    for i in range(len(prices)):
        max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
    
    return max_profit


prices = [3,3,5,0,0,3,1,4]
# 6
# prices = [1,2,3,4,5]
# 4
# prices = [7,6,4,3,1]
# 0

print(maxProfit(prices))