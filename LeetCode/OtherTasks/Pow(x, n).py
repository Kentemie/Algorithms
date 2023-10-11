# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

def binaryExponentiation(x, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 1 / binaryExponentiation(x, -1 * n)
    
    value = binaryExponentiation(x, n // 2)
    
    if n & 1:
        return x * value * value
    
    return value * value 

print(binaryExponentiation(2, -2))