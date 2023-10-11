# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the
# strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at
# least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


def successfulPairs(spells, potions, success):
    potions.sort()
    
    def search(lo, hi, val):
        while lo < hi:
            mid = (lo + hi) // 2
            if success <= val * potions[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    res = []

    for i in range(len(spells)):
        res.append(len(potions) - search(0, len(potions), spells[i]))
    
    return res
    


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

# spells = [3,1,2]
# potions = [8,5,17]
# success = 16

print(successfulPairs(spells, potions, success))