# Extended Euclidean Algorithm: 

    # Extended Euclidean algorithm also finds integer coefficients x and y such that: ax + by = gcd(a, b) 
    # Bézout's identity — Let a and b be integers with greatest common divisor d. Then there exist integers x and y such that 
    # ax + by = d. Moreover, the integers of the form az + bt are exactly the multiples of d.

# The extended Euclidean algorithm updates the results of gcd(a, b) using the results calculated by the recursive call 
# gcd(b%a, a). Let values of x and y calculated by the recursive call be x1 and y1. x and y are updated using the below
# expressions. 

    # ax + by = gcd(a, b)
    # gcd(a, b) = gcd(b%a, a)
    # gcd(b%a, a) = (b%a)x1 + ay1
    # ax + by = (b%a)x1 + ay1
    # ax + by = (b – [b/a] * a)x1 + ay1
    # ax + by = a(y1 – [b/a] * x1) + bx1

    # Comparing LHS and RHS,
    # x = y1 – ⌊b/a⌋ * x1
    # y = x1

def GCD(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = GCD(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    print(x, y)
    return gcd, x, y

print(GCD(13, 11))