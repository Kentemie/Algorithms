# Alice and Bob take turns playing a game, with Alice starting first.

# There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from
# the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score
# when there are no stones left to remove.

# Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's
# goal is to maximize the difference in the score.

# Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in
# Alice and Bob's score if they both play optimally.

def stoneGameVII(stones):
    n = len(stones)
    prefixSum = [0] * (n + 1)

    for i in range(n):
        prefixSum[i + 1] = prefixSum[i] + stones[i]

    dp = [[-1] * n for _ in range(n)]

    def DFS(Alice, left, right):
        if left == right:
            return 0
        if dp[left][right] != -1:
            return dp[left][right]

        remove_first_stone = prefixSum[right + 1] - prefixSum[left + 1]
        remove_last_stone = prefixSum[right] - prefixSum[left]

        difference = 0 if Alice else float("-inf")

        if Alice:
            difference = max(DFS(not Alice, left + 1, right) + remove_first_stone, DFS(not Alice, left, right - 1) + remove_last_stone)
        else:
            difference = min(DFS(not Alice, left + 1, right) - remove_first_stone, DFS(not Alice, left, right - 1) - remove_last_stone)

        dp[left][right] = difference

        return difference
    
    return DFS(True, 0, n - 1)


stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]

print(stoneGameVII(stones))