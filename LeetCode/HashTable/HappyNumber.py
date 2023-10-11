# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

    # Starting with any positive integer, replace the number by the sum of the squares of its digits.
    # Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    # Those numbers for which this process ends in 1 are happy.
    
# Return true if n is a happy number, and false if not.

def getNumber(n):
    totalSum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        totalSum += digit ** 2
    return totalSum

def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = getNumber(n)
    return n == 1

n = 19
n = 2 ** 31 - 1

print(isHappy(n))