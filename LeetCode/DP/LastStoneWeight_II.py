# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones
# have weights x and y with x <= y. The result of this smash is:

    # If x == y, both stones are destroyed, and
    # If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

from math import ceil

def lastStoneWeightII(stones):
    dp = {}
    n = len(stones)
    stone_sum = sum(stones)
    target = ceil(stone_sum / 2)

    def DFS(i, total):
        if i == n or total >= target:
            return abs(total - (stone_sum - total))
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = min(DFS(i + 1, total), DFS(i + 1, total + stones[i]))

        return dp[(i, total)]
        
    return DFS(0, 0)

stones = [2,7,4,1,8,1]

stones = [31,26,33,21,40]

print(lastStoneWeightII(stones))
