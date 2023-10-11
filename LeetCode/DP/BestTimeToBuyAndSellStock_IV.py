# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k 
# times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

from functools import lru_cache

@lru_cache(None)
def maxProfit(i, transactions_remaining, holding):
    if i == len(prices) or transactions_remaining == 0:
        return 0
    
    do_nothing = maxProfit(i + 1, transactions_remaining, holding)

    do_something = 0

    if holding: 
        do_something = prices[i] + maxProfit(i + 1, transactions_remaining - 1, 0)
    else:
        do_something = -prices[i] + maxProfit(i + 1, transactions_remaining, 1)

    return max(do_nothing, do_something)


k = 2
prices = [2,4,1]

print(maxProfit(0, k, 0))