# The divisors are paired, i.e., if i is a divisor of N, then N/i is a divisor of N, too.

def factor(n):
    factors, sqrt_n = [], int(n ** 0.5)
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)

    return factors

print(factor(16))