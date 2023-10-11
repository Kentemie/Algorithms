# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in 
# candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

from collections import Counter

def combinationSum2(candidates, target):
    res = []
    def backTracking(curr, target, i, counter):
        if target == 0:
            res.append(curr.copy())
            return 
        if target < 0:
            return 
        for j in range(i, len(counter)):
            candidate, freq = counter[j]
            if freq <= 0:
                continue
            curr.append(candidate)
            counter[j] = (candidate, freq - 1)
            backTracking(curr, target - candidate, j, counter)
            curr.pop()
            counter[j] = (candidate, freq)

    counter = Counter(candidates)
    counter = [(c, counter[c]) for c in counter]
    print(counter)

    backTracking([], target, 0, counter)

    return res


candidates = [10,1,2,7,6,1,5]
target = 8
# candidates = [2,5,2,1,2]
# target = 5

print(combinationSum2(candidates, target))
