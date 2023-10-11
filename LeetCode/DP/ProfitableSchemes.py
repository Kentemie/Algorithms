# There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires 
# group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

# Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of 
# members participating in that subset of crimes is at most n.

# Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 10^9 + 7.


def profitableSchemes(n, minProfit, group, profit):
    MOD = 10 ** 9 + 7
    memo = [[[-1] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group))]

    def DFS(idx, members, curr_profit):
        if idx == len(group):
            return 1 if curr_profit >= minProfit else 0
        if memo[idx][members][curr_profit] != -1:
            return memo[idx][members][curr_profit] % MOD
        
        memo[idx][members][curr_profit] = DFS(idx + 1, members, curr_profit)

        if members + group[idx] <= n:
            # take min(minProfit, curr_profit + profit[idx]), this is to reduce the number of states.
            memo[idx][members][curr_profit] += DFS(idx + 1, members + group[idx], min(minProfit, curr_profit + profit[idx]))
        
        return memo[idx][members][curr_profit] % MOD

    return DFS(0, 0, 0)

n = 5
minProfit = 3
group = [2,2]
profit = [2,3]
# Output: 2
# Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.

n = 10
minProfit = 5
group = [2,3,5]
profit = [6,7,8]
# Output: 7
# Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

n = 100
minProfit = 30
group = [6,4,1,3,7,4,5,10,6,1,3,8,10,8,6,9,9,7,1,4,1,9,5,2,8,3,1,1,9,7,10,7,7,1,4,5,4,10,3,1,2,9,2,6,3,2,6,8,8,2,7,3,4,4,6,5,6,8,3,10,7,4,2,2,6,6,1,10,8,9,4,5,6,1,6,3,8,5,3,1,9,10,4,10,3,5,7,1,3,10,2,1,1,10,8,10,1,8,10,4]
profit = [2,8,4,7,2,3,9,5,3,10,8,5,6,1,2,4,3,1,7,5,5,9,10,9,1,6,4,3,9,4,8,6,2,10,9,6,5,2,5,4,4,5,9,9,2,6,7,3,1,8,8,8,7,6,9,2,9,1,5,8,8,4,9,5,7,5,9,10,3,10,9,7,5,3,1,7,4,10,2,10,8,9,4,10,5,9,9,4,1,1,4,2,1,6,7,1,10,8,4,8]
# 376627909

print(profitableSchemes(n, minProfit, group, profit))