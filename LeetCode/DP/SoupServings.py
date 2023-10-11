# There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

#     Serve 100 ml of soup A and 0 ml of soup B,
#     Serve 75 ml of soup A and 25 ml of soup B,
#     Serve 50 ml of soup A and 50 ml of soup B, and
#     Serve 25 ml of soup A and 75 ml of soup B.

# When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations 
# with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much 
# as possible. We stop once we no longer have some quantity of both types of soup.

# Note that we do not have an operation where all 100 ml's of soup B are used first.

# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. 
# Answers within 10-5 of the actual answer will be accepted.

def soupServings(A, B):
    if A <= 0 and B <= 0:
        return 0.5
    if A <= 0 and B > 0:
        return 1
    if A > 0 and B <= 0:
        return 0
    if (A, B) in memo:
        return memo[(A, B)]

    total = 0

    for amount in serve:
        soupA = A - amount[0]
        soupB = B - amount[1]
        total += soupServings(soupA, soupB)

    memo[(A, B)] = total / 4
    
    return memo[(A, B)]


n = 50

serve = [(100, 0), (75, 25), (50, 50), (25, 75)]

memo = {}

print(soupServings(n, n))