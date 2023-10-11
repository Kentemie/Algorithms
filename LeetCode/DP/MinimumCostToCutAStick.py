# Given a wooden stick of length n units. The stick is labelled from 0 to n.

# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

# You should perform the cuts in order, you can change the order of the cuts as you wish.

# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, 
# it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer
# to the first example for a better explanation.

# Return the minimum total cost of the cuts.

def minCost(n, cuts):
    cuts = [0] + sorted(cuts) + [n]
    dp = [[float("inf")] * len(cuts) for _ in range(len(cuts))]

    def DFS(left, right):
        if dp[left][right] != float("inf"):
            return dp[left][right]

        if right - left == 1:
            return 0 
        
        for mid in range(left + 1, right):
            dp[left][right] = min(dp[left][right], DFS(left, mid) + DFS(mid, right) + cuts[right] - cuts[left])

        return dp[left][right]
    
    return DFS(0, len(cuts) - 1)


n = 7
cuts = [1,3,4,5]

n = 9
cuts = [5,6,1,4,2]

print(minCost(n, cuts))