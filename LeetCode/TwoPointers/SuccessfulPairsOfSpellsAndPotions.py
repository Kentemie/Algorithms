def successfulPairs(spells, potions, success):
    sorted_spells = [(spell, idx) for idx, spell in enumerate(spells)]
        
    potions.sort()
    sorted_spells.sort()

    res = [0] * len(spells)
    m = len(potions)
    j = m - 1

    for spell, i in sorted_spells:
        while j >= 0 and (spell * potions[j]) >= success:
            j -= 1
        res[i] = m - (j + 1)
    
    return res

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

# spells = [3,1,2]
# potions = [8,5,17]
# success = 16

print(successfulPairs(spells, potions, success))