# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of
# an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

def binarySearch(left, right, query):
    while left < right:
        mid = (left + right) // 2
        if query < items[mid][0]:
            right = mid
        else:
            left = mid + 1
    return left

def maximumBeauty(items, queries):
    items.sort()
    mostBeautySoFar = 0
    for item in items:
        mostBeautySoFar = max(mostBeautySoFar, item[1])
        item[1] = mostBeautySoFar
    res = []
    for query in queries:
        if query < items[0][0]:
            res.append(0)
        elif query >= items[-1][0]:
            res.append(items[-1][1])
        else:
            pos = binarySearch(0, len(items) - 1, query) - 1
            res.append(items[pos][1])
    return res 

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
# [2,4,5,5,6,6]

items = [[1,2],[1,2],[1,3],[1,4]]
queries = [1]
# [4]

items = [[10,1000]]
queries = [5]
# [0]

print(maximumBeauty(items, queries))
