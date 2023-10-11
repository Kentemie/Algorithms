from math import sqrt

def Sieve_of_Eratosthenes(n):
    primes = [i for i in range(n + 1)]
    primes[1] = 0
    i = 2

    while i <= sqrt(n):
        if primes[i] != 0:
            j = i + i
            while j <= n:
                primes[j] = 0
                j += i
        i += 1

    return { num for num in primes if num != 0 }

def prime_factors(n):
    seen = set()

    for prime in primes:
        while n % prime == 0:

            if prime in seen:
                return False
            
            seen.add(prime)
            n //= prime
    
    return True

primes = Sieve_of_Eratosthenes(30)

print(prime_factors(30))