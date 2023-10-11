# Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' 
# (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

# For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the
# pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza
# horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

# Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge
# number, return this modulo 10^9 + 7.


def ways(pizza, k):
    MOD = (10 ** 9) + 7
    rows = len(pizza)
    cols = len(pizza[0])
    apples = [[0] * (cols + 1) for _ in range(rows + 1)]

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            apples[row][col] = (pizza[row][col] == 'A') + \
                                apples[row + 1][col] + \
                                apples[row][col + 1] - \
                                apples[row + 1][col + 1]

    dp = [[[-1 for _ in range(k)] for _ in range(cols)] for _ in range(rows)]

    def DFS(row, col, remaining_cuts):
        if apples[row][col] == 0:
            return 0
        if remaining_cuts == 0:
            return 1
        if dp[row][col][remaining_cuts] != -1:
            return dp[row][col][remaining_cuts]
        
        res = 0

        for nr in range(row + 1, rows):
            if apples[row][col] - apples[nr][col] > 0:
                res += DFS(nr, col, remaining_cuts - 1) % MOD

        for nc in range(col + 1, cols):
            if apples[row][col] - apples[row][nc] > 0:
                res += DFS(row, nc, remaining_cuts - 1) % MOD
        
        dp[row][col][remaining_cuts] = res % MOD

        return res
    
    return DFS(0, 0, k - 1)


pizza = ["A..",
         "AAA",
         "..."]
k = 3

print(ways(pizza, k))