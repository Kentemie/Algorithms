# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range,
# inclusive.


# Shift both numbers to the right, until the numbers become equal, i.e. the numbers are reduced into their 
# common prefix. Then append zeros to the common prefix in order to obtain the desired result, by shifting the common prefix 
# to the left.

def rangeBitwiseAnd(left, right):
    cnt = 0

    while left != right:
        left >>= 1
        right >>= 1
        cnt += 1
    
    return left << cnt


left = 5
right = 7

print(rangeBitwiseAnd(left, right))