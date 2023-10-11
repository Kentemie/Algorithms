# There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a
# positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

def maxValueOfCoins(piles, k):
    n = len(piles)
    dp = [[-1] * (k + 1) for _ in range(n)]

    def DFS(i, coins):
        if i == n:
            return 0
        
        if dp[i][coins] != -1:
            return dp[i][coins]

        dp[i][coins] = DFS(i + 1, coins)
        currPile = 0

        for j in range(min(coins, len(piles[i]))):
            currPile += piles[i][j]
            dp[i][coins] = max(dp[i][coins], currPile + DFS(i + 1, coins - j - 1))


        return dp[i][coins]
    
    return DFS(0, k)

piles = [[1,100,3],[7,8,9]]
k = 2

piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
k = 7

print(maxValueOfCoins(piles, k))