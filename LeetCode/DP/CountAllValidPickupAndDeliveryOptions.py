# Given n orders, each order consist in pickup and delivery services. 

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

# Since the answer may be too large, return it modulo 10^9 + 7.


def countOrders(n):
    mod = 1_000_000_007
    memo = [[-1] * (n + 1) for _ in range(n + 1)]

    def DFS(unpicked, undelivered):
        if unpicked == 0 and undelivered == 0:
            return 1
        if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
            return 0
        if memo[unpicked][undelivered] != -1:
            return memo[unpicked][undelivered]
        
        memo[unpicked][undelivered] = ((unpicked * DFS(unpicked - 1, undelivered)) % mod) \
              + (((undelivered - unpicked) * DFS(unpicked, undelivered - 1)) % mod)
        
        return memo[unpicked][undelivered]
    
    return DFS(n, n)

n = 3

print(countOrders(n))


