# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original,
# and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array.
# The elements in original may be returned in any order.

def findOriginalArray(changed):
    if len(changed) % 2:
        return []
    
    changed.sort()
    counter = {}

    for num in changed:
        counter[num] = counter.get(num, 0) + 1

    res = []

    for num in changed:
        if counter[num] > 0:
            counter[num] -= 1
            twiceNum = num * 2
            if twiceNum in counter and counter[twiceNum] > 0:
                counter[twiceNum] -= 1
                res.append(num)
            else:
                return []
            
    return res


def findOriginalArray2(changed):
    if len(changed) % 2:
        return []
    
    maxNum = 0

    for num in changed:
        maxNum = max(maxNum, num)

    frequency = [0] * (2 * maxNum + 1)

    for num in changed:
        frequency[num] += 1

    original = []

    for num in range(maxNum + 1):
        if frequency[num] > 0:
            frequency[num] -= 1
            twiceNum = num * 2
            if frequency[twiceNum] > 0:
                frequency[twiceNum] -= 1
                original.append(num)
            else:
                return []
    
    return original

changed = [1,3,4,2,6,8]

print(findOriginalArray(changed))
print(findOriginalArray2(changed))