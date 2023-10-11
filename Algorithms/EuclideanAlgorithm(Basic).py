# Basic Euclidean Algorithm for GCD: 
# The algorithm is based on the below facts. 

    # If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep 
    # subtracting repeatedly the larger of two, we end up with GCD.
    # Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find the remainder 0.

def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)

print(GCD(31, 2))