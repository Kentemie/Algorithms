# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by
# an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    # You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of 
    # fruit each basket can hold.
    # Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) 
    # while moving to the right. The picked fruits must fit in one of your baskets.
    # Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

# Given the integer array fruits, return the maximum number of fruits you can pick.

from collections import defaultdict

def totalFruit(fruits):
    seen = defaultdict(int)
    left = right = maxLen = 0
    
    while right < len(fruits):
        seen[fruits[right]] = right
        if len(seen) > 2:
            idx = min(seen.values())
            del seen[fruits[idx]]
            left = idx + 1
        maxLen = max(maxLen, (right - left + 1))
        right += 1

    return maxLen

fruits = [1,2,1]

print(totalFruit(fruits))