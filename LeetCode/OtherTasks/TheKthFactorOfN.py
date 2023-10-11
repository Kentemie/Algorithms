# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has 
# less than k factors.

def kthFactor(n, k):
    factors, sqrt_n = [], int(n ** 0.5)

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            k -= 1
            factors.append(i)
            if k == 0:
                return i
            
    # If n is a perfect square
    # we have to skip the duplicate 
    # in the factor list
    if sqrt_n * sqrt_n == n:
        k += 1
    
    return n // factors[len(factors) - k] if k <= len(factors) else -1


n = 16
k = 4

print(kthFactor(n, k))