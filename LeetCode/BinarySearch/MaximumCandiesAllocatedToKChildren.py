# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i].
# You can divide each pile into any number of sub piles, but you cannot merge two piles together.

# You are also given an integer k. You should allocate piles of candies to k children such that each child gets the 
# same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

# Return the maximum number of candies each child can get.

def maximumCandies(candies, k):
    n = len(candies)
    left = 1
    right = max(candies)
    ans = 0

    while left <= right:
        numOfPiles = 0
        mid = (left + right) // 2

        for i in range(n):
            numOfPiles += candies[i] // mid
        
        if numOfPiles >= k:
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans

candies = [5,8,6]
k = 3

print(maximumCandies(candies, k))