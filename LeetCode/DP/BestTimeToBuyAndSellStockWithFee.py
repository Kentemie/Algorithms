# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a 
# transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction 
# fee for each transaction.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

def maxProfit(i, status):
    if i == len(prices):
        return 0
    if (i, status) in memo:
        return memo[(i, status)]
    
    do_nothing = maxProfit(i + 1, status)
    do_something = 0

    if status:
        do_something = prices[i] + maxProfit(i + 1, 0) - fee
    else: 
        do_something = -prices[i] + maxProfit(i + 1, 1)

    memo[(i, status)] = max(do_nothing, do_something)

    return memo[(i, status)]

prices = [1,3,7,5,10,3]
fee = 3

memo = {}

print(maxProfit(0, 0))