# There is a garden of n flowers, and each flower has an integer beauty value. The flowers are arranged in a line. You are 
# given an integer array flowers of size n and each flowers[i] represents the beauty of the ith flower.

# A garden is valid if it meets these conditions:

    # The garden has at least two flowers.
    # The first and the last flower of the garden have the same beauty value.

# As the appointed gardener, you have the ability to remove any (possibly none) flowers from the garden. You want to remove
# flowers in a way that makes the remaining garden valid. The beauty of the garden is the sum of the beauty of all the
# remaining flowers.

# Return the maximum possible beauty of some valid garden after you have removed any (possibly none) flowers.

def maximumBeauty(flowers):
    hashMap, prefSums, res = {}, [0], float('-inf')
    for i, beauty in enumerate(flowers):
        prefSums.append(prefSums[-1] + beauty * (beauty > 0))

        if beauty not in hashMap:
            hashMap[beauty] = i
        else:
            res = max(res, 2 * beauty * (beauty < 0) + prefSums[-1] - prefSums[hashMap[beauty]])

    return res


flowers = [1,2,3,1,2]
# Output: 8
# Explanation: You can produce the valid garden [2,3,1,2] to have a total beauty of 2 + 3 + 1 + 2 = 8.

flowers = [100,1,1,-3,1]
# Output: 3
# Explanation: You can produce the valid garden [1,1,1] to have a total beauty of 1 + 1 + 1 = 3.

flowers = [-1,-2,0,-1]
# Output: -2
# Explanation: You can produce the valid garden [-1,-1] to have a total beauty of -1 + -1 = -2.

print(maximumBeauty(flowers))