# Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile 
# has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

# Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  
# Then, we set M = max(M, X).

# The game continues until all the stones have been taken.

# Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

def stoneGameII(piles):
    n = len(piles)
    dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

    def DFS(turn, i, M): # turn = 1 if Alice else 0 (Bob)
        if i == n:
            return 0
        if dp[turn][i][M] != -1:
            return dp[turn][i][M]
        
        res = 0 if turn else float("inf")
        stones = 0

        for X in range(1, min(2 * M, n - i) + 1):
            stones += piles[i + X - 1]
            
            if turn:
                res = max(res, stones + DFS(not turn, i + X, max(M, X)))
            else:
                res = min(res, DFS(not turn, i + X, max(M, X)))
        
        dp[turn][i][M] = res

        return res
    
    return DFS(1, 0, 1)


piles = [2,7,9,4,4]
# 10
piles = [1,2,3,4,5,100]
# 104

print(stoneGameII(piles))