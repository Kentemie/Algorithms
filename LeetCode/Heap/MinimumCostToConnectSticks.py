# You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i]
# is the length of the ith stick.

# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks
# until there is only one stick remaining.

# Return the minimum cost of connecting all the given sticks into one stick in this way.

from heapq import heapify, heappop, heappush

def connectSticks(sticks):
    res = 0
    heapify(sticks)
    while len(sticks) > 1:
        firstMin = heappop(sticks)
        secondMin = heappop(sticks)
        combineSum = firstMin + secondMin
        res += combineSum
        heappush(sticks, combineSum)
    return res

sticks = [3354,4316,3259,4904,4598,474,3166,6322,8080,9009]

print(connectSticks(sticks))