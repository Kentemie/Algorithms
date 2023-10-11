# There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting 
# of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti]
# (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered 
# between candles if there is at least one candle to its left and at least one candle to its right in the substring.

    # For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this 
    # substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

# Return an integer array answer where answer[i] is the answer to the ith query.

# O(nlogn)
def platesBetweenCandles(s, queries):

    def search_left(x):
        left, right = 0, len(candles)

        while left < right:
            mid = (left + right) // 2
            if candles[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    n = len(s)

    candles = [0] * (n + 1)
    plates = [0] * (n + 1)

    for i in range(n):
        if s[i] == "*":
            candles[i + 1] = candles[i]
            plates[i + 1] = plates[i] + 1
        else:
            candles[i + 1] = candles[i] + 1
            plates[i + 1] = plates[i]

    res = [0] * len(queries)

    for idx, boundaries in enumerate(queries):
        l, r = boundaries
        if candles[l + 1] == candles[l]:
            l = search_left(candles[l + 1] + 1)
        if candles[r + 1] == candles[r]:
            r = search_left(candles[r + 1])
        if l < r:
            res[idx] = plates[r] - plates[l]

    return res

# O(n)
def platesBetweenCandles2(s, queries):
    n = len(s)
    nearestRightCandle = [-1] * n 
    nearestLeftCandle = [-1] * n 
    candleCount = [0] * n
    res = [0] * len(queries)

    candle = -1
    for i in range(n):
        if s[i] == '|':
            candle = i
        nearestLeftCandle[i] = candle
    
    candle = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            candle = i
        nearestRightCandle[i] = candle

    count = 0
    for i in range(n):
        if s[i] == '|':
            count += 1
        candleCount[i] = count

    for idx, bounds in enumerate(queries):
        left, right = bounds
        leftCandle = nearestRightCandle[left]
        rightCandle = nearestLeftCandle[right]

        if leftCandle == -1 or rightCandle == -1:
            continue
        if (rightCandle - leftCandle) > 1:
            res[idx] = rightCandle - leftCandle + 1 - (candleCount[rightCandle] - candleCount[leftCandle] + 1)

    return res



s = "**|**|***|"
queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.

s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.


# print(platesBetweenCandles(s, queries))
print(platesBetweenCandles2(s, queries))