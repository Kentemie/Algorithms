# # You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# # Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the 
# # coins, return -1.
# # You may assume that you have an infinite number of each kind of coin.

# def coinChange(amount):
#     if amount == 0:
#         return 0
#     if amount < 0:
#         return -1
#     if amount in memo:
#         return memo[amount]
#     shortest_path = float('inf')
#     for coin in coins:
#         lvl = coinChange(amount - coin)
#         if lvl != -1:
#             shortest_path = min(shortest_path, lvl + 1)
    
#     memo[amount] = shortest_path
#     return shortest_path if shortest_path != float('inf') else -1     

# coins = [1,2,5]
# amount = 11
# memo = {}

# print(coinChange(amount))


# Bottom-Up

coins = [186,419,83,408]
amount = 6249

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x - coin] + 1)
        
print(dp[amount] if dp[amount] != float('inf') else -1)