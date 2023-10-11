# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and
# is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 
# 32-bit integer, return -1.

def swap(i, j):
    digits[i], digits[j] = digits[j], digits[i]

def nextGreaterElement(digits):
    pivot = len(digits) - 2

    while pivot >= 0 and digits[pivot + 1] <= digits[pivot]:
        pivot -= 1
        # n = 2147483476
    print(pivot)
    
    if pivot >= 0:
        j = len(digits) - 1
        while digits[j] <= digits[pivot]:
            j -= 1
        swap(pivot, j)
    else:
        return -1
    
    left = pivot + 1
    right = len(digits) - 1
    
    while left < right:
        swap(left, right)
        left += 1
        right -= 1
    
    newInteger = int("".join(digits))

    return newInteger if newInteger <= (2**31 - 1) else -1


n = 21
n = 2147483476

digits = []

for digit in str(n):
    digits.append(digit)

print(nextGreaterElement(digits))