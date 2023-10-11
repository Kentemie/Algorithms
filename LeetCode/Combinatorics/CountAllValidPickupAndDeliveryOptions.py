# Given n orders, each order consist in pickup and delivery services. 

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

# Since the answer may be too large, return it modulo 10^9 + 7.

def countOrders(n):
    mod = 1_000_000_007
    res = 1

    for i in range(1, n + 1):
        # Ways to arrange all pickups, 1*2*3*4*5*...*n
        res *= i
        # Ways to arrange all deliveries, 1*3*5*...*(2n-1)
        res *= (2 * i - 1)
        res %= mod

    return res 

n = 3

print(countOrders(n))