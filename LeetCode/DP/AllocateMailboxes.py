# Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate
# k mailboxes in the street.
# Return the minimum total distance between each house and its nearest mailbox.


# Algorithm:

    # The idea is we try to allocate each mailbox to k group of the consecutive houses houses[i:j]. We found a solution 
    # if we can distribute total k mailboxes to n houses divided into k groups [0..i], [i+1..j], ..., [l..n-1].

    # After all, we choose the minimum cost among our solutions.

    # Let costs[i][j] is the total travel distance from houses houses[i:j] to a mailbox when putting the mailbox among
    # houses[i:j], the best way is put the mail box at median position among houses[i:j]

def minDistance(houses, k):
    n = len(houses)
    houses.sort()
    costs = [[0] * n for _ in range(n)]
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            medianPos = houses[(i + j) // 2]
            for m in range(i, j + 1):
                costs[i][j] += abs(medianPos - houses[m])

    for row in costs:
        print(row)

    def DP(i, k):
        if i == n and k == 0:
            return 0
        if i == n or k == 0:
            return float('inf')
        if dp[i][k]:
            return dp[i][k]

        res = float('inf')

        for j in range(i, n):
            cost = costs[i][j] # Try to put a mailbox among house[i:j]
            res = min(res, cost + DP(j + 1, k - 1))
        dp[i][k] = res 

        return dp[i][k]
    
    return DP(0, k)

houses = [1,4,8,10,20]
k = 3

print(minDistance(houses, k))