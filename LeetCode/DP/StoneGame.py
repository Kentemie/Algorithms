# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile 
# has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, 
# so there are no ties.

# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from 
# the beginning or from the end of the row. This continues until there are no more piles left, at which point the person 
# with the most stones wins.

# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

def stoneGame(i, j):
    if i > j:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    
    parity = (j - i - n) % 2
    
    if parity:
        memo[(i, j)] = max(piles[i] + stoneGame(i + 1, j), piles[j] + stoneGame(i, j - 1))
        return memo[(i, j)]
    else:
        memo[(i, j)] = min(-piles[i] + stoneGame(i + 1, j), -piles[j] + stoneGame(i, j - 1))
        return memo[(i, j)]

piles = [5,3,4,5]
piles = [3,7,2,3]

n = len(piles)
memo = {}

print(stoneGame(0, n - 1) > 0)