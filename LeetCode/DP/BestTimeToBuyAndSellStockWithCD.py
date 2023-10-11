# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one 
# share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(i, status):
    if i == len(prices):
        return 0
    if (i, status) in memo: 
        return memo[(i, status)]
    
    do_nothing = maxProfit(i + 1, status)
    do_something = 0

    if status == 0:
        do_something = -prices[i] + maxProfit(i + 1, 1)
    elif status == 1: 
        do_something = prices[i] + maxProfit(i + 1, 2)
    else:
        do_something = maxProfit(i + 1, 0)

    memo[(i, status)] = max(do_nothing, do_something)

    return memo[(i, status)]

prices = [1,2,3,0,2]
memo = {}

print(maxProfit(0, 0))